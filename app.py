"""
==========================================================
File: app.py
Project: AgroSentry

Description:
    Single entry point that runs both:
      1. The REST API (predict / history / stats) built on
         top of the existing inference and service modules.
      2. The static frontend dashboard (leaf-scan-dashboard.html),
         served directly so you only need one command to run
         everything.

    This does NOT modify or replace the Streamlit app — it's a
    separate, self-contained way to run the custom frontend.

Folder layout expected:
    AgroSentry/
    ├── app.py                          <- this file, project root
    ├── config.py
    ├── frontend/
    │   └── leaf-scan-dashboard.html    <- the dashboard file
    ├── pages/                          <- existing Streamlit pages (untouched)
    ├── src/
    └── ...

Install (fastapi + python-multipart are missing from requirements.txt):
    pip install fastapi python-multipart uvicorn --break-system-packages

Run:
    uvicorn app:app --reload --host 0.0.0.0 --port 8000

Then open:
    http://localhost:8000/          -> the dashboard
    http://localhost:8000/api       -> health check
    http://localhost:8000/docs      -> interactive API docs (auto-generated)
==========================================================
"""

import io
from pathlib import Path
from typing import List

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image

from config import MODEL_PATH, APP_NAME, APP_VERSION

from src.inference.class_names import load_class_names
from src.inference.predictor import load_trained_model, predict_image
from src.inference.disease_info import get_disease_info
from src.services.history_service import (
    save_prediction,
    get_history_dataframe,
    get_statistics,
    clear_history,
)


# =============================================================================
# Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent
FRONTEND_DIR = PROJECT_ROOT / "frontend"
FRONTEND_FILE = FRONTEND_DIR / "leaf-scan-dashboard.html"


# =============================================================================
# App setup
# =============================================================================

app = FastAPI(title=APP_NAME, version=APP_VERSION)

# Loosen this to your actual frontend origin before deploying anywhere public.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Loaded lazily once, equivalent to Streamlit's @st.cache_resource / @st.cache_data
_model = None
_class_names = None


def get_model():
    global _model
    if _model is None:
        _model = load_trained_model(MODEL_PATH)
    return _model


def get_class_names():
    global _class_names
    if _class_names is None:
        _class_names = load_class_names()
    return _class_names


# =============================================================================
# Frontend — served directly so one command runs everything
# =============================================================================

@app.get("/", include_in_schema=False)
def serve_frontend():
    if not FRONTEND_FILE.exists():
        raise HTTPException(
            status_code=404,
            detail=(
                f"Frontend file not found at {FRONTEND_FILE}. "
                "Place leaf-scan-dashboard.html inside a 'frontend/' folder "
                "next to app.py, or update FRONTEND_FILE above."
            ),
        )
    return FileResponse(FRONTEND_FILE)


# =============================================================================
# API health check
# =============================================================================

@app.get("/api")
def health():
    return {"status": "ok", "app": APP_NAME, "version": APP_VERSION}


# =============================================================================
# Predict
# =============================================================================

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")

    try:
        raw_bytes = await image.read()
        pil_image = Image.open(io.BytesIO(raw_bytes)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Could not read image file.")

    model = get_model()
    class_names = get_class_names()

    predicted_class, predicted_index, confidence, probabilities = predict_image(
        model, pil_image, class_names
    )

    disease = get_disease_info(predicted_class)

    try:
        crop_name = predicted_class.split("___")[0]
        disease_name = predicted_class.split("___")[1]
    except IndexError:
        crop_name = disease.get("crop", "Unknown")
        disease_name = disease.get("display_name", predicted_class)

    # Rank all 38 classes by probability, return the top 5 for the UI
    ranked = sorted(
        zip(class_names, probabilities.tolist()),
        key=lambda pair: pair[1],
        reverse=True,
    )

    predictions: List[dict] = [
        {
            "disease": get_disease_info(cls_name).get("display_name", cls_name),
            "confidence": round(float(prob), 4),
        }
        for cls_name, prob in ranked[:5]
    ]

    save_prediction(
        image_name=image.filename,
        crop=crop_name,
        disease=disease_name,
        confidence=confidence * 100,
        prediction_type="Disease Detection",
        status="Success",
    )

    return {
        "predicted_class": predicted_class,
        "confidence": round(float(confidence), 4),
        "predictions": predictions,
        "disease_info": disease,
    }


# =============================================================================
# History
# =============================================================================

@app.get("/history")
def history():
    df = get_history_dataframe()
    return df.to_dict(orient="records")


@app.delete("/history")
def delete_history():
    clear_history()
    return {"status": "cleared"}


@app.get("/stats")
def stats():
    return get_statistics()


# =============================================================================
# Optional: expose the frontend folder for any extra static assets
# (images, css, js) if you split those out later.
# =============================================================================

if FRONTEND_DIR.exists():
    app.mount("/assets", StaticFiles(directory=FRONTEND_DIR), name="assets")
<h1 align="center">AgroSentry</h1>
<p align="center"><b>AI Crop Health Intelligence Platform for Disease Detection and Explainable AI</b></p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.13-blue">
  <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-2.21-orange">
  <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-1.59-red">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-0.115-teal">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## Overview

AgroSentry is a deep learning platform that identifies crop leaf diseases from photographs and explains its reasoning visually. It combines a fine-tuned **EfficientNetB0** classifier trained on the **PlantVillage** dataset (38 classes) with **Grad-CAM** explainability, a searchable disease knowledge base, and prediction analytics — delivered through two independent frontends built on the same inference core: a multi-page **Streamlit** application and a custom **FastAPI + HTML/JS** dashboard.

---

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Running the Streamlit App](#running-the-streamlit-app)
- [Running the FastAPI + Custom Frontend](#running-the-fastapi--custom-frontend)
- [Model Details](#model-details)
- [API Reference](#api-reference)
- [Roadmap](#roadmap)
- [License](#license)

---

## Features

| Capability | Description |
|---|---|
| **Disease Detection** | Upload a leaf image and receive a ranked prediction across 38 crop/disease classes with confidence scores. |
| **Grad-CAM Explainability** | Visual heatmap overlay showing exactly which regions of the leaf influenced the model's decision. |
| **Disease Knowledge Base** | Full reference for every class — symptoms, treatment, prevention, organic and chemical control, farmer tips. |
| **Prediction Analytics** | Historical trends: totals, healthy vs. diseased breakdown, per-crop and per-disease charts, confidence over time. |
| **Dual Frontend** | A full Streamlit application for interactive use, and a standalone REST API + static dashboard for integration elsewhere. |

---

## Architecture

Both frontends sit on top of the same **service layer**, which wraps the inference core (model loading, preprocessing, prediction, Grad-CAM) and the history store. This keeps predictions and history consistent no matter which frontend is used.

**Layer 1 — Frontends**
- `Streamlit App` (`main.py` + `pages/`) — calls the service layer directly, in-process.
- `Custom Frontend` (`frontend/leaf-scan-dashboard.html`) — calls the service layer over HTTP, via FastAPI.

**Layer 2 — API (custom frontend only)**
- `FastAPI` (`app.py`) — exposes `/predict`, `/history`, `/stats`, and serves the custom frontend itself.

**Layer 3 — Service Layer** (`src/services/`)
- `prediction_service.py` — model loading and inference
- `disease_service.py` — disease metadata lookups
- `gradcam_service.py` — Grad-CAM heatmap generation
- `history_service.py` — reading and writing prediction history

**Layer 4 — Core resources**
- Inference core (`src/inference/`) — `predictor.py`, `image_utils.py`, `gradcam.py`
- Model and data — `models/best_model.keras`, `data/class_names.json`, `data/disease_info.json`
- History store — `outputs/history.csv`

---

## Screenshots

> Add your own screenshots to `docs/images/` using the filenames below — they will render automatically once added.

### Detection
<p align="center">
  <img src="docs/images/screenshot-detection.png" alt="Detection page screenshot" width="90%">
</p>

### Dashboard
<p align="center">
  <img src="docs/images/screenshot-dashboard.png" alt="Dashboard page screenshot" width="90%">
</p>

### Explainability (Grad-CAM)
<p align="center">
  <img src="docs/images/screenshot-explainability.png" alt="Explainability page screenshot" width="90%">
</p>

### Knowledge Base
<p align="center">
  <img src="docs/images/screenshot-knowledge.png" alt="Knowledge page screenshot" width="90%">
</p>

### Analytics
<p align="center">
  <img src="docs/images/screenshot-analytics.png" alt="Analytics page screenshot" width="90%">
</p>

---

## Tech Stack

- **Model / Training:** TensorFlow, Keras, EfficientNetB0 (transfer learning), scikit-learn
- **Explainability:** Grad-CAM (custom implementation)
- **Backend API:** FastAPI, Uvicorn
- **Frontend (Option 1):** Streamlit (multi-page app)
- **Frontend (Option 2):** Static HTML, CSS, JavaScript
- **Data handling:** Pandas, NumPy, Pillow, OpenCV
- **Dataset:** PlantVillage (38 classes)

---

## Project Structure

```
AgroSentry/
├── main.py                       # Streamlit entry point
├── app.py                        # FastAPI entry point (API + serves custom frontend)
├── config.py                     # Central configuration
├── requirements.txt
│
├── assets/
│   └── theme.css                 # Global Streamlit theme
│
├── components/                   # Reusable Streamlit UI components
│   ├── hero.py
│   ├── metric_card.py
│   ├── upload_card.py
│   ├── prediction_card.py
│   ├── disease_card.py
│   └── sidebar.py
│
├── pages/                        # Streamlit multi-page sections
│   ├── 1_Detection.py
│   ├── 2_Dashboard.py
│   ├── 3_Explainability.py
│   ├── 4_Knowledge.py
│   └── 5_Analytics.py
│
├── frontend/
│   └── leaf-scan-dashboard.html  # Standalone REST-API-driven dashboard
│
├── src/
│   ├── inference/                # predictor.py, class_names.py, disease_info.py,
│   │                              # image_utils.py, gradcam.py
│   ├── services/                 # prediction_service.py, disease_service.py,
│   │                              # gradcam_service.py, history_service.py
│   └── ui/                       # dashboard.py, charts.py, knowledge.py, layout.py
│
├── models/
│   └── best_model.keras
│
├── data/
│   ├── class_names.json
│   └── disease_info.json
│
├── notebooks/                    # Dataset analysis, preprocessing, training, evaluation
│
└── outputs/
    └── history.csv               # Prediction history log
```

---

## Getting Started

### Prerequisites

- Python 3.13
- pip

### Installation

```bash
git clone https://github.com/<your-username>/AgroSentry.git
cd AgroSentry

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
```

Ensure the trained model is present at the path defined by `MODEL_PATH` in `config.py` (default: `models/best_model.keras`).

---

## Running the Streamlit App

```bash
streamlit run main.py
```

Then open `http://localhost:8501` in your browser.

Pages: **Detection → Dashboard → Explainability → Knowledge → Analytics**

---

## Running the FastAPI + Custom Frontend

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

Then open `http://localhost:8000` in your browser.

- `/` — the custom HTML dashboard
- `/docs` — interactive API documentation (Swagger UI)
- `/predict`, `/history`, `/stats` — REST endpoints

---

## Model Details

| Property | Value |
|---|---|
| Architecture | EfficientNetB0 (transfer learning) |
| Classes | 38 |
| Input size | 224 × 224 |
| Dataset | PlantVillage |
| Explainability | Grad-CAM |

> Validation metrics are recorded in `config.py` and `outputs/evaluation_metrics.csv`. Note: accuracy figures should be interpreted alongside the train/validation split methodology in `notebooks/03_model_training.ipynb`, since datasets like PlantVillage are prone to inflated accuracy from near-duplicate images across splits.

---

## API Reference

### `POST /predict`
Multipart form upload, field name `image`.

**Response**
```json
{
  "predicted_class": "Tomato___Early_blight",
  "confidence": 0.87,
  "predictions": [
    { "disease": "Tomato — Early Blight", "confidence": 0.87 }
  ],
  "disease_info": {
    "display_name": "Tomato - Early Blight",
    "scientific_name": "...",
    "crop": "Tomato",
    "disease_type": "...",
    "severity": "...",
    "description": "...",
    "symptoms": ["..."],
    "treatment": ["..."],
    "prevention": ["..."],
    "organic_control": ["..."],
    "chemical_control": ["..."],
    "farmer_tips": ["..."]
  }
}
```

### `GET /history`
Returns the full prediction history log as JSON.

### `GET /stats`
Returns aggregate statistics: total predictions, healthy vs. diseased counts, average confidence.

---

## Roadmap

- [ ] Per-user/session-isolated prediction history
- [ ] Deployment to a public host (Streamlit Community Cloud / cloud VM)
- [ ] Real-world (non-lab) image robustness testing
- [ ] Automated unit tests for inference and API layers
- [ ] Batch image upload support

---

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center"><sub>Built with TensorFlow, Streamlit, and FastAPI.</sub></p>
"""
==========================================================
File: 1_Detection.py
Project: AgroSentry

Description:
    Disease Detection page. Handles image upload and
    prediction only — full breakdown lives on the
    Dashboard page.
==========================================================
"""

import numpy as np
import streamlit as st
from PIL import Image

from config import SUPPORTED_IMAGE_TYPES

from src.ui.layout import configure_page
from src.utils.theme import load_theme
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.upload_card import render_upload_card
from components.prediction_card import render_prediction_card

from src.services.prediction_service import predict, get_class_names
from src.services.disease_service import load_disease_info
from src.services.history_service import save_prediction
from src.inference.disease_info import get_disease_info


# ==========================================================
# Setup
# ==========================================================

configure_page()
load_theme()
render_sidebar()

render_hero(
    title="Crop Disease Detection",
    subtitle="Upload a crop leaf image and let AgroSentry identify the disease using AI.",
)


# ==========================================================
# Helpers
# ==========================================================

def build_top_predictions(probabilities, class_names, top_k=5):
    """
    Return the top-k predictions as display-ready dicts.
    """
    indices = np.argsort(probabilities)[::-1][:top_k]

    results = []
    for index in indices:
        class_name = class_names[index]
        info = get_disease_info(class_name)
        results.append(
            {
                "display_name": info["display_name"],
                "confidence": float(probabilities[index]),
            }
        )
    return results


# ==========================================================
# Upload
# ==========================================================

uploaded_file = render_upload_card(SUPPORTED_IMAGE_TYPES)

if uploaded_file is None:
    st.info("Upload a JPG, JPEG or PNG image to begin disease detection.")
    st.stop()

image = Image.open(uploaded_file).convert("RGB")

left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("Uploaded Image")
    st.image(image, use_container_width=True)

with right_col:
    st.subheader("Run Diagnosis")

    predict_btn = st.button("Predict Disease", use_container_width=True)

    if not predict_btn:
        st.info("Click Predict Disease to analyze the uploaded image.")
        st.stop()

    with st.spinner("Analyzing image..."):
        (
            predicted_class,
            predicted_index,
            confidence,
            probabilities,
        ) = predict(image)

    disease = load_disease_info(predicted_class)

    try:
        crop_name = predicted_class.split("___")[0]
        disease_name = predicted_class.split("___")[1]
    except IndexError:
        crop_name = disease.get("crop", "Unknown")
        disease_name = disease.get("display_name", predicted_class)

    # ------------------------------------------------------
    # Save to history
    # ------------------------------------------------------
    save_prediction(
        image_name=uploaded_file.name,
        crop=crop_name,
        disease=disease_name,
        confidence=confidence * 100,
        prediction_type="Disease Detection",
        status="Success",
    )

    # ------------------------------------------------------
    # Build top-5 predictions and stash everything for the
    # other pages (Dashboard, Explainability, Knowledge)
    # ------------------------------------------------------
    class_names = get_class_names()
    top_predictions = build_top_predictions(probabilities, class_names)

    st.session_state["last_image"] = image
    st.session_state["last_predicted_class"] = predicted_class
    st.session_state["last_confidence"] = confidence
    st.session_state["last_disease_info"] = disease
    st.session_state["last_top_predictions"] = top_predictions

    st.success("Prediction completed successfully.")

    render_prediction_card(
        disease_name=disease["display_name"],
        confidence=confidence,
        crop=disease["crop"],
        disease_type=disease["disease_type"],
        severity=disease["severity"],
    )

st.divider()

nav_col1, nav_col2, nav_col3 = st.columns(3)
with nav_col1:
    st.page_link("pages/2_Dashboard.py", label="View Full Dashboard", use_container_width=True)
with nav_col2:
    st.page_link("pages/3_Explainability.py", label="View Grad-CAM", use_container_width=True)
with nav_col3:
    st.page_link("pages/4_Knowledge.py", label="Disease Knowledge", use_container_width=True)
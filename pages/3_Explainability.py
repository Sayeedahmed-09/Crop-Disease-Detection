"""
==========================================================
File: 3_Explainability.py
Project: AgroSentry

Description:
    Grad-CAM explainability page — shows which regions of
    the leaf the model focused on to make its prediction.
==========================================================
"""

import streamlit as st
from PIL import Image

from config import SUPPORTED_IMAGE_TYPES

from src.ui.layout import configure_page
from src.utils.theme import load_theme
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.disease_card import render_description, render_section

from src.services.gradcam_service import explain_prediction
from src.services.disease_service import load_disease_info


configure_page()
load_theme()
render_sidebar()

render_hero(
    title="Grad-CAM Explainability",
    subtitle="Visualize which parts of the leaf influenced the AI's diagnosis.",
)

# ==========================================================
# Choose image: reuse last detection, or upload a new one
# ==========================================================

default_image = st.session_state.get("last_image")

st.subheader("Image")

use_last = False
if default_image is not None:
    use_last = st.checkbox("Use image from last detection", value=True)

if use_last and default_image is not None:
    image = default_image
else:
    uploaded_file = st.file_uploader(
        "Upload a Crop Leaf Image",
        type=SUPPORTED_IMAGE_TYPES,
    )
    if uploaded_file is None:
        st.info("Upload an image, or run a detection first to reuse it here.")
        st.stop()
    image = Image.open(uploaded_file).convert("RGB")

# ==========================================================
# Run Grad-CAM
# ==========================================================

with st.spinner("Generating Grad-CAM explanation..."):
    overlay, predicted_class, confidence, heatmap = explain_prediction(image)

disease = load_disease_info(predicted_class)

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Original Image")
    st.image(image, use_container_width=True)

with right_col:
    st.subheader("Grad-CAM Overlay")
    st.image(overlay, use_container_width=True)

st.divider()

st.metric("Predicted Disease", disease["display_name"])
st.metric("Confidence", f"{confidence * 100:.2f}%")

st.caption(
    "The highlighted regions show where the model focused most "
    "when making this prediction."
)

st.divider()

render_description(disease["description"])
render_section("Symptoms", "bi-clipboard2-pulse-fill", disease["symptoms"])
render_section("Treatment", "bi-capsule", disease["treatment"])

st.divider()

st.page_link("pages/4_Knowledge.py", label="View Full Disease Knowledge", use_container_width=True)
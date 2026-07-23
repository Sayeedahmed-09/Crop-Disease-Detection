"""
==========================================================
File: main.py
Project: AgroSentry

Description:
    Home page / entry point for the AgroSentry Streamlit
    application.
==========================================================
"""

import streamlit as st

from config import (
    APP_NAME,
    APP_DESCRIPTION,
    APP_VERSION,
    MODEL_NAME,
    MODEL_ACCURACY,
    NUM_CLASSES,
    DATASET_NAME,
)

from src.ui.layout import configure_page
from src.utils.theme import load_theme
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.metric_card import render_metric_card


# ==========================================================
# Setup
# ==========================================================

configure_page()
load_theme()
render_sidebar()


# ==========================================================
# Hero
# ==========================================================

render_hero(
    title=APP_NAME,
    subtitle=APP_DESCRIPTION,
)


# ==========================================================
# Model snapshot
# ==========================================================

st.subheader("Model Snapshot")

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_metric_card("Model", MODEL_NAME, "bi-cpu-fill")

with col2:
    render_metric_card("Validation Accuracy", f"{MODEL_ACCURACY}%", "bi-bullseye")

with col3:
    render_metric_card("Classes", str(NUM_CLASSES), "bi-diagram-3-fill")

with col4:
    render_metric_card("Dataset", DATASET_NAME, "bi-database-fill")

st.divider()


# ==========================================================
# Navigation
# ==========================================================

st.subheader("Get Started")

nav_col1, nav_col2, nav_col3 = st.columns(3)

with nav_col1:
    st.page_link(
        "pages/1_Detection.py",
        label="Run Disease Detection",
        use_container_width=True,
    )

with nav_col2:
    st.page_link(
        "pages/3_Explainability.py",
        label="View Grad-CAM Explainability",
        use_container_width=True,
    )

with nav_col3:
    st.page_link(
        "pages/5_Analytics.py",
        label="View Prediction Analytics",
        use_container_width=True,
    )

st.divider()

st.caption(f"{APP_NAME} | Version {APP_VERSION}")
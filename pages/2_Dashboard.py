"""
==========================================================
File: 2_Dashboard.py
Project: AgroSentry

Description:
    Full prediction dashboard — summary, top predictions,
    and confidence charts for the most recent detection.
==========================================================
"""

import streamlit as st

from src.ui.layout import configure_page
from src.utils.theme import load_theme
from components.sidebar import render_sidebar
from components.hero import render_hero

from src.ui.dashboard import render_prediction_dashboard
from src.ui.charts import render_prediction_charts


configure_page()
load_theme()
render_sidebar()

render_hero(
    title="Prediction Dashboard",
    subtitle="Full breakdown of your most recent disease detection.",
)

if "last_disease_info" not in st.session_state:
    st.warning("No prediction yet. Run a detection first.")
    st.page_link("pages/1_Detection.py", label="Go to Detection", use_container_width=True)
    st.stop()

disease_info = st.session_state["last_disease_info"]
confidence = st.session_state["last_confidence"]
top_predictions = st.session_state["last_top_predictions"]

render_prediction_dashboard(
    disease_info=disease_info,
    confidence=confidence,
    top_predictions=top_predictions,
)

st.divider()

render_prediction_charts(
    confidence=confidence,
    predictions=top_predictions,
)

st.divider()

nav_col1, nav_col2 = st.columns(2)
with nav_col1:
    st.page_link("pages/3_Explainability.py", label="View Grad-CAM", use_container_width=True)
with nav_col2:
    st.page_link("pages/4_Knowledge.py", label="Full Disease Knowledge", use_container_width=True)
"""
==========================================================
File: 5_Analytics.py
Project: AgroSentry

Description:
    Prediction history analytics — totals, healthy vs
    diseased breakdown, and trends over time.
==========================================================
"""

import pandas as pd
import streamlit as st

from src.ui.layout import configure_page
from src.utils.theme import load_theme
from components.sidebar import render_sidebar
from components.hero import render_hero
from components.metric_card import render_metric_card

from src.services.history_service import (
    get_history_dataframe,
    get_statistics,
    clear_history,
)


configure_page()
load_theme()
render_sidebar()

render_hero(
    title="📈 Prediction Analytics",
    subtitle="Trends and statistics across every prediction AgroSentry has made.",
)

history = get_history_dataframe()

if history.empty:
    st.info("No predictions recorded yet — run a detection to start building analytics.")
    st.page_link("pages/1_Detection.py", label="🔍 Go to Detection →", use_container_width=True)
    st.stop()

stats = get_statistics()

# ==========================================================
# Summary metrics
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    render_metric_card("Total Predictions", str(stats["total_predictions"]), "bi-graph-up")

with col2:
    render_metric_card("Healthy", str(stats["healthy_predictions"]), "bi-check-circle-fill")

with col3:
    render_metric_card("Diseased", str(stats["diseased_predictions"]), "bi-exclamation-triangle-fill")

with col4:
    render_metric_card("Avg. Confidence", f"{stats['average_confidence']:.2f}%", "bi-bullseye")

st.divider()

# ==========================================================
# Trends
# ==========================================================

left_col, right_col = st.columns(2)

with left_col:
    st.subheader("🌾 Predictions by Crop")
    crop_counts = history["Crop"].value_counts()
    st.bar_chart(crop_counts)

with right_col:
    st.subheader("🦠 Predictions by Disease")
    disease_counts = history["Disease"].value_counts()
    st.bar_chart(disease_counts)

st.subheader("📈 Confidence Over Time")
history_sorted = history.copy()
history_sorted["Timestamp"] = pd.to_datetime(history_sorted["Timestamp"])
history_sorted = history_sorted.sort_values("Timestamp")
st.line_chart(history_sorted.set_index("Timestamp")["Confidence"])

st.divider()

# ==========================================================
# Raw history table
# ==========================================================

st.subheader("🕒 Full Prediction History")
st.dataframe(history.sort_values("Timestamp", ascending=False), use_container_width=True)

with st.expander("⚠ Clear history"):
    st.warning("This permanently deletes all recorded predictions.")
    if st.button("Clear all history", type="primary"):
        clear_history()
        st.success("History cleared.")
        st.rerun()
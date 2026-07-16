"""
dashboard.py

Displays the prediction dashboard for AgriVision AI.

Contains:
    - Prediction Summary
    - Top Predictions
"""

from typing import Dict, List

import streamlit as st

from src.inference.prediction_utils import (
    confidence_color,
    confidence_level,
    confidence_message,
)


def render_prediction_summary(
    disease_info: Dict,
    confidence: float,
) -> None:
    """
    Display the main prediction summary.
    """

    confidence_percentage = confidence * 100

    left_column, right_column = st.columns(2)

    with left_column:

        with st.container(border=True):

            st.subheader("🦠 Disease")

            st.markdown(
                f"### {disease_info['display_name']}"
            )

        with st.container(border=True):

            st.subheader("🌱 Crop")

            st.write(
                disease_info["crop"]
            )

        with st.container(border=True):

            st.subheader("⚠ Severity")

            st.write(
                disease_info["severity"]
            )

    with right_column:

        with st.container(border=True):

            st.subheader("🎯 Confidence")

            st.metric(
                label="Prediction Confidence",
                value=f"{confidence_percentage:.2f}%",
            )

            st.info(
                f"{confidence_color(confidence)} "
                f"{confidence_level(confidence)} Confidence"
            )

            st.caption(
                confidence_message(confidence)
            )

        with st.container(border=True):

            st.subheader("🧫 Disease Type")

            st.write(
                disease_info["disease_type"]
            )


def render_top_predictions(
    predictions: List[Dict],
) -> None:
    """
    Display Top-3 model predictions.
    """

    st.subheader("🏆 Top Predictions")

    medals = (
        "🥇",
        "🥈",
        "🥉",
    )

    for medal, prediction in zip(
        medals,
        predictions,
    ):

        confidence = prediction["confidence"] * 100

        with st.container(border=True):

            left, right = st.columns(
                [5, 1]
            )

            with left:

                st.write(
                    f"{medal} **{prediction['display_name']}**"
                )

            with right:

                st.write(
                    f"{confidence:.2f}%"
                )


def render_prediction_dashboard(
    disease_info: Dict,
    confidence: float,
    top_predictions: List[Dict],
) -> None:
    """
    Render the complete prediction dashboard.
    """

    st.header("Prediction Dashboard")

    render_prediction_summary(
        disease_info,
        confidence,
    )

    st.divider()

    render_top_predictions(
        top_predictions,
    )
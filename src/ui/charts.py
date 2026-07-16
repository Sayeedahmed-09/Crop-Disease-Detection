"""
charts.py

Visualization components for AgriVision AI.

Contains:
    - Confidence Indicator
    - Probability Distribution Chart
"""

from typing import Dict, List

import pandas as pd
import streamlit as st


def render_confidence_indicator(
    confidence: float,
) -> None:
    """
    Display model confidence.
    """

    st.subheader("🎯 Prediction Confidence")

    percentage = confidence * 100

    st.progress(confidence)

    if confidence >= 0.90:

        st.success(
            f"High Confidence ({percentage:.2f}%)"
        )

    elif confidence >= 0.70:

        st.warning(
            f"Medium Confidence ({percentage:.2f}%)"
        )

    else:

        st.error(
            f"Low Confidence ({percentage:.2f}%)"
        )


def render_probability_chart(
    predictions: List[Dict],
) -> None:
    """
    Display Top-K prediction probabilities.
    """

    if not predictions:

        st.info(
            "Prediction probabilities are unavailable."
        )

        return

    dataframe = pd.DataFrame(
        {
            "Disease": [
                prediction["display_name"]
                for prediction in predictions
            ],
            "Confidence (%)": [
                prediction["confidence"] * 100
                for prediction in predictions
            ],
        }
    )

    st.subheader(
        "📊 Top Prediction Probabilities"
    )

    st.bar_chart(
        dataframe.set_index("Disease")
    )


def render_prediction_charts(
    confidence: float,
    predictions: List[Dict],
) -> None:
    """
    Render all prediction charts.
    """

    st.header("Prediction Analytics")

    render_confidence_indicator(
        confidence,
    )

    st.divider()

    render_probability_chart(
        predictions,
    )
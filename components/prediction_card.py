"""
==========================================================
File: prediction_card.py
Project: AgroSentry

Description:
    Reusable prediction result card.
==========================================================
"""

import textwrap

import streamlit as st


def render_prediction_card(
    disease_name: str,
    confidence: float,
    crop: str,
    disease_type: str,
    severity: str,
):
    """
    Render the AI prediction result card.

    Parameters
    ----------
    disease_name : str
    confidence : float
    crop : str
    disease_type : str
    severity : str
    """

    confidence_percent = confidence * 100

    html = textwrap.dedent(
        f"""\
        <div class="prediction-card">
        <div class="prediction-header"><i class="bi bi-cpu-fill"></i><span>AI Prediction</span></div>
        <div class="prediction-disease">{disease_name}</div>
        <div class="prediction-confidence">Confidence <strong>{confidence_percent:.2f}%</strong></div>
        <div class="prediction-progress">
        <div class="prediction-progress-bar" style="width:{confidence_percent:.2f}%"></div>
        </div>
        <hr>
        <div class="prediction-grid">
        <div><small>Crop</small><h5>{crop}</h5></div>
        <div><small>Disease Type</small><h5>{disease_type}</h5></div>
        <div><small>Severity</small><h5>{severity}</h5></div>
        </div>
        </div>
        """
    )

    st.markdown(html, unsafe_allow_html=True)
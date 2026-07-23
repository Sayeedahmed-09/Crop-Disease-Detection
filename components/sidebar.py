"""
==========================================================
File: sidebar.py
Description:
    Reusable sidebar component used across all pages.
==========================================================
"""

from __future__ import annotations

import textwrap

import streamlit as st


# ==========================================================
# Sidebar
# ==========================================================

def render_sidebar() -> None:
    """
    Render the application sidebar.
    """

    with st.sidebar:

        # --------------------------------------------------
        # Logo
        # --------------------------------------------------

        header_html = textwrap.dedent(
            """\
            <div style="text-align:center;">
            <h2 style="margin-bottom:0;">AgroSentry</h2>
            <p style="color:#94A3B8;margin-top:2px;">AI Crop Health Intelligence Platform</p>
            </div>
            """
        )

        st.markdown(header_html, unsafe_allow_html=True)

        st.divider()

        # --------------------------------------------------
        # Model Information
        # --------------------------------------------------

        st.subheader("Model")

        st.markdown(
            "**Model Name**\n\n"
            "EfficientNetB0\n\n"
            "**Dataset**\n\n"
            "PlantVillage\n\n"
            "**Classes**\n\n"
            "38\n\n"
            "**Image Size**\n\n"
            "224 x 224\n\n"
            "**Epochs**\n\n"
            "5"
        )

        st.divider()

        # --------------------------------------------------
        # Explainability
        # --------------------------------------------------

        st.subheader("Explainability")

        st.markdown(
            "Grad-CAM\n\n"
            "Visual Attention Maps\n\n"
            "Disease Localization"
        )

        st.divider()

        # --------------------------------------------------
        # System Status
        # --------------------------------------------------

        st.subheader("System Status")

        st.success("AI Model Loaded")
        st.success("Prediction Engine Ready")
        st.success("Grad-CAM Ready")

        st.divider()

        # --------------------------------------------------
        # Application
        # --------------------------------------------------

        st.subheader("Application")

        st.markdown(
            "Version\n\n"
            "2.0.0\n\n"
            "Framework\n\n"
            "TensorFlow + Streamlit"
        )

        st.divider()

        # --------------------------------------------------
        # Footer
        # --------------------------------------------------

        st.caption("AgroSentry Version 2")
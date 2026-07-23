"""
layout.py

Contains all layout-related UI components:
    - Page Configuration
    - Header
    - Sidebar
    - Footer
"""

import streamlit as st

from config import (
    APP_NAME,
    APP_DESCRIPTION,
    APP_VERSION,
    MODEL_NAME,
    MODEL_ACCURACY,
)


def configure_page() -> None:
    """
    Configure the Streamlit page.
    """

    st.set_page_config(
        page_title=APP_NAME,
        layout="wide",
        initial_sidebar_state="expanded",
    )


def render_sidebar() -> None:
    """
    Render the application sidebar.
    """

    with st.sidebar:

        st.title(APP_NAME)

        st.markdown("---")

        st.subheader("About")

        st.write(
            "AgroSentry is an intelligent crop disease "
            "diagnosis system powered by deep learning."
        )

        st.markdown("---")

        st.subheader("Model Information")

        st.write(f"Model: {MODEL_NAME}")
        st.write(f"Validation Accuracy: {MODEL_ACCURACY}")
        st.write(f"Version: {APP_VERSION}")

        st.markdown("---")

        st.subheader("Project Status")

        st.success("Disease Detection")
        st.success("Knowledge Base")
        st.success("Top-3 Predictions")
        st.success("Confidence Chart")
        st.success("Grad-CAM")

        st.markdown("---")

        st.caption("Built using TensorFlow, Streamlit and EfficientNetB0")


def render_header() -> None:
    """
    Render the application header.
    """

    st.title(APP_NAME)

    st.caption(APP_DESCRIPTION)

    st.divider()


def render_footer() -> None:
    """
    Render application footer.
    """

    st.divider()

    st.caption(f"{APP_NAME} | Version {APP_VERSION}")
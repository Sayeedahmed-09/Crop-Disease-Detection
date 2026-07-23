"""
==========================================================
File: theme.py
Project: AgroSentry

Description:
    Utility for loading the global AgroSentry CSS theme.
==========================================================
"""

from pathlib import Path

import streamlit as st

from config import ASSETS_PATH


# ==========================================================
# Theme Loader
# ==========================================================

def load_theme() -> None:
    """
    Load the global CSS theme into the Streamlit application.

    This function should be called once at the beginning
    of every Streamlit page.
    """

    css_file = ASSETS_PATH / "theme.css"

    if not css_file.exists():
        st.error(f"Theme file not found:\n{css_file}")
        return

    with open(css_file, "r", encoding="utf-8") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True,
        )
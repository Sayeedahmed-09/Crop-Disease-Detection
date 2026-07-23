"""
==========================================================
File: disease_service.py
Project: AgroSentry

Description:
    Service layer for retrieving disease information,
    used by the Streamlit Disease Detection page.
==========================================================
"""

import streamlit as st

from src.inference.disease_info import get_disease_info


@st.cache_data
def load_disease_info(class_name):
    """
    Retrieve disease information for a predicted class.

    Parameters
    ----------
    class_name : str

    Returns
    -------
    dict
    """
    return get_disease_info(class_name)
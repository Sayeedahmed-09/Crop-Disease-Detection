"""
==========================================================
File: 4_Knowledge.py
Project: AgroSentry

Description:
    Disease knowledge base — browse full information for
    any class the model can recognize.
==========================================================
"""

import streamlit as st

from src.ui.layout import configure_page
from src.utils.theme import load_theme
from components.sidebar import render_sidebar
from components.hero import render_hero

from src.ui.knowledge import render_disease_information
from src.services.prediction_service import get_class_names
from src.services.disease_service import load_disease_info


configure_page()
load_theme()
render_sidebar()

render_hero(
    title="Disease Knowledge Base",
    subtitle="Browse detailed information for every disease AgroSentry can recognize.",
)

class_names = get_class_names()

# Default to the last-predicted class if one exists, otherwise the first entry
default_class = st.session_state.get("last_predicted_class", class_names[0])
default_index = (
    class_names.index(default_class) if default_class in class_names else 0
)

selected_class = st.selectbox(
    "Select a crop / disease",
    options=class_names,
    index=default_index,
    format_func=lambda name: load_disease_info(name)["display_name"],
)

disease_info = load_disease_info(selected_class)

render_disease_information(disease_info)
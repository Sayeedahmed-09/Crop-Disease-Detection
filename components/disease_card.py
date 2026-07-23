"""
==========================================================
File: disease_card.py
Project: AgroSentry

Description:
    Reusable disease information card.
==========================================================
"""

import textwrap

import streamlit as st


def render_section(title: str, icon: str, items):
    """
    Render one disease information section.
    """

    if not items:
        return

    items_html = "".join(f"<li>{item}</li>" for item in items)

    html = textwrap.dedent(
        f"""\
        <div class="disease-card">
        <div class="disease-card-title"><i class="bi {icon}"></i><span>{title}</span></div>
        <ul>{items_html}</ul>
        </div>
        """
    )

    st.markdown(html, unsafe_allow_html=True)


def render_description(description: str):
    """
    Render disease description.
    """

    html = textwrap.dedent(
        f"""\
        <div class="disease-description">
        <h4><i class="bi bi-file-earmark-medical-fill"></i> Description</h4>
        <p>{description}</p>
        </div>
        """
    )

    st.markdown(html, unsafe_allow_html=True)
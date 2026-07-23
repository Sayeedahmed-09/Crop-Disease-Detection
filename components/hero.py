"""
==========================================================
File: hero.py
Project: AgroSentry

Description:
    Reusable hero banner component used across the
    AgroSentry platform.
==========================================================
"""

import textwrap

import streamlit as st


def render_hero(
    title: str,
    subtitle: str,
):
    """
    Render the page hero section.

    Parameters
    ----------
    title : str
        Main page title.

    subtitle : str
        Short page description.
    """

    html = textwrap.dedent(
        f"""\
        <div class="hero">
        <h1>{title}</h1>
        <p>{subtitle}</p>
        </div>
        """
    )

    st.markdown(html, unsafe_allow_html=True)
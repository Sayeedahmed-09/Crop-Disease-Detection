"""
==========================================================
File: metric_card.py
Project: AgroSentry

Description:
    Reusable metric card component.
==========================================================
"""

import textwrap

import streamlit as st


def render_metric_card(
    title: str,
    value: str,
    icon: str = "bi-info-circle",
):
    """
    Render a reusable metric card.

    Parameters
    ----------
    title : str
        Metric title.

    value : str
        Metric value.

    icon : str
        Bootstrap icon class.
    """

    html = textwrap.dedent(
        f"""\
        <div class="metric-card">
        <div class="metric-icon"><i class="bi {icon}"></i></div>
        <div class="metric-content">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
        </div>
        </div>
        """
    )

    st.markdown(html, unsafe_allow_html=True)
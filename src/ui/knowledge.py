"""
knowledge.py

Displays complete disease information.

Sections
--------
- Description
- Symptoms
- Treatment
- Prevention
- Organic Control
- Chemical Control
- Farmer Tips
"""

import streamlit as st


def render_information_list(title: str, items: list) -> None:
    """
    Render a titled list of information.
    """

    st.subheader(title)

    if not items:
        st.info("Information not available.")
        return

    for item in items:
        st.markdown(f"• {item}")


def render_disease_information(
    disease_info: dict,
) -> None:
    """
    Display complete disease information.
    """

    st.header("Disease Knowledge")

    with st.container(border=True):

        st.subheader("📖 Description")

        st.write(
            disease_info.get(
                "description",
                "Information not available.",
            )
        )

    st.divider()

    render_information_list(
        "🍂 Symptoms",
        disease_info.get(
            "symptoms",
            [],
        ),
    )

    st.divider()

    render_information_list(
        "💊 Treatment",
        disease_info.get(
            "treatment",
            [],
        ),
    )

    st.divider()

    render_information_list(
        "🛡 Prevention",
        disease_info.get(
            "prevention",
            [],
        ),
    )

    st.divider()

    render_information_list(
        "🌱 Organic Control",
        disease_info.get(
            "organic_control",
            [],
        ),
    )

    st.divider()

    render_information_list(
        "🧪 Chemical Control",
        disease_info.get(
            "chemical_control",
            [],
        ),
    )

    st.divider()

    render_information_list(
        "👨‍🌾 Farmer Tips",
        disease_info.get(
            "farmer_tips",
            [],
        ),
    )
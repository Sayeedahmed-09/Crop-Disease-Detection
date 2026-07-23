"""
==========================================================
File: upload_card.py
Project: AgroSentry

Description:
    Reusable upload section for crop disease detection.
==========================================================
"""

import textwrap

import streamlit as st


def render_upload_card(supported_types):
    """
    Render the upload section.

    Parameters
    ----------
    supported_types : tuple
        Supported image extensions.

    Returns
    -------
    UploadedFile | None
    """

    html = textwrap.dedent(
        """\
        <div class="upload-card">
        <div class="upload-icon"><i class="bi bi-cloud-arrow-up-fill"></i></div>
        <h2>Upload Crop Leaf Image</h2>
        <p>Upload a clear image of a plant leaf for AI-powered disease detection.</p>
        </div>
        """
    )

    st.markdown(html, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        label="",
        type=supported_types,
        label_visibility="collapsed",
    )

    st.caption("Supported formats: JPG, JPEG, PNG")

    return uploaded_file
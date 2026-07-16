"""
uploader.py

Handles:
    - Image Upload
    - Image Preview
"""

from typing import Optional

from PIL import Image
import streamlit as st


SUPPORTED_FORMATS = (
    "jpg",
    "jpeg",
    "png",
)


def render_uploader() -> Optional[Image.Image]:
    """
    Display an image uploader and return the uploaded image.

    Returns
    -------
    PIL.Image.Image | None
        Uploaded image in RGB format if successful,
        otherwise None.
    """

    uploaded_file = st.file_uploader(
        label="📤 Upload a Crop Leaf Image",
        type=SUPPORTED_FORMATS,
    )

    if uploaded_file is None:
        return None

    try:

        image = Image.open(uploaded_file)

        return image.convert("RGB")

    except Exception as error:

        st.error(
            "Unable to read the uploaded image. "
            "Please upload a valid JPG, JPEG or PNG image."
        )

        st.exception(error)

        return None


def render_image_preview(
    image: Image.Image,
) -> None:
    """
    Display uploaded image preview.

    Parameters
    ----------
    image : PIL.Image.Image
        Uploaded image.
    """

    st.subheader("📷 Uploaded Image")

    st.image(
        image,
        width="stretch",
    )
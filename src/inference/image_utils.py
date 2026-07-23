"""
image_utils.py

Shared image processing utilities for AgriVision AI.

Used by:
    - Predictor
    - Grad-CAM
    - LIME
    - Future PDF Report
"""

from PIL import Image
import cv2
import numpy as np
import tensorflow as tf

from config import IMAGE_SIZE


def resize_image(image: Image.Image) -> Image.Image:
    """
    Resize image to model input size.

    Parameters
    ----------
    image : PIL.Image

    Returns
    -------
    PIL.Image
    """

    return image.resize(IMAGE_SIZE)


def image_to_array(image: Image.Image) -> np.ndarray:
    """
    Convert PIL image to NumPy array.

    Parameters
    ----------
    image : PIL.Image

    Returns
    -------
    np.ndarray
    """

    return tf.keras.utils.img_to_array(image)


def preprocess_image(image: Image.Image) -> np.ndarray:
    """
    Prepare image for model inference.

    Steps
    -----
    1. Resize
    2. Convert to array
    3. Add batch dimension

    Parameters
    ----------
    image : PIL.Image

    Returns
    -------
    np.ndarray
    """

    image = resize_image(image)

    image = image_to_array(image)

    image = np.expand_dims(image, axis=0)

    return image


def pil_to_numpy(image: Image.Image) -> np.ndarray:
    """
    Convert PIL image to RGB NumPy array.

    Parameters
    ----------
    image : PIL.Image

    Returns
    -------
    np.ndarray
    """

    return np.array(image)


def rgb_to_bgr(image: np.ndarray) -> np.ndarray:
    """
    Convert RGB image to OpenCV BGR format.
    """

    return cv2.cvtColor(
        image,
        cv2.COLOR_RGB2BGR,
    )


def bgr_to_rgb(image: np.ndarray) -> np.ndarray:
    """
    Convert OpenCV BGR image to RGB.
    """

    return cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB,
    )


def normalize_heatmap(
    heatmap: np.ndarray,
) -> np.ndarray:
    """
    Normalize Grad-CAM heatmap.

    Parameters
    ----------
    heatmap : np.ndarray

    Returns
    -------
    np.ndarray
    """

    heatmap = np.maximum(
        heatmap,
        0,
    )

    max_value = np.max(heatmap)

    if max_value == 0:
        return heatmap

    return heatmap / max_value
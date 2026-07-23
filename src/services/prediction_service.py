"""
==========================================================
File: prediction_service.py
Project: AgroSentry

Description:
    Service layer for loading the AI model and making
    disease predictions.
==========================================================
"""

import streamlit as st

from config import MODEL_PATH

from src.inference.class_names import load_class_names
from src.inference.predictor import (
    load_trained_model,
    predict_image,
)


@st.cache_resource
def get_model():
    """
    Load the trained model once.

    Returns
    -------
    tf.keras.Model
    """
    return load_trained_model(MODEL_PATH)


@st.cache_data
def get_class_names():
    """
    Load class names once.

    Returns
    -------
    list
    """
    return load_class_names()


def predict(image):
    """
    Perform disease prediction.

    Parameters
    ----------
    image : PIL.Image

    Returns
    -------
    tuple
    """
    model = get_model()

    class_names = get_class_names()

    return predict_image(
        model,
        image,
        class_names,
    )
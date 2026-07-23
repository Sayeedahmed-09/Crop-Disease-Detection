"""
predictor.py

Handles:
    - Model Loading
    - Image Preprocessing
    - Disease Prediction
"""

from pathlib import Path

import numpy as np
import tensorflow as tf

from src.inference.image_utils import preprocess_image


def load_trained_model(model_path: Path):
    """
    Load the trained TensorFlow model.

    Parameters
    ----------
    model_path : Path

    Returns
    -------
    tf.keras.Model
    """

    return tf.keras.models.load_model(model_path)


def predict_image(
    model,
    image,
    class_names,
):
    """
    Predict crop disease.

    Parameters
    ----------
    model
        Trained TensorFlow model.

    image
        Uploaded PIL Image.

    class_names
        List of disease classes.

    Returns
    -------
    tuple
        (
            predicted_class,
            predicted_index,
            confidence,
            probabilities,
        )
    """

    image_array = preprocess_image(image)

    predictions = model.predict(
        image_array,
        verbose=0,
    )

    probabilities = predictions[0]

    predicted_index = int(
        np.argmax(probabilities)
    )

    predicted_class = class_names[
        predicted_index
    ]

    confidence = float(
        probabilities[predicted_index]
    )

    return (
        predicted_class,
        predicted_index,
        confidence,
        probabilities,
    )
"""
prediction_utils.py

Utility functions for processing model predictions.
"""

from typing import List, Dict

import numpy as np


def get_top_predictions(
    probabilities: np.ndarray,
    class_names: List[str],
    top_k: int = 3,
) -> List[Dict]:
    """
    Return the Top-K predictions sorted by confidence.

    Parameters
    ----------
    probabilities : numpy.ndarray
        Prediction probabilities.

    class_names : list
        List of class names.

    top_k : int
        Number of predictions to return.

    Returns
    -------
    list
        List of prediction dictionaries.
    """

    top_indices = np.argsort(probabilities)[::-1][:top_k]

    predictions = []

    for index in top_indices:

        predictions.append(
            {
                "class_name": class_names[index],
                "display_name": (
                    class_names[index]
                    .replace("___", " - ")
                    .replace("_", " ")
                ),
                "confidence": float(probabilities[index]),
            }
        )

    return predictions


def confidence_level(confidence: float) -> str:
    """
    Return confidence category.
    """

    if confidence >= 0.90:
        return "High"

    if confidence >= 0.70:
        return "Medium"

    return "Low"


def confidence_color(confidence: float) -> str:
    """
    Return confidence indicator.
    """

    if confidence >= 0.90:
        return "🟢"

    if confidence >= 0.70:
        return "🟡"

    return "🔴"


def confidence_message(confidence: float) -> str:
    """
    Return a message based on confidence score.
    """

    if confidence >= 0.90:
        return (
            "The model is highly confident "
            "about this prediction."
        )

    if confidence >= 0.70:
        return (
            "The prediction appears reliable, "
            "but further inspection is recommended."
        )

    return (
        "The prediction confidence is low. "
        "Consider uploading a clearer image."
    )

from typing import List, Dict

import numpy as np


def get_top_predictions(
    probabilities: np.ndarray,
    class_names: List[str],
    top_k: int = 3,
) -> List[Dict]:
    """
    Return the Top-K predictions sorted by confidence.

    Parameters
    ----------
    probabilities : numpy.ndarray
        Prediction probabilities.

    class_names : list
        List of class names.

    top_k : int
        Number of predictions to return.

    Returns
    -------
    list
        List of prediction dictionaries.
    """

    top_indices = np.argsort(probabilities)[::-1][:top_k]

    predictions = []

    for index in top_indices:

        predictions.append(
            {
                "class_name": class_names[index],
                "display_name": (
                    class_names[index]
                    .replace("___", " - ")
                    .replace("_", " ")
                ),
                "confidence": float(probabilities[index]),
            }
        )

    return predictions


def confidence_level(confidence: float) -> str:
    """
    Return confidence category.
    """

    if confidence >= 0.90:
        return "High"

    if confidence >= 0.70:
        return "Medium"

    return "Low"


def confidence_color(confidence: float) -> str:
    """
    Return confidence indicator.
    """

    if confidence >= 0.90:
        return "🟢"

    if confidence >= 0.70:
        return "🟡"

    return "🔴"


def confidence_message(confidence: float) -> str:
    """
    Return a message based on confidence score.
    """

    if confidence >= 0.90:
        return (
            "The model is highly confident "
            "about this prediction."
        )

    if confidence >= 0.70:
        return (
            "The prediction appears reliable, "
            "but further inspection is recommended."
        )

    return (
        "The prediction confidence is low. "
        "Consider uploading a clearer image."
    )
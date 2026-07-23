"""
==========================================================
File: gradcam_service.py
Project: AgroSentry

Description:
    Service layer for generating Grad-CAM explanations,
    used by the Explainability page.

    Wraps the function-based Grad-CAM implementation in
    src/explainability/gradcam.py (get_last_conv_layer,
    make_gradcam_heatmap, overlay_heatmap).
==========================================================
"""

import numpy as np

from src.explainability.gradcam import make_gradcam_heatmap, overlay_heatmap
from src.inference.image_utils import preprocess_image
from src.services.prediction_service import get_model, get_class_names


def explain_prediction(image):
    """
    Run the full Grad-CAM pipeline on an uploaded image.

    Parameters
    ----------
    image : PIL.Image.Image

    Returns
    -------
    tuple
        (
            overlay_image,      # PIL.Image, heatmap overlaid on the original
            predicted_class,    # str, class name
            confidence,         # float, 0-1
            heatmap,            # raw heatmap array
        )
    """
    model = get_model()
    class_names = get_class_names()

    img_array = preprocess_image(image)

    # Model prediction (same shape/behaviour as predictor.predict_image,
    # done directly here since we already need img_array for the heatmap)
    predictions = model.predict(img_array, verbose=0)
    probabilities = predictions[0]
    predicted_index = int(np.argmax(probabilities))
    predicted_class = class_names[predicted_index]
    confidence = float(probabilities[predicted_index])

    heatmap = make_gradcam_heatmap(img_array, model)
    overlay = overlay_heatmap(image, heatmap)

    return overlay, predicted_class, confidence, heatmap
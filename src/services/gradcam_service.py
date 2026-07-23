"""
==========================================================
File: gradcam_service.py
Project: AgroSentry
==========================================================
"""

from src.inference.gradcam import GradCAM
from src.services.prediction_service import get_model, get_class_names


def get_gradcam_explainer():
    model = get_model()
    return GradCAM(model)


def explain_prediction(image):
    explainer = get_gradcam_explainer()
    class_names = get_class_names()

    overlay, predictions, predicted_index, heatmap = explainer.explain(image)

    predicted_class = class_names[predicted_index]
    confidence = float(predictions[0][predicted_index])

    return overlay, predicted_class, confidence, heatmap

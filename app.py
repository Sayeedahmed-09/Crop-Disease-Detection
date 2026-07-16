"""
app.py

Main entry point for AgriVision AI.
"""

import streamlit as st

from config import (
    APP_NAME,
    APP_DESCRIPTION,
    APP_ICON,
    MODEL_PATH,
)

from src.inference.predictor import (
    load_trained_model,
    predict_image,
)

from src.inference.class_names import (
    load_class_names,
)

from src.inference.disease_info import (
    get_disease_info,
)

from src.inference.prediction_utils import (
    get_top_predictions,
)

from src.ui.layout import (
    configure_page,
    render_sidebar,
    render_header,
    render_footer,
)

from src.ui.uploader import (
    render_uploader,
    render_image_preview,
)

from src.ui.dashboard import (
    render_prediction_dashboard,
)

from src.ui.knowledge import (
    render_disease_information,
)

from src.ui.charts import (
    render_prediction_charts,
)


# =============================================================================
# Cached Resources
# =============================================================================

@st.cache_resource
def load_model():
    """
    Load the trained TensorFlow model.
    """

    return load_trained_model(MODEL_PATH)


@st.cache_data
def load_classes():
    """
    Load class names.
    """

    return load_class_names()


# =============================================================================
# Main Application
# =============================================================================

def main():
    """
    Run AgriVision AI.
    """

    configure_page()

    render_sidebar()

    render_header()

    model = load_model()

    class_names = load_classes()

    uploaded_image = render_uploader()

    if uploaded_image is None:

        st.info(
            "Upload a crop leaf image to begin disease detection."
        )

        render_footer()

        return

    render_image_preview(
        uploaded_image,
    )
        # =========================================================================
    # Prediction
    # =========================================================================

    with st.spinner("Analyzing crop leaf..."):

        predicted_class, confidence, probabilities = predict_image(
            model=model,
            image=uploaded_image,
            class_names=class_names,
        )

    # =========================================================================
    # Process Prediction Results
    # =========================================================================

    disease_info = get_disease_info(
        predicted_class,
    )

    top_predictions = get_top_predictions(
        probabilities=probabilities,
        class_names=class_names,
        top_k=3,
    )
        # =========================================================================
    # Prediction Dashboard
    # =========================================================================

    render_prediction_dashboard(
        disease_info=disease_info,
        confidence=confidence,
        top_predictions=top_predictions,
    )

    # =========================================================================
    # Disease Knowledge
    # =========================================================================

    render_disease_information(
        disease_info=disease_info,
    )

    # =========================================================================
    # Prediction Analytics
    # =========================================================================

    render_prediction_charts(
        confidence=confidence,
        predictions=top_predictions,
    )

    # =========================================================================
    # Footer
    # =========================================================================

    render_footer()


# =============================================================================
# Application Entry Point
# =============================================================================

if __name__ == "__main__":
    main()
from pathlib import Path

import numpy as np
import tensorflow as tf

from config import IMAGE_SIZE


def load_trained_model(model_path: Path):
    """
    Load the trained TensorFlow model.
    """

    return tf.keras.models.load_model(model_path)


def preprocess_image(image):
    """
    Resize and preprocess the uploaded image.
    """

    image = image.resize(IMAGE_SIZE)

    image_array = tf.keras.utils.img_to_array(image)

    image_array = np.expand_dims(
        image_array,
        axis=0,
    )

    return image_array


def predict_image(model, image, class_names):
    """
    Predict the disease class for an uploaded image.

    Returns:
        predicted_class (str)
        confidence (float)
        probabilities (numpy.ndarray)
    """

    image_array = preprocess_image(image)

    predictions = model.predict(
        image_array,
        verbose=0,
    )

    probabilities = predictions[0]

    predicted_index = np.argmax(probabilities)

    predicted_class = class_names[predicted_index]

    confidence = float(probabilities[predicted_index])

    return (
        predicted_class,
        confidence,
        probabilities,
    )
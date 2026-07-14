from pathlib import Path

import numpy as np
import tensorflow as tf

from config import IMAGE_SIZE


def load_trained_model(model_path):

    model = tf.keras.models.load_model(model_path)

    return model


def predict_image(model, image_path, class_names):

    image = tf.keras.utils.load_img(
        image_path,
        target_size=IMAGE_SIZE,
    )

    image_array = tf.keras.utils.img_to_array(image)

    image_array = tf.expand_dims(
        image_array,
        axis=0,
    )

    predictions = model.predict(
        image_array,
        verbose=0,
    )

    confidence = float(np.max(predictions))

    predicted_index = int(np.argmax(predictions))

    predicted_class = class_names[predicted_index]

    return predicted_class, confidence
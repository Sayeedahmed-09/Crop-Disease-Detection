import tensorflow as tf

from config import (
    IMAGE_SIZE,
    NUM_CLASSES,
    DROPOUT_RATE,
)


def build_model():

    inputs = tf.keras.Input(shape=(*IMAGE_SIZE, 3))
    base_model = tf.keras.applications.EfficientNetB0(
        include_top=False,
        weights="imagenet",
        input_tensor=inputs
    )

    base_model.trainable = False

    x = base_model.output
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(DROPOUT_RATE)(x)

    outputs = tf.keras.layers.Dense(
        NUM_CLASSES,
        activation="softmax"
    )(x)

    model = tf.keras.Model(
        inputs=inputs,
        outputs=outputs,
        name="CropDiseaseEfficientNetB0"
    )

    return model
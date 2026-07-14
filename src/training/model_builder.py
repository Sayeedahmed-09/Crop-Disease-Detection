import tensorflow as tf

from config import (
    IMAGE_SIZE,
    NUM_CLASSES,
    DROPOUT_RATE,
)

from src.preprocessing.augmentation import get_data_augmentation


def build_model():

    inputs = tf.keras.Input(shape=(*IMAGE_SIZE, 3))

    augmentation = get_data_augmentation()

    x = augmentation(inputs)

    x = tf.keras.applications.efficientnet.preprocess_input(x)

    base_model = tf.keras.applications.EfficientNetB0(
        include_top=False,
        weights="imagenet",
    )

    base_model.trainable = False

    x = base_model(x, training=False)

    x = tf.keras.layers.GlobalAveragePooling2D()(x)

    x = tf.keras.layers.Dense(
        512,
        activation="relu"
    )(x)

    x = tf.keras.layers.Dropout(DROPOUT_RATE)(x)

    outputs = tf.keras.layers.Dense(
        NUM_CLASSES,
        activation="softmax"
    )(x)

    model = tf.keras.Model(
        inputs,
        outputs,
        name="CropDiseaseEfficientNetB0"
    )

    return model
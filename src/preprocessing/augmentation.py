import tensorflow as tf


def get_data_augmentation():

    data_augmentation = tf.keras.Sequential(
        [
            tf.keras.layers.RandomFlip("horizontal"),

            tf.keras.layers.RandomRotation(0.10),

            tf.keras.layers.RandomZoom(0.10),

            tf.keras.layers.RandomContrast(0.10),
        ],
        name="data_augmentation",
    )

    return data_augmentation
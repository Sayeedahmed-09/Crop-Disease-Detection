import tensorflow as tf
from pathlib import Path

def load_dataset(
    dataset_path,
    image_size=(224, 224),
    batch_size=32,
    validation_split=0.2,
    seed=42
):
     train_dataset = tf.keras.utils.image_dataset_from_directory(
        dataset_path,
        validation_split=validation_split,
        subset="training",
        seed=seed,
        image_size=image_size,
        batch_size=batch_size
    )
     validation_dataset = tf.keras.utils.image_dataset_from_directory(
        dataset_path,
        validation_split=validation_split,
        subset="validation",
        seed=seed,
        image_size=image_size,
        batch_size=batch_size
    )
     class_names = train_dataset.class_names
     return train_dataset, validation_dataset, class_names
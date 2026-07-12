from pathlib import Path
import tensorflow as tf

from config import (
    DATASET_PATH,
    IMAGE_SIZE,
    BATCH_SIZE,
    VALIDATION_SPLIT,
    SEED,
)

AUTOTUNE = tf.data.AUTOTUNE


def normalize_images(images, labels):
    images = tf.cast(images, tf.float32) / 255.0
    return images, labels


def load_dataset(
    dataset_path=DATASET_PATH,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    validation_split=VALIDATION_SPLIT,
    seed=SEED,
):
    dataset_path = Path(dataset_path)

    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    train_dataset = tf.keras.utils.image_dataset_from_directory(
        dataset_path,
        validation_split=validation_split,
        subset="training",
        seed=seed,
        image_size=image_size,
        batch_size=batch_size,
    )

    # Save class names before applying transformations
    class_names = train_dataset.class_names

    validation_dataset = tf.keras.utils.image_dataset_from_directory(
        dataset_path,
        validation_split=validation_split,
        subset="validation",
        seed=seed,
        image_size=image_size,
        batch_size=batch_size,
    )
    train_dataset = train_dataset.map(
        normalize_images,
        num_parallel_calls=AUTOTUNE,
    )

    validation_dataset = validation_dataset.map(
        normalize_images,
        num_parallel_calls=AUTOTUNE,
    )

    train_dataset = train_dataset.cache().prefetch(AUTOTUNE)
    validation_dataset = validation_dataset.cache().prefetch(AUTOTUNE)

    return train_dataset, validation_dataset, class_names
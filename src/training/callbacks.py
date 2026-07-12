import tensorflow as tf

from config import (
    MODELS_PATH,
    PATIENCE,
    MIN_LEARNING_RATE,
)


def get_callbacks():
    MODELS_PATH.mkdir(parents=True, exist_ok=True)

    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(
            filepath=MODELS_PATH / "best_model.keras",
            monitor="val_accuracy",
            save_best_only=True,
            verbose=1,
        ),

        tf.keras.callbacks.EarlyStopping(
            monitor="val_accuracy",
            patience=PATIENCE,
            restore_best_weights=True,
            verbose=1,
        ),

        tf.keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.2,
            patience=3,
            min_lr=MIN_LEARNING_RATE,
            verbose=1,
        ),
    ]

    return callbacks
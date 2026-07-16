"""
config.py

Global configuration for AgriVision AI.
"""

from pathlib import Path


# =============================================================================
# Project Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent

DATASET_PATH = PROJECT_ROOT / "data" / "raw" / "color"

MODELS_PATH = PROJECT_ROOT / "models"

OUTPUTS_PATH = PROJECT_ROOT / "outputs"

CLASS_NAMES_PATH = PROJECT_ROOT / "data" / "class_names.json"

DISEASE_INFO_PATH = PROJECT_ROOT / "data" / "disease_info.json"

MODEL_PATH = MODELS_PATH / "best_model.keras"


# =============================================================================
# Model Configuration
# =============================================================================

MODEL_NAME = "EfficientNetB0"

MODEL_ACCURACY = "96.37%"

IMAGE_SIZE = (224, 224)

NUM_CLASSES = 38

BATCH_SIZE = 16

VALIDATION_SPLIT = 0.20

SEED = 42

LEARNING_RATE = 1e-4

EPOCHS = 5

DROPOUT_RATE = 0.30

PATIENCE = 5

MIN_LEARNING_RATE = 1e-6


# =============================================================================
# Application Configuration
# =============================================================================

APP_NAME = "AgriVision AI"

APP_DESCRIPTION = (
    "AI-Powered Crop Disease Detection and Diagnosis System"
)

APP_VERSION = "1.0.0"

APP_ICON = "🌿"


# =============================================================================
# Upload Configuration
# =============================================================================

SUPPORTED_IMAGE_TYPES = (
    "jpg",
    "jpeg",
    "png",
)
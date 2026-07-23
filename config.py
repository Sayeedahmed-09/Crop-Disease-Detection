"""
==========================================================
File: config.py
Project: AgroSentry

Description:
    Global configuration file for the AgroSentry
    AI Crop Health Intelligence Platform.
==========================================================
"""

from pathlib import Path


# =============================================================================
# Project Paths
# =============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent

DATASET_PATH = PROJECT_ROOT / "data" / "raw" / "color"

MODELS_PATH = PROJECT_ROOT / "models"

OUTPUTS_PATH = PROJECT_ROOT / "outputs"

REPORTS_PATH = PROJECT_ROOT / "reports"

ASSETS_PATH = PROJECT_ROOT / "assets"

PAGES_PATH = PROJECT_ROOT / "pages"

CLASS_NAMES_PATH = PROJECT_ROOT / "data" / "class_names.json"

DISEASE_INFO_PATH = PROJECT_ROOT / "data" / "disease_info.json"

MODEL_PATH = MODELS_PATH / "best_model.keras"


# =============================================================================
# Model Configuration
# =============================================================================

MODEL_NAME = "EfficientNetB0"

MODEL_VERSION = "1.0"

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

MODEL_VERSION = "1.0"
MODEL_ACCURACY = 98.50   
MODEL_PRECISION = 98.20
MODEL_RECALL = 98.10
MODEL_F1_SCORE = 98.15


# =============================================================================
# Dataset Configuration
# =============================================================================

DATASET_NAME = "PlantVillage"

DATASET_VERSION = "1.0"

IMAGE_FORMATS = ("jpg", "jpeg", "png")


# =============================================================================
# Application Configuration
# =============================================================================

APP_NAME = "AgroSentry"

APP_DESCRIPTION = (
    "AI Crop Health Intelligence Platform for Disease Detection "
    "and Explainable AI"
)

APP_VERSION = "2.0.0"

AUTHOR = "Sayeed Ahmed"

PROJECT_YEAR = 2026

FRAMEWORK = "TensorFlow"

EXPLAINABILITY = "Grad-CAM"

LICENSE = "MIT"


# =============================================================================
# Theme Configuration
# =============================================================================

THEME = "Dark"

PRIMARY_COLOR = "#16A34A"

SECONDARY_COLOR = "#38BDF8"

BACKGROUND_COLOR = "#0F172A"

CARD_COLOR = "#1E293B"

SIDEBAR_COLOR = "#111827"

TEXT_COLOR = "#F8FAFC"

MUTED_TEXT_COLOR = "#94A3B8"

BORDER_COLOR = "#334155"

SUCCESS_COLOR = "#10B981"

WARNING_COLOR = "#F59E0B"

ERROR_COLOR = "#EF4444"


# =============================================================================
# Upload Configuration
# =============================================================================

SUPPORTED_IMAGE_TYPES = (
    "jpg",
    "jpeg",
    "png",
)

MAX_UPLOAD_SIZE_MB = 10


# =============================================================================
# Output Configuration
# =============================================================================

PREDICTIONS_FOLDER = OUTPUTS_PATH / "predictions"

GRAPHS_FOLDER = OUTPUTS_PATH / "graphs"

REPORTS_OUTPUT_FOLDER = OUTPUTS_PATH / "reports"


# =============================================================================
# Dashboard Configuration
# =============================================================================

SHOW_CONFIDENCE_SCORE = True

SHOW_GRADCAM = True

SHOW_DISEASE_INFORMATION = True

SHOW_MODEL_INFORMATION = True

SHOW_ANALYTICS = True


# =============================================================================
# Logging Configuration
# =============================================================================

LOG_LEVEL = "INFO"

ENABLE_CACHE = True

ENABLE_DEBUG = False
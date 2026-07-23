"""
===========================================================
AgroSentry - Prediction History Service
-----------------------------------------------------------
Stores and retrieves prediction history for Analytics,
Reports, Dashboard and Prediction History page.

Project: AgroSentry
===========================================================
"""

from pathlib import Path
from datetime import datetime
import pandas as pd


# =========================================================
# History File Configuration
# =========================================================

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

HISTORY_FILE = OUTPUT_DIR / "history.csv"

HISTORY_COLUMNS = [
    "Timestamp",
    "Image Name",
    "Crop",
    "Disease",
    "Confidence",
    "Prediction Type",
    "Status",
]


# =========================================================
# Initialize History File
# =========================================================

def initialize_history():
    """
    Creates history.csv if it doesn't exist.
    """

    if not HISTORY_FILE.exists():

        pd.DataFrame(columns=HISTORY_COLUMNS).to_csv(
            HISTORY_FILE,
            index=False,
        )


# =========================================================
# Save Prediction
# =========================================================

def save_prediction(
    image_name,
    crop,
    disease,
    confidence,
    prediction_type="Disease Detection",
    status="Success",
):
    """
    Saves one prediction into history.csv.
    """

    initialize_history()

    history = pd.read_csv(HISTORY_FILE)

    new_record = pd.DataFrame(
        [
            {
                "Timestamp": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "Image Name": image_name,
                "Crop": crop,
                "Disease": disease,
                "Confidence": round(float(confidence), 2),
                "Prediction Type": prediction_type,
                "Status": status,
            }
        ]
    )

    history = pd.concat(
        [history, new_record],
        ignore_index=True,
    )

    history.to_csv(
        HISTORY_FILE,
        index=False,
    )


# =========================================================
# Load History
# =========================================================

def load_history():
    """
    Returns the prediction history.
    """

    initialize_history()

    return pd.read_csv(HISTORY_FILE)


# =========================================================
# Clear History
# =========================================================

def clear_history():
    """
    Removes all prediction history while
    preserving the CSV structure.
    """

    pd.DataFrame(
        columns=HISTORY_COLUMNS
    ).to_csv(
        HISTORY_FILE,
        index=False,
    )


# =========================================================
# Dashboard Statistics
# =========================================================

def get_statistics():
    """
    Returns dashboard statistics.
    """

    history = load_history()

    if history.empty:

        return {
            "total_predictions": 0,
            "healthy_predictions": 0,
            "diseased_predictions": 0,
            "average_confidence": 0,
        }

    healthy = history[
        history["Disease"].str.contains(
            "healthy",
            case=False,
            na=False,
        )
    ]

    return {
        "total_predictions": len(history),
        "healthy_predictions": len(healthy),
        "diseased_predictions": len(history) - len(healthy),
        "average_confidence": round(
            history["Confidence"].mean(),
            2,
        ),
    }


# =========================================================
# History DataFrame
# =========================================================

def get_history_dataframe():
    """
    Returns prediction history as a DataFrame.
    """

    return load_history()
"""
disease_info.py

Loads and caches the disease knowledge base.
"""

import json
from pathlib import Path


DISEASE_INFO_PATH = Path("data/disease_info.json")

_disease_database = None


def load_disease_database():
    """
    Load disease information from JSON.

    Returns
    -------
    dict
        Complete disease database.
    """

    global _disease_database

    if _disease_database is None:

        with open(
            DISEASE_INFO_PATH,
            "r",
            encoding="utf-8",
        ) as file:

            _disease_database = json.load(file)

    return _disease_database


def get_disease_info(class_name):
    """
    Return disease information for a predicted class.

    Parameters
    ----------
    class_name : str

    Returns
    -------
    dict
    """

    database = load_disease_database()

    return database.get(
        class_name,
        {
            "display_name": class_name.replace(
                "___",
                " - ",
            ).replace(
                "_",
                " ",
            ),
            "scientific_name": "Unknown",
            "crop": "Unknown",
            "disease_type": "Unknown",
            "severity": "Unknown",
            "description": "Disease information is not available.",

            "symptoms": [],
            "treatment": [],
            "prevention": [],
            "organic_control": [],
            "chemical_control": [],
            "farmer_tips": [],
        },
    )
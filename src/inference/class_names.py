"""
class_names.py

Loads and caches the class names used by the model.
"""

import json
from pathlib import Path


CLASS_NAMES_PATH = Path("data/class_names.json")

_class_names_cache = None


def load_class_names():
    """
    Load class names from disk.

    Returns
    -------
    list
        List of model class names.
    """

    global _class_names_cache

    if _class_names_cache is None:

        with open(
            CLASS_NAMES_PATH,
            "r",
            encoding="utf-8",
        ) as file:

            _class_names_cache = json.load(file)

    return _class_names_cache
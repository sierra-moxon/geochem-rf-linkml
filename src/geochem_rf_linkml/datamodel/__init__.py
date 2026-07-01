"""Data model package for geochem-rf-linkml."""

from pathlib import Path
from .geochem_rf_linkml import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "geochem_rf_linkml.yaml"

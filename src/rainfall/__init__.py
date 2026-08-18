"""Summary statistics for daily rainfall records."""

from rainfall.exceptions import InvalidRecordError, RainfallError
from rainfall.types import Record

__all__ = [
    "InvalidRecordError",
    "RainfallError",
    "Record",
]

__version__ = "0.1.0.dev0"

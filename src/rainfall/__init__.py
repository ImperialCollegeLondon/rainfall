"""Summary statistics for daily rainfall records."""

from rainfall.exceptions import InvalidRecordError, RainfallError
from rainfall.io import load_records
from rainfall.stats import mean, total_rain, wettest_day
from rainfall.types import Record

__all__ = [
    "InvalidRecordError",
    "RainfallError",
    "Record",
    "load_records",
    "mean",
    "total_rain",
    "wettest_day",
]

__version__ = "0.1.0.dev0"

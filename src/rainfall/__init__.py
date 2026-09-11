"""Summary statistics for daily rainfall records."""

from rainfall.exceptions import EmptyRecordsError, InvalidRecordError, RainfallError
from rainfall.io import load_records
from rainfall.stats import mean, moving_average, total_rain, wettest_day
from rainfall.types import Record

__all__ = [
    "EmptyRecordsError",
    "InvalidRecordError",
    "RainfallError",
    "Record",
    "load_records",
    "mean",
    "moving_average",
    "total_rain",
    "wettest_day",
]

__version__ = "0.2.0"

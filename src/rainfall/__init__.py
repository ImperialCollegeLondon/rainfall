"""Summary statistics for daily rainfall records."""

from rainfall.exceptions import EmptyRecordsError, InvalidRecordError, RainfallError
from rainfall.io import load_records
from rainfall.stats import (
    WET_DAY_THRESHOLD_MM,
    count_wet_days,
    mean,
    moving_average,
    total_rain,
    wettest_day,
)
from rainfall.types import Record

__all__ = [
    "WET_DAY_THRESHOLD_MM",
    "EmptyRecordsError",
    "InvalidRecordError",
    "RainfallError",
    "Record",
    "count_wet_days",
    "load_records",
    "mean",
    "moving_average",
    "total_rain",
    "wettest_day",
]

__version__ = "0.3.0"

"""Summary statistics for daily rainfall records."""

from collections.abc import Sequence

from rainfall._validation import validate_records
from rainfall.types import Record

WET_DAY_THRESHOLD_MM = 1.0
"""Minimum daily rainfall, in millimetres, for a day to count as wet."""


@validate_records
def count_wet_days(
    records: Sequence[Record], threshold_mm: float = WET_DAY_THRESHOLD_MM
) -> int:
    """Return the number of wet days.

    Parameters
    ----------
    records : Sequence[Record]
        Daily rainfall records in ascending date order.
    threshold_mm : float, optional
        Minimum rainfall in millimetres for a day to count as wet. Defaults to
        ``WET_DAY_THRESHOLD_MM``.

    Returns
    -------
    int
        Number of days with at least ``threshold_mm`` of rain.
    """
    return sum(1 for _date, rain_mm in records if rain_mm >= threshold_mm)


def mean(values_mm: Sequence[float]) -> float:
    """Return the arithmetic mean of rainfall values.

    Parameters
    ----------
    values_mm : Sequence[float]
        Rainfall values in millimetres.

    Returns
    -------
    float
        The mean rainfall in millimetres.
    """
    return sum(values_mm) / len(values_mm)


def moving_average(values_mm: Sequence[float], window_days: int) -> list[float]:
    """Return the moving average of daily rainfall values.

    Parameters
    ----------
    values_mm : Sequence[float]
        Daily rainfall values in millimetres, in date order.
    window_days : int
        Number of consecutive days in each window.

    Returns
    -------
    list[float]
        The mean rainfall of each window in millimetres, one value for every
        window of ``window_days`` consecutive values that fits in
        ``values_mm``.
    """
    return [
        mean(values_mm[i : i + window_days])
        for i in range(len(values_mm) - window_days)
    ]


@validate_records
def total_rain(records: Sequence[Record], start_date: str, end_date: str) -> float:
    """Return the total rainfall between two dates, inclusive.

    Parameters
    ----------
    records : Sequence[Record]
        Daily rainfall records in ascending date order.
    start_date : str
        First date to include, in ISO 8601 format.
    end_date : str
        Last date to include, in ISO 8601 format.

    Returns
    -------
    float
        Total rainfall in millimetres.
    """
    return sum(rain_mm for date, rain_mm in records if start_date <= date < end_date)


@validate_records
def wettest_day(records: Sequence[Record]) -> str:
    """Return the date with the most rainfall.

    Parameters
    ----------
    records : Sequence[Record]
        Daily rainfall records in ascending date order.

    Returns
    -------
    str
        The ISO 8601 date of the wettest day. If several days tie, the
        earliest is returned.
    """
    date, _rain_mm = max(records, key=lambda record: record[1])
    return date

"""Summary statistics for daily rainfall records."""

from collections.abc import Sequence

from rainfall.types import Record


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

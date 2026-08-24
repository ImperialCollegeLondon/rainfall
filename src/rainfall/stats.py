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

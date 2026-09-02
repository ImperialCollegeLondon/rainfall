"""Validation for functions that take rainfall records."""

import datetime as dt
import functools
from collections.abc import Callable, Sequence
from typing import Concatenate, ParamSpec, TypeVar

from rainfall.exceptions import EmptyRecordsError, InvalidRecordError
from rainfall.types import Record

P = ParamSpec("P")
R = TypeVar("R")


def validate_records(
    func: Callable[Concatenate[Sequence[Record], P], R],
) -> Callable[Concatenate[Sequence[Record], P], R]:
    """Check the records passed to a function before it runs.

    The decorated function must take its records as the first positional
    argument. The records must not be empty, every date must be in ISO 8601
    format, rainfall must not be negative, and the dates must be in strictly
    ascending order.

    Parameters
    ----------
    func : Callable
        A function whose first argument is a sequence of records.

    Returns
    -------
    Callable
        The function, wrapped so that its records are checked first.

    Raises
    ------
    EmptyRecordsError
        If the wrapped function is called with no records.
    InvalidRecordError
        If a record is malformed or the records are out of order.
    """

    @functools.wraps(func)
    def wrapper(records: Sequence[Record], /, *args: P.args, **kwargs: P.kwargs) -> R:
        _check_records(records)
        return func(records, *args, **kwargs)

    return wrapper


def _check_records(records: Sequence[Record]) -> None:
    """Raise if the records are empty, malformed or out of order."""
    if not records:
        raise EmptyRecordsError("expected at least one record")
    previous_date: dt.date | None = None
    for date, rain_mm in records:
        try:
            parsed_date = dt.date.fromisoformat(date)
        except ValueError as error:
            raise InvalidRecordError(f"not an ISO 8601 date: {date!r}") from error
        if rain_mm < 0:
            raise InvalidRecordError(f"negative rainfall on {date}: {rain_mm} mm")
        if previous_date is not None and parsed_date <= previous_date:
            raise InvalidRecordError(f"records are not in ascending order at {date}")
        previous_date = parsed_date

from collections.abc import Sequence

import pytest

from rainfall._validation import validate_records
from rainfall.exceptions import EmptyRecordsError, InvalidRecordError
from rainfall.types import Record


@validate_records
def _count(records: Sequence[Record]) -> int:
    return len(records)


def test_validate_records_accepts_valid_records(march_records: list[Record]) -> None:
    assert _count(march_records) == 3


def test_validate_records_rejects_empty_records() -> None:
    with pytest.raises(EmptyRecordsError):
        _count([])


def test_validate_records_rejects_invalid_date() -> None:
    with pytest.raises(InvalidRecordError, match="ISO 8601"):
        _count([("01/03/2026", 1.0)])


def test_validate_records_rejects_negative_rain() -> None:
    with pytest.raises(InvalidRecordError, match="negative"):
        _count([("2026-03-01", -1.0)])


def test_validate_records_rejects_unsorted_dates() -> None:
    with pytest.raises(InvalidRecordError, match="ascending"):
        _count([("2026-03-02", 1.0), ("2026-03-01", 1.0)])

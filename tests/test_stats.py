import pytest

from rainfall.exceptions import EmptyRecordsError
from rainfall.stats import mean, moving_average, wettest_day
from rainfall.types import Record


def test_mean_of_three_values() -> None:
    assert mean([1.0, 2.0, 3.0]) == 2.0


def test_moving_average_returns_values() -> None:
    assert len(moving_average([1.0, 2.0, 3.0, 4.0], 2)) > 0


def test_wettest_day_returns_date_with_most_rain(
    march_records: list[Record],
) -> None:
    assert wettest_day(march_records) == "2026-03-02"


def test_wettest_day_rejects_empty_records() -> None:
    with pytest.raises(EmptyRecordsError):
        wettest_day([])

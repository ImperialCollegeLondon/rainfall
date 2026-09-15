from pathlib import Path

import pytest

from rainfall.exceptions import InvalidRecordError
from rainfall.io import load_records


def _write_csv(tmp_path: Path, text: str) -> Path:
    path = tmp_path / "rainfall.csv"
    path.write_text(text, encoding="utf-8")
    return path


def test_load_records_reads_dates_and_rain(tmp_path: Path) -> None:
    path = _write_csv(tmp_path, "date,rain_mm\n2026-03-01,2.0\n2026-03-02,11.5\n")
    assert load_records(path) == [("2026-03-01", 2.0), ("2026-03-02", 11.5)]


def test_load_records_rejects_missing_column(tmp_path: Path) -> None:
    path = _write_csv(tmp_path, "date\n2026-03-01\n")
    with pytest.raises(InvalidRecordError, match="rain_mm"):
        load_records(path)


def test_load_records_rejects_non_numeric_rain(tmp_path: Path) -> None:
    path = _write_csv(tmp_path, "date,rain_mm\n2026-03-01,n/a\n")
    with pytest.raises(InvalidRecordError, match="not a number"):
        load_records(path)


def test_load_records_reports_date_of_non_numeric_rain(tmp_path: Path) -> None:
    path = _write_csv(tmp_path, "date,rain_mm\n2026-03-05,n/a\n")
    with pytest.raises(InvalidRecordError, match="2026-03-05"):
        load_records(path)

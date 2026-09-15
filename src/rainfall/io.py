"""Read rainfall records from CSV files."""

import csv
from pathlib import Path

from rainfall.exceptions import InvalidRecordError
from rainfall.types import Record

REQUIRED_COLUMNS = ("date", "rain_mm")


def load_records(path: str | Path) -> list[Record]:
    """Read daily rainfall records from a CSV file.

    The file must have a header row with ``date`` and ``rain_mm`` columns.

    Parameters
    ----------
    path : str or pathlib.Path
        Path to the CSV file.

    Returns
    -------
    list[Record]
        The records, in the order they appear in the file.

    Raises
    ------
    InvalidRecordError
        If a required column is missing or a rainfall value is not a number.
    """
    with Path(path).open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames or []
        missing = [name for name in REQUIRED_COLUMNS if name not in fieldnames]
        if missing:
            raise InvalidRecordError(f"missing column(s): {', '.join(missing)}")
        records: list[Record] = []
        for row in reader:
            try:
                rain_mm = float(row["rain_mm"])
            except ValueError as error:
                raise InvalidRecordError(
                    f"rain_mm is not a number on {row['date']}: {row['rain_mm']!r}"
                ) from error
            records.append((row["date"], rain_mm))
    return records

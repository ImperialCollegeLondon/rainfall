import pytest

from rainfall.types import Record


@pytest.fixture
def march_records() -> list[Record]:
    return [("2026-03-01", 2.0), ("2026-03-02", 11.5), ("2026-03-03", 1.0)]

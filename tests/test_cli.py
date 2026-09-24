from pathlib import Path

import pytest

from rainfall.cli import main


def test_main_prints_summary(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    path = tmp_path / "rainfall.csv"
    path.write_text(
        "date,rain_mm\n2026-03-01,2.0\n2026-03-02,11.5\n2026-03-03,1.0\n",
        encoding="utf-8",
    )
    assert main([str(path)]) == 0
    output = capsys.readouterr().out
    assert "Days: 3" in output
    assert "Wettest day: 2026-03-02" in output

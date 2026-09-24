"""Command-line interface for summarising rainfall records."""

import argparse
from collections.abc import Sequence

from rainfall.io import load_records
from rainfall.stats import mean, total_rain, wettest_day


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the ``rainfall`` command.

    Returns
    -------
    argparse.ArgumentParser
        The parser.
    """
    parser = argparse.ArgumentParser(
        prog="rainfall", description="Summarise daily rainfall records."
    )
    parser.add_argument("path", help="CSV file with date and rain_mm columns")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Print a summary of the rainfall records in a CSV file.

    Parameters
    ----------
    argv : Sequence[str] or None, optional
        Command-line arguments, excluding the program name. If ``None``, the
        arguments are read from ``sys.argv``.

    Returns
    -------
    int
        The exit status.
    """
    args = build_parser().parse_args(argv)
    records = load_records(args.path)
    wettest_date = wettest_day(records)
    start_date, end_date = records[0][0], records[-1][0]
    values_mm = [rain_mm for _date, rain_mm in records]
    print(f"Days: {len(records)}")
    print(f"Total: {total_rain(records, start_date, end_date):.1f} mm")
    print(f"Mean: {mean(values_mm):.1f} mm/day")
    print(f"Wettest day: {wettest_date}")
    return 0

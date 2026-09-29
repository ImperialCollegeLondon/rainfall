# rainfall

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ImperialCollegeLondon/rainfall?quickstart=1)

Summary statistics for daily rainfall records.

`rainfall` reads daily rainfall from CSV files and calculates totals, means,
moving averages and the wettest day. It is a small, fully typed Python package
with no runtime dependencies.

## Quickstart

With Python 3.10 or later and Git:

```bash
git clone https://github.com/ImperialCollegeLondon/rainfall.git
cd rainfall
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

Or open a Codespace with the button at the top of this README, which has
everything set up already.

## Installation

Requires Python 3.10 or later.

```bash
python -m pip install -e ".[dev]"
```

## Usage

A record is a `(date, rain_mm)` tuple: an ISO 8601 date and the rainfall that
day in millimetres. Functions that take records expect them in ascending date
order.

```python
from rainfall import load_records, total_rain, wettest_day

records = load_records("data/raw/rainfall_march_2026.csv")
total_rain(records, "2026-03-01", "2026-03-07")
wettest_day(records)
```

From the command line:

```bash
rainfall data/raw/rainfall_march_2026.csv
```

## Development

Run the tests, linter, formatter and type checker:

```bash
python -m pytest
ruff check .
ruff format --check .
mypy
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the conventions this project follows.
A dev container configuration is included for VS Code and GitHub Codespaces.

## Data

`data/raw/` contains example input data. See [data/README.md](data/README.md)
for its source and licence.

## Citation

If you use this software, please cite it using the metadata in
[CITATION.cff](CITATION.cff).

## Licence

BSD 3-Clause. See [LICENSE](LICENSE).

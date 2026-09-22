# Contributing to rainfall

Thanks for your interest in improving rainfall. Bug reports, fixes, new
statistics and documentation are all welcome.

If you've found a bug or want to suggest a feature, please open an issue
first. For small fixes, such as typos or an obvious bug with a test to show
it, go ahead and open a pull request.

## Setting up

You'll need Python 3.10 or later. We recommend working in a virtual
environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pre-commit install
```

The pre-commit hooks run ruff and mypy on each commit, so most problems are
caught before they reach CI. If you use VS Code, the dev container in
`.devcontainer/` gives you the same setup without installing anything
locally.

## Before you open a pull request

Please check that these all pass. CI runs the same checks on Python 3.10 to
3.13, and we can't merge until they do.

```bash
ruff check .
ruff format --check .
mypy
python -m pytest
```

## Code style

We use ruff for formatting and linting, with a line length of 88, and run mypy
in strict mode over both `src/` and `tests/`. This means every function needs
type hints, including in tests. Imports should be absolute
(`from rainfall.types import Record`) rather than relative.

### Naming

Most of our naming follows PEP 8: `snake_case` for modules, functions and
variables, `PascalCase` for classes and `UPPER_SNAKE_CASE` for constants.

The one convention that's specific to this project is that **any variable or
parameter holding a physical quantity ends with its unit**: `rain_mm`,
`values_mm`, `window_days`. Rainfall data comes in millimetres, inches and
tenths of a millimetre depending on the source, and putting the unit in the
name makes a mix-up much harder to miss in review. Dates don't need a suffix:
they're ISO 8601 strings named `date`, `start_date` or `end_date`.

Private modules and functions start with an underscore, like `_validation.py`.
Anything not listed in `rainfall.__all__` isn't part of the public API and may
change without notice.

### Docstrings

Every public module, class and function should have a docstring in the
[NumPy style](https://numpydoc.readthedocs.io/en/latest/format.html). Ruff
checks the format, but not the content, so please make sure the docstring
says what the function actually does, including the unit of every quantity.
For example:

```python
def total_rain(records: Sequence[Record], start_date: str, end_date: str) -> float:
    """Return the total rainfall between two dates, inclusive.

    Parameters
    ----------
    records : Sequence[Record]
        Daily rainfall records in ascending date order.
    start_date : str
        First date to include, in ISO 8601 format.
    end_date : str
        Last date to include, in ISO 8601 format.

    Returns
    -------
    float
        Total rainfall in millimetres.
    """
```

### Records, validation and errors

Most functions take a sequence of records, where a record is a
`(date, rain_mm)` tuple (`rainfall.types.Record`). Records always come first
in the argument list.

Every public function that takes records should be decorated with
`@validate_records` from `rainfall._validation`, rather than checking its input
itself. That way, empty, malformed or unsorted input is rejected in the same
way, with the same errors, wherever it's passed in.

When something goes wrong, please raise one of the exceptions in
`rainfall.exceptions` rather than letting a built-in one such as
`ZeroDivisionError` or `KeyError` escape. Users can then catch
`RainfallError` and know they've handled everything the package raises. If you
add a new exception, its name should end in `Error` and it should inherit from
`RainfallError`.

New public functions also need adding to `rainfall/__init__.py` and its
`__all__`.

## Tests

Tests live in `tests/`, with one test module for each source module, so
`src/rainfall/stats.py` is tested in `tests/test_stats.py`. We name tests
`test_<function>_<behaviour>`, for example `test_total_rain_includes_end_date`,
so a failure tells you what broke without opening the file. Shared fixtures
are in `tests/conftest.py`; `march_records` is a good starting point for small
examples.

New functions need tests. If you're fixing a bug, please add a test that fails
without your fix, so we know the fix works and the bug can't quietly come
back.

Please don't change an existing test just to make it pass. If you think a test
is wrong, fix it in a separate commit and explain why in the commit message,
so the change gets its own review.

## Data

Files in `data/raw/` are input data and should never be edited, renamed or
overwritten. If you produce derived data, write it to `data/processed/`, which
git ignores. If you add a raw data file, please record its source and licence
in `data/README.md`.

## Commit messages and the changelog

We use [Conventional Commits](https://www.conventionalcommits.org/), so each
commit message starts with a type: `feat:`, `fix:`, `docs:`, `test:`,
`refactor:`, `build:`, `ci:` or `chore:`. The summary that follows should be
in the imperative mood and under 72 characters, for example
`fix: include the end date in total_rain`. Please keep each commit to one
logical change.

If your change is something a user would notice, add a line to the
`Unreleased` section of `CHANGELOG.md` under Added, Changed or Fixed.

## Releases

Releases are made by the maintainers and follow
[Semantic Versioning](https://semver.org/). For each release we update the
version in `pyproject.toml` and `src/rainfall/__init__.py`, move the
`Unreleased` entries in `CHANGELOG.md` under the new version, update
`CITATION.cff`, and tag the commit `vX.Y.Z`.

## Code of conduct

Everyone taking part in this project is expected to follow our
[code of conduct](CODE_OF_CONDUCT.md).

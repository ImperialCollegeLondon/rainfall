# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-09-11

### Added

- `validate_records` decorator, applied to every public function that takes records.
- `EmptyRecordsError`.
- `moving_average` for daily rainfall values.

### Changed

- `wettest_day` and `total_rain` now raise `EmptyRecordsError` for empty input and `InvalidRecordError` for malformed or unsorted records.

## [0.1.0] - 2026-08-28

### Added

- `Record` type alias and `RainfallError` exception hierarchy.
- `load_records` to read records from a CSV file with `date` and `rain_mm` columns.
- `mean` and `wettest_day`.
- `total_rain` for the total rainfall between two dates.

[Unreleased]: ../../compare/v0.2.0...HEAD
[0.2.0]: ../../compare/v0.1.0...v0.2.0
[0.1.0]: ../../releases/tag/v0.1.0

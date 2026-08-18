"""Exceptions raised by the package."""


class RainfallError(Exception):
    """Base class for all errors raised by this package."""


class InvalidRecordError(RainfallError):
    """Raised when a record or input file is malformed."""

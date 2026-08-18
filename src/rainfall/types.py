"""Types shared across the package."""

from typing import TypeAlias

Record: TypeAlias = tuple[str, float]
"""A daily rainfall record: an ISO 8601 date and the rainfall in millimetres."""

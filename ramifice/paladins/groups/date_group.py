"""Group for checking date fields.
Supported fields:
DateTimeField | DateField
"""

from typing import Any


class DateGroupMixin:
    """Group for checking date fields.
    Supported fields:
    DateTimeField | DateField
    """

    def date_group(self, params: dict[str, Any]) -> None:
        """Checking date fields."""

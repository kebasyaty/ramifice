"""Group for checking boolean fields.
Supported fields: BooleanField
"""

from typing import Any


class BoolGroupMixin:
    """Group for checking boolean fields.
    Supported fields: BooleanField
    """

    def bool_group(self, params: dict[str, Any]) -> None:
        """Checking boolean fields."""

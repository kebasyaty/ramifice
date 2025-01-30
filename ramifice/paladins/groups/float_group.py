"""Group for checking float fields.
Supported fields: FloatField
"""

from typing import Any


class FloatGroupMixin:
    """Group for checking float fields.
    Supported fields: FloatField
    """

    def float_group(self, params: dict[str, Any]) -> None:
        """Checking float fields."""

"""Group for checking integer fields.
Supported fields: IntegerField
"""

from typing import Any


class IntGroupMixin:
    """Group for checking integer fields.
    Supported fields: IntegerField
    """

    def int_group(self, params: dict[str, Any]) -> None:
        """Checking integer fields."""

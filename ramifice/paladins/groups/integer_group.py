"""Group for checking integer fields.
Supported fields: IntegerField
"""

from typing import Any


class IntegerGroupMixin:
    """Group for checking integer fields.
    Supported fields: IntegerField
    """

    def integer_group(self, params: dict[str, Any]) -> None:
        """Checking integer fields."""

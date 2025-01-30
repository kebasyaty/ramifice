"""Group for checking hash fields.
Supported fields: HashField
"""

from typing import Any


class HashGroupMixin:
    """Group for checking hash fields.
    Supported fields: HashField
    """

    def hash_group(self, params: dict[str, Any]) -> None:
        """Checking hash fields."""

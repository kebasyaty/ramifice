"""Group for checking slug fields.
Supported fields: SlugField
"""

from typing import Any


class SlugGroupMixin:
    """Group for checking slug fields.
    Supported fields: SlugField
    """

    def slug_group(self, params: dict[str, Any]) -> None:
        """Checking slug fields."""

"""Group for checking image fields.
Supported fields: ImageField
"""

from typing import Any


class ImageGroupMixin:
    """Group for checking image fields.
    Supported fields: ImageField
    """

    def image_group(self, params: dict[str, Any]) -> None:
        """Checking image fields."""

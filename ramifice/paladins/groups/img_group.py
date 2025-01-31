"""Group for checking image fields.
Supported fields: ImageField
"""

from typing import Any


class ImgGroupMixin:
    """Group for checking image fields.
    Supported fields: ImageField
    """

    def img_group(self, params: dict[str, Any]) -> None:
        """Checking image fields."""

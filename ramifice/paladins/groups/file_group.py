"""Group for checking file fields.
Supported fields: FileField
"""

from typing import Any


class FileGroupMixin:
    """Group for checking file fields.
    Supported fields: FileField
    """

    def file_group(self, params: dict[str, Any]) -> None:
        """Checking file fields."""

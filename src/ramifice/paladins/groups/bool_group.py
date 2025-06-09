"""Group for checking boolean fields.

Supported fields:
    BooleanField
"""

from typing import Any


class BoolGroupMixin:
    """Group for checking boolean fields.

    Supported fields:
        BooleanField
    """

    def bool_group(self, params: dict[str, Any]) -> None:
        """Checking boolean fields."""
        field = params["field_data"]
        # Get current value.
        value = field.value
        if not params["is_update"] and value is None:
            value = field.default
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = bool(value)

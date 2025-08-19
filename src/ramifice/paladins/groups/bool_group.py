"""Group for checking boolean fields.

Supported fields:
    BooleanField
"""

from __future__ import annotations

__all__ = ("BoolGroupMixin",)

from typing import Any

from ramifice.paladins.tools import panic_type_error


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

        if not isinstance(value, (bool, type(None))):
            panic_type_error("bool | None", params)

        if not params["is_update"] and value is None:
            value = field.default
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = bool(value)

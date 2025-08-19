"""Group for checking id fields.

Supported fields:
    IDField
"""

from __future__ import annotations

__all__ = ("IDGroupMixin",)

from typing import Any

from bson.objectid import ObjectId

from ramifice.paladins.tools import accumulate_error, panic_type_error
from ramifice.utils import translations


class IDGroupMixin:
    """Group for checking id fields.

    Supported fields:
        IDField
    """

    def id_group(self, params: dict[str, Any]) -> None:
        """Checking id fields."""
        field = params["field_data"]
        # Get current value.
        value = field.value

        if not isinstance(value, (ObjectId, type(None))):
            panic_type_error("ObjectId | None", params)

        if value is None:
            if field.required:
                err_msg = translations._("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation of the MongoDB identifier in a string form.
        if not ObjectId.is_valid(value):
            err_msg = translations._("Invalid document ID !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value

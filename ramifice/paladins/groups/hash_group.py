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
        field = params["field_data"]
        # Get current value.
        value = field.value or None
        if value is None:
            if field.required:
                err_msg = "Required field !"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation of the Mongodb identifier in a string form.
        if not field.is_valid(value):
            err_msg = "Required field !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value

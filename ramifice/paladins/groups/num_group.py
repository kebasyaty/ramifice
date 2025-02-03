"""Group for checking integer fields.
Supported fields:
IntegerField | FloatField
"""

from typing import Any


class NumGroupMixin:
    """Group for checking integer fields.
    Supported fields:
    IntegerField | FloatField
    """

    async def num_group(self, params: dict[str, Any]) -> None:
        """Checking number fields."""
        field = params["field_data"]
        # Get current value.
        value = field.value
        if value is None:
            value = field.default
        if value is None:
            if field.required:
                err_msg = "Required field !"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation the `max_number` field attribute.
        max_number = field.__dict__["max_number"]
        if max_number is not None and value > max_number:
            err_msg = f"The value {value} must not be greater than max={max_number} !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation the `min_number` field attribute.
        min_number = field.__dict__["min_number"]
        if min_number is not None and value < min_number:
            err_msg = f"The value {value} must not be less than min={min_number} !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation the `unique` field attribute.
        if field.unique and not await self.check_uniqueness(value, params):  # type: ignore[attr-defined]
            err_msg = "Is not unique !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value

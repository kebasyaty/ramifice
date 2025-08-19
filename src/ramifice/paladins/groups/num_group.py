"""Group for checking integer fields.

Supported fields:
    IntegerField | FloatField
"""

from __future__ import annotations

__all__ = ("NumGroupMixin",)

from typing import Any

from ramifice.paladins.tools import (
    accumulate_error,
    check_uniqueness,
    panic_type_error,
)
from ramifice.utils import translations


class NumGroupMixin:
    """Group for checking integer fields.

    Supported fields:
        IntegerField | FloatField
    """

    async def num_group(self, params: dict[str, Any]) -> None:
        """Checking number fields."""
        field = params["field_data"]
        field_name = field.name
        # Get current value.
        value = field.value
        if value is None:
            value = field.default

        if "Float" in field.field_type:
            if not isinstance(value, (float, type(None))):
                panic_type_error("float | None", params)
        else:
            if not isinstance(value, (int, type(None))):
                panic_type_error("int | None", params)

        if value is None:
            if field.required:
                err_msg = translations._("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field_name] = None
            return
        # Validation the `max_number` field attribute.
        max_number = field.max_number
        if max_number is not None and value > max_number:
            err_msg = translations._(
                "The value {} must not be greater than max={} !",
            ).format(value, max_number)
            accumulate_error(err_msg, params)
        # Validation the `min_number` field attribute.
        min_number = field.min_number
        if min_number is not None and value < min_number:
            err_msg = translations._(
                "The value {} must not be less than min={} !",
            ).format(value, min_number)
            accumulate_error(err_msg, params)
        # Validation the `unique` field attribute.
        if field.unique and not await check_uniqueness(value, params, field_name):
            err_msg = translations._("Is not unique !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            params["result_map"][field_name] = value

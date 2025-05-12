"""Group for checking date fields.
Supported fields:
DateTimeField | DateField
"""

from typing import Any


class DateGroupMixin:
    """Group for checking date fields.
    Supported fields:
    DateTimeField | DateField
    """

    def date_group(self, params: dict[str, Any]) -> None:
        """Checking date fields."""
        field = params["field_data"]
        # Get current value.
        value = field.value or field.default or None
        if value is None:
            if field.required:
                err_msg = "Required field !"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        #
        # Validation the `max_date` field attribute.
        max_date = field.max_date
        if max_date is not None and value > max_date:
            date_str = (
                str(max_date)[:11]
                if field.field_type == "DateField"
                else str(max_date)[:20]
            )
            err_msg = f"The date {value} must not be greater than max={date_str} !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation the `min_date` field attribute.
        min_date = field.min_date
        if min_date is not None and value < min_date:
            date_str = (
                str(max_date)[:11]
                if field.field_type == "DateField"
                else str(max_date)[:20]
            )
            err_msg = f"The date {value} must not be less than min={date_str} !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value

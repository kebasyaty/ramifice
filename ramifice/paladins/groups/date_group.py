"""Group for checking date fields.
Supported fields:
DateTimeField | DateField
"""

from typing import Any

from ...errors import InvalidDateError, InvalidDateTimeError
from ...tools import date_parse, datetime_parse


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
        if "DateTime" in field.field_type:
            try:
                value = datetime_parse(value)
            except InvalidDateTimeError:
                err_msg = "Invalid date and time !"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        else:
            try:
                value = date_parse(value)
            except InvalidDateError:
                err_msg = "Invalid date !"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        #
        time_object_list = self.__class__.META["time_object_list"]  # type: ignore[attr-defined]
        # Validation the `max_date` field attribute.
        max_date = field.__dict__["max_date"]
        if max_date is not None and value > max_date:
            err_msg = f"The date {value} must not be greater than max={max_date} !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation the `min_date` field attribute.
        min_date = field.__dict__["min_date"]
        if min_date is not None and value < min_date:
            err_msg = f"The date {value} must not be less than min={min_date} !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]

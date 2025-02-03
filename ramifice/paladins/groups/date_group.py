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
        time_object_list = self.__class__.META["time_object_list"]  # type: ignore[attr-defined]
        # Get current value.
        value = field.value or field.default or None
        if value is None:
            if field.required:
                err_msg = "Required field !"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"][field.name] = None
            return

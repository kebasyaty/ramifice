"""Group for checking text fields.
Supported fields:
URLField | TextField | PhoneField
| IPField | EmailField | ColorField
"""

from typing import Any


class TextGroupMixin:
    """Group for checking text fields.
    Supported fields:
    URLField | TextField | PhoneField
    | IPField | EmailField | ColorField
    """

    def text_group(self, params: dict[str, Any]) -> None:
        """Checking text fields."""
        field = params["field_data"]
        # Get current value.
        value = field.value or field.default
        if value is None:
            if field.required:
                self.accumulate_error("Required field!", params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"] = None
            return

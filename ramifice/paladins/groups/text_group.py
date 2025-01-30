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
                err_msg = "Required field !"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"] = None
            return
        # Validation the `maxlength` field attribute.
        maxlength = field.__dict__.get("maxlength")
        if maxlength is not None:
            if len(value) > maxlength:
                err_msg = f"The number {len(value)} must not be greater than max={maxlength} !"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation the `minlength` field attribute.
        minlength = field.__dict__.get("minlength")
        if minlength is not None:
            if len(value) < minlength:
                err_msg = (
                    f"The number {len(value)} must not be less than min={minlength} !"
                )
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]

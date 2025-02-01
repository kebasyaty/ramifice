"""Group for checking text fields.
Supported fields:
URLField | TextField | PhoneField
| IPField | EmailField | ColorField
"""

from typing import Any

from email_validator import EmailNotValidError, validate_email


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
        if maxlength is not None and len(value) > maxlength:
            err_msg = (
                f"The number {len(value)} must not be greater than max={maxlength} !"
            )
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation the `minlength` field attribute.
        minlength = field.__dict__.get("minlength")
        if minlength is not None and len(value) < minlength:
            err_msg = f"The number {len(value)} must not be less than min={minlength} !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation the `unique` field attribute.
        if field.unique and not self.check_uniqueness(value, params):  # type: ignore[attr-defined]
            err_msg = "Is not unique !"
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation Email, Url, IP, Color, Phone.
        field_type = field.field_type
        if "Email" in field_type:
            try:
                emailinfo = validate_email(value, check_deliverability=True)
                value = emailinfo.normalized
            except EmailNotValidError:
                err_msg = "Invalid Email address!"
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        elif "URL" in field_type:
            pass
        elif "IP" in field_type:
            pass
        elif "Color" in field_type:
            pass
        elif "Phone" in field_type:
            pass
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value

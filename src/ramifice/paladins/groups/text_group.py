"""Group for checking text fields.

Supported fields:
    URLField | TextField | PhoneField
    IPField | EmailField | ColorField
"""

from typing import Any

from email_validator import EmailNotValidError, validate_email

from ... import translations
from ...utilities import is_color, is_ip, is_phone, is_url
from ..tools import accumulate_error, check_uniqueness, panic_type_error


class TextGroupMixin:
    """Group for checking text fields.

    Supported fields:
        URLField | TextField | PhoneField
        IPField | EmailField | ColorField
    """

    async def text_group(self, params: dict[str, Any]) -> None:
        """Checking text fields."""
        field = params["field_data"]
        # Get current value.
        value = field.value or field.default or None

        if not isinstance(value, (str, type(None))):
            panic_type_error("str | None", params)

        if value is None:
            if field.required:
                err_msg = translations._("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation the `maxlength` field attribute.
        maxlength: int | None = field.__dict__.get("maxlength")
        if maxlength is not None and len(value) > maxlength:
            err_msg = translations._("The length of the string exceeds maxlength=%d !" % maxlength)
            accumulate_error(err_msg, params)
        # Validation the `unique` field attribute.
        if field.unique and not await check_uniqueness(value, params):
            err_msg = translations._("Is not unique !")
            accumulate_error(err_msg, params)
        # Validation Email, Url, IP, Color, Phone.
        field_type = field.field_type
        if "Email" in field_type:
            try:
                emailinfo = validate_email(
                    str(value),
                    check_deliverability=self.__class__.META["is_migrate_model"],  # type: ignore[attr-defined]
                )
                value = emailinfo.normalized
                params["field_data"].value = value
            except EmailNotValidError:
                err_msg = translations._("Invalid Email address !")
                accumulate_error(err_msg, params)
        elif "URL" in field_type and not is_url(value):
            err_msg = translations._("Invalid URL address !")
            accumulate_error(err_msg, params)
        elif "IP" in field_type and not is_ip(value):
            err_msg = translations._("Invalid IP address !")
            accumulate_error(err_msg, params)
        elif "Color" in field_type and not is_color(value):
            err_msg = translations._("Invalid Color code !")
            accumulate_error(err_msg, params)
        elif "Phone" in field_type and not is_phone(value):
            err_msg = translations._("Invalid Phone number !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value

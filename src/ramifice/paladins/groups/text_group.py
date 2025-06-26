"""Group for checking text fields.

Supported fields:
    URLField | TextField | PhoneField
    IPField | EmailField | ColorField
"""

from typing import Any

from email_validator import EmailNotValidError, validate_email

from ...utils import translations
from ...utils.tools import is_color, is_ip, is_phone, is_url
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
        field_name = field.name
        field_type: str = field.field_type
        is_text_field: bool = "TextField" == field_type
        # Get current value.
        value = field.value or field.__dict__.get("default")

        if is_text_field:
            if not isinstance(value, (str, dict, type(None))):
                panic_type_error("str | dict | None", params)
        else:
            if not isinstance(value, (str, type(None))):
                panic_type_error("str | None", params)

        if value is None:
            if field.required:
                err_msg = translations._("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field_name] = None
            return
        # Validation the `maxlength` field attribute.
        maxlength: int | None = field.__dict__.get("maxlength")
        if maxlength is not None and len(field) > maxlength:
            err_msg = translations._("The length of the string exceeds maxlength=%d !" % maxlength)
            accumulate_error(err_msg, params)
        # Validation the `unique` field attribute.
        if field.unique and not await check_uniqueness(
            value,
            params,
            field_name,
            is_text_field,
        ):
            err_msg = translations._("Is not unique !")
            accumulate_error(err_msg, params)
        # Validation Email, Url, IP, Color, Phone.
        if "EmailField" == field_type:
            try:
                emailinfo = validate_email(
                    str(value),
                    check_deliverability=self.__class__.META["is_migrate_model"],
                )
                value = emailinfo.normalized
                params["field_data"].value = value
            except EmailNotValidError:
                err_msg = translations._("Invalid Email address !")
                accumulate_error(err_msg, params)
        elif "URLField" == field_type and not is_url(value):
            err_msg = translations._("Invalid URL address !")
            accumulate_error(err_msg, params)
        elif "IPField" == field_type and not is_ip(value):
            err_msg = translations._("Invalid IP address !")
            accumulate_error(err_msg, params)
        elif "ColorField" == field_type and not is_color(value):
            err_msg = translations._("Invalid Color code !")
            accumulate_error(err_msg, params)
        elif "PhoneField" == field_type and not is_phone(value):
            err_msg = translations._("Invalid Phone number !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            if is_text_field:
                mult_lang_text: dict[str, str] = (
                    params["curr_doc"][field_name] if params["is_update"] else {}
                )
                if isinstance(value, dict):
                    for lang, text in value.items():
                        mult_lang_text[lang] = text
                else:
                    mult_lang_text[translations.CURRENT_LOCALE] = value
                value = mult_lang_text
            params["result_map"][field_name] = value

"""Group for checking text fields.

Supported fields:
    URLField | TextField | PhoneField
    IPField | EmailField | ColorField
"""

from __future__ import annotations

__all__ = ("TextGroupMixin",)

import asyncio
from typing import Any

from email_validator import (
    EmailNotValidError,
    validate_email,
)

from ramifice.paladins.tools import (
    accumulate_error,
    check_uniqueness,
    panic_type_error,
)
from ramifice.utils import translations
from ramifice.utils.tools import (
    is_color,
    is_ip,
    is_phone,
    is_url,
)


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
        is_multi_language: bool = (field_type == "TextField") and field.multi_language
        # Get current value.
        value = field.value or field.__dict__.get("default")

        if is_multi_language:
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
            err_msg = translations._(
                "The length of the string exceeds maxlength={} !",
            ).format(maxlength)
            accumulate_error(err_msg, params)
        # Validation the `unique` field attribute.
        if field.unique and not await check_uniqueness(
            value,
            params,
            field_name,
            is_multi_language,
        ):
            err_msg = translations._("Is not unique !")
            accumulate_error(err_msg, params)
        # Validation Email, Url, IP, Color, Phone.
        if field_type == "EmailField":
            try:
                emailinfo = await asyncio.to_thread(
                    validate_email,
                    str(value),
                    check_deliverability=True,
                )
                value = emailinfo.normalized
                params["field_data"].value = value
            except EmailNotValidError:
                err_msg = translations._("Invalid Email address !")
                accumulate_error(err_msg, params)
        elif field_type == "URLField" and not is_url(value):
            err_msg = translations._("Invalid URL address !")
            accumulate_error(err_msg, params)
        elif field_type == "IPField" and not is_ip(value):
            err_msg = translations._("Invalid IP address !")
            accumulate_error(err_msg, params)
        elif field_type == "ColorField" and not is_color(value):
            err_msg = translations._("Invalid Color code !")
            accumulate_error(err_msg, params)
        elif field_type == "PhoneField" and not is_phone(value):
            err_msg = translations._("Invalid Phone number !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            if is_multi_language:
                mult_lang_text = (
                    params["curr_doc"][field_name]
                    if params["is_update"]
                    else (
                        dict.fromkeys(translations.LANGUAGES)
                        if isinstance(value, str)
                        else {lang: value.get(lang, "- -") for lang in translations.LANGUAGES}
                    )
                )
                if isinstance(value, dict):
                    for lang in translations.LANGUAGES:
                        mult_lang_text[lang] = value.get(lang, "- -")
                else:
                    mult_lang_text[translations.CURRENT_LOCALE] = value
                value = mult_lang_text
            params["result_map"][field_name] = value

"""Group for checking text fields.
Supported fields:
URLField | TextField | PhoneField
| IPField | EmailField | ColorField
"""

from typing import Any

from email_validator import EmailNotValidError, validate_email

from ... import translations


class TextGroupMixin:
    """Group for checking text fields.
    Supported fields:
    URLField | TextField | PhoneField
    | IPField | EmailField | ColorField
    """

    async def text_group(self, params: dict[str, Any]) -> None:
        """Checking text fields."""
        field = params["field_data"]
        gettext = translations.gettext
        # Get current value.
        value = field.value or field.default or None
        if value is None:
            if field.required:
                err_msg = gettext("Required field !")
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
            if params["is_save"]:
                params["result_map"][field.name] = None
            return
        # Validation the `maxlength` field attribute.
        maxlength = field.__dict__.get("maxlength")
        if maxlength is not None and len(value) > maxlength:
            err_msg = gettext(
                "The length of the string exceeds maxlength={maxlength} !"
            ).format(maxlength=maxlength)
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation the `unique` field attribute.
        if field.unique and not await self.check_uniqueness(value, params):  # type: ignore[attr-defined]
            err_msg = gettext("Is not unique !")
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Validation Email, Url, IP, Color, Phone.
        field_type = field.field_type
        if "Email" in field_type:
            try:
                emailinfo = validate_email(
                    str(value),
                    check_deliverability=self.__class__.META["is_migrat_model"],  # type: ignore[attr-defined]
                )
                value = emailinfo.normalized
                params["field_data"].value = value
            except EmailNotValidError:
                err_msg = gettext("Invalid Email address !")
                self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        elif "URL" in field_type and not field.is_valid(value):
            err_msg = gettext("Invalid URL address !")
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        elif "IP" in field_type and not field.is_valid(value):
            err_msg = gettext("Invalid IP address !")
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        elif "Color" in field_type and not field.is_valid(value):
            err_msg = gettext("Invalid Color code !")
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        elif "Phone" in field_type and not field.is_valid(value):
            err_msg = gettext("Invalid Phone number !")
            self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
        # Insert result.
        if params["is_save"]:
            params["result_map"][field.name] = value

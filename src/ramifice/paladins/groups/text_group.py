"""Group for checking text fields.

Supported fields:
    URLField | TextField | PhoneField
    IPField | EmailField | ColorField
"""

from typing import Any

from email_validator import EmailNotValidError, validate_email

from ... import translations


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
		if value is None:
			if field.required:
				err_msg = translations._("Required field !")
				self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
			if params["is_save"]:
				params["result_map"][field.name] = None
			return
		# Validation the `maxlength` field attribute.
		maxlength: int | None = field.__dict__.get("maxlength")
		if maxlength is not None and len(value) > maxlength:
			err_msg = translations._("The length of the string exceeds maxlength=%d !" % maxlength)
			self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
		# Validation the `unique` field attribute.
		if field.unique and not await self.check_uniqueness(value, params):  # type: ignore[attr-defined]
			err_msg = translations._("Is not unique !")
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
				err_msg = translations._("Invalid Email address !")
				self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
		elif "URL" in field_type and not field.is_valid(value):
			err_msg = translations._("Invalid URL address !")
			self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
		elif "IP" in field_type and not field.is_valid(value):
			err_msg = translations._("Invalid IP address !")
			self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
		elif "Color" in field_type and not field.is_valid(value):
			err_msg = translations._("Invalid Color code !")
			self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
		elif "Phone" in field_type and not field.is_valid(value):
			err_msg = translations._("Invalid Phone number !")
			self.accumulate_error(err_msg, params)  # type: ignore[attr-defined]
		# Insert result.
		if params["is_save"]:
			params["result_map"][field.name] = value

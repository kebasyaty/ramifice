"""Field of Model for enter phone number."""

import json

import phonenumbers

from ..store import DEBUG
from .general.field import Field
from .general.text_group import TextGroup


class PhoneField(Field, TextGroup):
    """Field of Model for enter phone number.
    WARNING: By default is used validator `phonenumbers.is_valid_number()`.
    """

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: str | None = None,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="PhoneField",
            group="text",
        )
        TextGroup.__init__(
            self,
            input_type="tel",
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=unique,
        )
        if DEBUG:
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
                try:
                    phone_default = phonenumbers.parse(default)
                    if not phonenumbers.is_valid_number(phone_default):
                        raise AssertionError()
                except:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        "Parameter `default` - Invalid Phone number!"
                    )  # pylint: disable=raise-missing-from

        self.__default = default

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

    # --------------------------------------------------------------------------
    def to_dict(self) -> dict[str, str | bool | list[str] | None]:
        """Convert the field object to a dictionary."""
        json_dict: dict[str, str | bool | list[str] | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                json_dict[f_name] = f_type
        return json_dict

    def to_json(self):
        """Convert field object to a json string."""
        return json.dumps(self.to_dict())

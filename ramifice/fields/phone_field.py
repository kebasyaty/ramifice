"""Field of Model for enter phone number."""

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
        regex: str = "",
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
        self.__regex = regex

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

    @property
    def regex(self) -> str:
        """Regular expression to validate the `value`.
        Example: "^.+$"
        """
        return self.__regex

"""Field of Model for enter email address."""

import json

from email_validator import EmailNotValidError, validate_email

from ..store import DEBUG
from .general.field import Field
from .general.text_group import TextGroup


class EmailField(Field, TextGroup):
    """Field of Model for enter email address."""

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
            field_type="EmailField",
            group="text",
        )
        TextGroup.__init__(
            self,
            input_type="email",
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
                    validate_email(default, check_deliverability=True)
                except EmailNotValidError:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        "Parameter `default` - Invalid Email address!"
                    )  # pylint: disable=raise-missing-from

        self.__default = default

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

    def to_dict(self) -> dict[str, str | bool | list[str] | None]:
        """Convert fields to a dictionary."""
        json_dict: dict[str, str | bool | list[str] | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                json_dict[f_name] = f_type
        return json_dict

    def to_json(self):
        """Convert a dictionary of fields to a JSON string."""
        return json.dumps(self.to_dict())

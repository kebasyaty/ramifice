"""Field of Model for enter logical value."""

import json

from ..store import DEBUG
from .general.field import Field


class BoolField(Field):
    """Field of Model for enter logical value."""

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: bool | None = False,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="BoolField",
            group="bool",
        )
        if DEBUG:
            if default is not None and not isinstance(default, bool):
                raise AssertionError("Parameter `default` - Not а `bool` type!")

        self.__input_type = "checkbox"
        self.__value: bool | None = None
        self.__default = default

    @property
    def input_type(self) -> str:
        """Input type for a web form field.
        Html tag: input type="checkbox".
        """
        return self.__input_type

    # --------------------------------------------------------------------------
    @property
    def value(self) -> bool | None:
        """Sets value of field."""
        return self.__value

    @value.setter
    def value(self, value: bool | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def default(self) -> bool | None:
        """Default file path.
        Example: 'public/media/default/nodoc.docx'
        """
        return self.__default

    # --------------------------------------------------------------------------
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

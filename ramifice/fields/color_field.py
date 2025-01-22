"""Field of Model for enter color code."""

import json

from ..store import DEBUG, REGEX
from .general.field import Field
from .general.text_group import TextGroup


class ColorField(Field, TextGroup):
    """Field of Model for enter color code.
    Default value is #000000 (black).
    Examples: #fff | #f2f2f2 | #f2f2f200 | rgb(255,0,24) |
              rgba(255,0,24,0.5) | rgba(#fff,0.5) | hsl(120,100%,50%) |
              hsla(170,23%,25%,0.2) | 0x00ffff
    """

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: str | None = "#000000",
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
            field_type="ColorField",
            group="text",
        )
        TextGroup.__init__(
            self,
            input_type="text",
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
                if REGEX["color_code"].match(default) is None:
                    raise AssertionError("Parameter `default` - Not а color code!")

        self.__default = default

    @property
    def default(self) -> str | None:
        """Value by default.
        Default value is #000000 (black).
        """
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

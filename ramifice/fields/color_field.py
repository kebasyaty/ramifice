"""Field of Model for enter color code."""

from ..mixins import JsonMixin
from ..store import DEBUG, REGEX
from .general.field import Field
from .general.text_group import TextGroup


class ColorField(Field, TextGroup, JsonMixin):
    """Field of Model for enter color code.
    Default value is #000000 (black).
    Examples: #fff | #f2f2f2 | #f2f2f200 | rgb(255,0,24) |
              rgba(255,0,24,0.5) | rgba(#fff,0.5) | hsl(120,100%,50%) |
              hsla(170,23%,25%,0.2) | 0x00ffff
    """

    def __init__(  # pylint: disable=too-many-arguments
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
        JsonMixin.__init__(self)

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

        self.default = default

    def __str__(self):
        return str(self.value)

    def is_valid(self, value: str | None = None) -> bool:
        """Validate Color code."""
        flag = True
        value = str(value or self.value or self.default)
        if REGEX["color_code"].match(value) is None:
            flag = False
        return flag

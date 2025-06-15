"""Field of Model for enter color code."""

from .. import store
from ..mixins import JsonMixin
from .general.field import Field
from .general.text_group import TextGroup


class ColorField(Field, TextGroup, JsonMixin):
    """Field of Model for enter color code.

    Default value is #000000 (black).

    Examples:
            #fff | #f2f2f2 | #f2f2f200 | rgb(255,0,24) |
        rgba(255,0,24,0.5) | rgba(#fff,0.5) | hsl(120,100%,50%) |
        hsla(170,23%,25%,0.2) | 0x00ffff
    """

    def __init__(  # noqa: D107
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
        if store.DEBUG:
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
                if store.REGEX["color_code"].match(default) is None:
                    raise AssertionError("Parameter `default` - Not а color code!")
            if not isinstance(label, str):
                raise AssertionError("Parameter `default` - Not а `str` type!")
            if not isinstance(disabled, bool):
                raise AssertionError("Parameter `disabled` - Not а `bool` type!")
            if not isinstance(hide, bool):
                raise AssertionError("Parameter `hide` - Not а `bool` type!")
            if not isinstance(ignored, bool):
                raise AssertionError("Parameter `ignored` - Not а `bool` type!")
            if not isinstance(ignored, bool):
                raise AssertionError("Parameter `ignored` - Not а `bool` type!")
            if not isinstance(hint, str):
                raise AssertionError("Parameter `hint` - Not а `str` type!")
            if warning is not None and not isinstance(warning, list):
                raise AssertionError("Parameter `warning` - Not а `list` type!")
            if not isinstance(placeholder, str):
                raise AssertionError("Parameter `placeholder` - Not а `str` type!")
            if not isinstance(required, bool):
                raise AssertionError("Parameter `required` - Not а `bool` type!")
            if not isinstance(readonly, bool):
                raise AssertionError("Parameter `readonly` - Not а `bool` type!")
            if not isinstance(unique, bool):
                raise AssertionError("Parameter `unique` - Not а `bool` type!")

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

        self.default = default

    def is_valid(self, value: str | None = None) -> bool:
        """Validate Color code."""
        color_code = str(value or self.value or self.default)
        if store.REGEX["color_code"].match(color_code) is None:
            return False
        return True

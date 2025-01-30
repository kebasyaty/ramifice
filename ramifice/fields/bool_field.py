"""Field of Model for enter boolean value."""

from ..mixins import JsonMixin
from ..store import DEBUG
from .general.field import Field


class BooleanField(Field, JsonMixin):
    """Field of Model for enter boolean value."""

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
            field_type="BooleanField",
            group="bool",
        )
        JsonMixin.__init__(self)

        if DEBUG:
            if default is not None and not isinstance(default, bool):
                raise AssertionError("Parameter `default` - Not а `bool` type!")

        self.input_type = "checkbox"
        self.value: bool | None = None
        self.default = default

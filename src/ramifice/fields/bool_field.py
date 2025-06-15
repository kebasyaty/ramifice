"""Field of Model for enter boolean value."""

from .. import store
from ..mixins import JsonMixin
from .general.field import Field


class BooleanField(Field, JsonMixin):
    """Field of Model for enter boolean value."""

    def __init__(  # noqa: D107
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: bool = False,
    ):
        if store.DEBUG:
            if default is not None and not isinstance(default, bool):
                raise AssertionError("Parameter `default` - Not а `bool` type!")
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

        self.input_type = "checkbox"
        self.value: bool | None = None
        self.default = default

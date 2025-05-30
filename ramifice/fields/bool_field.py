"""Field of Model for enter boolean value."""

from .. import translations
from ..mixins import JsonMixin
from ..store import DEBUG
from .general.field import Field


class BooleanField(Field, JsonMixin):
    """Field of Model for enter boolean value."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: bool = False,
    ):
        if DEBUG:
            if default is not None and not isinstance(default, bool):
                raise AssertionError("Parameter `default` - Not а `bool` type!")

        if len(label) > 0:
            label = translations.gettext(label)
        if len(hint) > 0:
            hint = translations.gettext(hint)
        if bool(warning):
            warning = [translations.gettext(item) for item in warning]

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

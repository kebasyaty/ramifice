"""A field for entering a text string."""

from . import field


class TextField(field.Field):
    """A field for entering a text string."""

    def __init__(
        self,
            label: str = "",
            disabled: bool = False,
            hide: bool = False,
            ignored: bool = False,
            hint: str = "",
            warning: list[str] | None = None,
            errors: list[str] | None = None,
    ):
        super().__init__(
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            errors=errors,
            field_type=type(self).__name__,
            group=1,
        )

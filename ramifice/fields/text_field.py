"""Field of Model for enter text."""

from ..mixins import JsonMixin
from ..store import DEBUG
from .general.field import Field
from .general.text_group import TextGroup


class TextField(Field, TextGroup, JsonMixin):
    """Field of Model for enter text."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        textarea: bool = False,
        use_editor: bool = False,
        default: str | None = None,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        maxlength: int = 256,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="TextField",
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
            if not isinstance(maxlength, int):
                raise AssertionError("Parameter `maxlength` - Not а `int` type!")
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
                if len(default) > maxlength:
                    raise AssertionError(
                        "Parameter `default` exceeds the size of `maxlength`!"
                    )

        self.default = default
        self.textarea = textarea
        self.use_editor = use_editor
        self.maxlength = maxlength

    def __str__(self):
        return str(self.value)

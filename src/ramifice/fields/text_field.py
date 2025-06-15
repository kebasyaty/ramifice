"""Field of Model for enter text."""

from .. import store
from ..mixins import JsonMixin
from .general.field import Field
from .general.text_group import TextGroup


class TextField(Field, TextGroup, JsonMixin):
    """Field of Model for enter text."""

    def __init__(  # noqa: D107
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
        if store.DEBUG:
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
                    raise AssertionError("Parameter `default` exceeds the size of `maxlength`!")
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
            if not isinstance(textarea, bool):
                raise AssertionError("Parameter `textarea` - Not а `bool` type!")
            if not isinstance(use_editor, bool):
                raise AssertionError("Parameter `use_editor` - Not а `bool` type!")
            if not isinstance(maxlength, int):
                raise AssertionError("Parameter `maxlength` - Not а `int` type!")

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

        self.default = default
        self.textarea = textarea
        self.use_editor = use_editor
        self.maxlength = maxlength

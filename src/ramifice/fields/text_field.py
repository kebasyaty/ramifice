"""Field of Model for enter text."""

from __future__ import annotations

__all__ = ("TextField",)

import logging

from ramifice.fields.general.field import Field
from ramifice.utils import constants
from ramifice.utils.mixins import JsonMixin

logger = logging.getLogger(__name__)


class TextField(Field, JsonMixin):
    """Field of Model for enter text.

    Agrs:
        label: Text label for a web form field.
        placeholder: Displays prompt text.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        textarea: Is it necessary to use the Textarea widget.
        use_editor: Is it necessary to use the widget of the text editor.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        unique: The unique value of a field in a collection.
        maxlength: The maximum line length.
        multi_language: Is it need support for several languages.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        placeholder: str = "",
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        textarea: bool = False,
        use_editor: bool = False,
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        maxlength: int = 256,
        # Support for several language.
        multi_language: bool = False,
    ) -> None:
        if constants.DEBUG:
            try:
                if not isinstance(maxlength, int):
                    raise AssertionError("Parameter `maxlength` - Not а `int` type!")
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
                if not isinstance(multi_language, bool):
                    raise AssertionError("Parameter `multi_language` - Not а `int` type!")
            except AssertionError as err:
                logger.critical(str(err))
                raise err

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
        JsonMixin.__init__(self)

        self.value: str | dict[str, str] | None = None
        self.input_type = "text"
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique
        self.textarea = textarea
        self.use_editor = use_editor
        self.maxlength = maxlength
        # Support for several language.
        self.multi_language = multi_language

    def __len__(self) -> int:
        """Return length of field `value`."""
        value = self.value
        if isinstance(value, str):
            return len(value)
        if isinstance(value, dict):
            count = 0
            for text in value.values():
                tmp = len(text)
                if tmp > count:
                    count = tmp
            return count
        return 0

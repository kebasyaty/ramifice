"""Field of Model for enter text."""

import json

from ..store import DEBUG
from .general.field import Field
from .general.text_group import TextGroup


class TextField(Field, TextGroup):
    """Field of Model for enter text."""

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

        self.__default = default
        self.__textarea = textarea
        self.__use_editor = use_editor
        self.__maxlength = maxlength

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

    # --------------------------------------------------------------------------
    @property
    def textarea(self) -> bool:
        """Use HTML tag Textarea?"""
        return self.__textarea

    # --------------------------------------------------------------------------
    @property
    def use_editor(self) -> bool:
        """Whether or not to use your preferred text editor -
        CKEditor, TinyMCE, etc."""
        return self.__use_editor

    # --------------------------------------------------------------------------
    @property
    def maxlength(self) -> int:
        """Maximum allowed number of characters."""
        return self.__maxlength

    # --------------------------------------------------------------------------
    def to_dict(self) -> dict[str, str | int | bool | list[str] | None]:
        """Convert the field object to a dictionary."""
        json_dict: dict[str, str | int | bool | list[str] | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                json_dict[f_name] = f_type
        return json_dict

    def to_json(self):
        """Convert field object to a json string."""
        return json.dumps(self.to_dict())

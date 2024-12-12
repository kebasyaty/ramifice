"""Field of Model for enter text."""

from .general.field import Field
from .general.text_group import TextGroup


class TextField(Field, TextGroup):
    """Field of Model for enter text."""

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 textarea: bool = False,
                 use_editor: bool = False,
                 default: str = '',
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 maxlength: int = 256,
                 regex: str = '',
                 regex_err_msg: list[str] | None = None,
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='TextField',
                       group='text',
                       )
        TextGroup.__init__(self,
                           input_type='text',
                           default=default,
                           placeholder=placeholder,
                           required=required,
                           readonly=readonly,
                           unique=unique,
                           )
        self.__textarea = textarea
        self.__use_editor = use_editor
        self.__maxlength = maxlength
        self.__regex = regex
        self.__regex_err_msg = regex_err_msg

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
    @property
    def regex(self) -> str:
        """Regular expression to validate the `value`.
        Example: ^[a-zA-Z0-9_]+$
        """
        return self.__regex

    # --------------------------------------------------------------------------
    @property
    def regex_err_msg(self) -> list[str] | None:
        """Error message.
        Example: ['Allowed chars: a-z, A-Z, 0-9, _']
        """
        return self.__regex_err_msg

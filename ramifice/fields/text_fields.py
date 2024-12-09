"""A field of Model for entering a text."""

from . import (field, groups)


class TextField(field.Field, groups.TextGroup):
    """A field of Model for entering a text."""

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
                 maxlength: int | None = None,
                 minlength: int | None = None,
                 ):
        field.Field.__init__(self,
                             label=label,
                             disabled=disabled,
                             hide=hide,
                             ignored=ignored,
                             hint=hint,
                             warning=warning,
                             field_type=type(self).__name__,
                             group='text',
                             )
        groups.TextGroup.__init__(self,
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
        self.__minlength = minlength

    # --------------------------------------------------------------------------
    @property
    def textarea(self) -> bool:
        """For Html textarea."""
        return self.__textarea

    # --------------------------------------------------------------------------
    @property
    def use_editor(self) -> bool:
        """Whether or not to use your preferred text editor - 
        CKEditor, TinyMCE, etc."""
        return self.__use_editor

    # --------------------------------------------------------------------------
    @property
    def maxlength(self) -> int | None:
        """The maximum number of characters allowed in the text."""
        return self.__maxlength

    # --------------------------------------------------------------------------
    @property
    def minlength(self) -> int | None:
        """The minimum number of characters allowed in the text."""
        return self.__minlength

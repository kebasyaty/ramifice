"""Field of Model for enter logical value."""

from .general.field import Field


class BoolField(Field):
    """Field of Model for enter logical value."""

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='BoolField',
                       group='bool',
                       )
        self.__input_type = 'checkbox'
        self.__value: bool | None = None

    @property
    def input_type(self) -> str:
        """Input type for a web form field.
        Html tag: input type="checkbox".
        """
        return self.__input_type

    # --------------------------------------------------------------------------
    @property
    def value(self) -> bool | None:
        """Sets the value of an element."""
        return self.__value

    @value.setter
    def value(self, value: bool | None) -> None:
        self.__value = value
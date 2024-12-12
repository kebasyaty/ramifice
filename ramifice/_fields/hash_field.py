"""Field of Model for enter identifier of document."""

from .general.field import Field


class HashField(Field):
    """Field of Model for enter identifier of document."""

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 maxlength: int = 24,
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='HashField',
                       group='hash',
                       )
        self.__input_type = 'text'
        self.__value = ''
        self.__placeholder = placeholder
        self.__required = required
        self.__readonly = readonly
        self.__unique = unique
        self.__maxlength = maxlength

    @property
    def input_type(self) -> str:
        """\
        Input type for a web form field.
        Html tag: input type="text".
        """
        return self.__input_type

    # --------------------------------------------------------------------------
    @property
    def value(self) -> str:
        """Sets the value of an element."""
        return self.__value

    @value.setter
    def value(self, value: str) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def placeholder(self) -> str:
        """Displays prompt text."""
        return self.__placeholder

    # --------------------------------------------------------------------------
    @property
    def required(self) -> bool:
        """Required field."""
        return self.__required

    # --------------------------------------------------------------------------
    @property
    def readonly(self) -> bool:
        """Specifies that the field cannot be modified by the user."""
        return self.__readonly

    # --------------------------------------------------------------------------
    @property
    def unique(self) -> bool:
        """The unique value of a field in a collection."""
        return self.__unique

    # --------------------------------------------------------------------------
    @property
    def maxlength(self) -> int:
        """Maximum allowed number of characters."""
        return self.__maxlength

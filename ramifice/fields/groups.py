"""Classes of Group parameters for fields of Model."""


class TextGroup:
    """Parameters for the text group of fields."""

    def __init__(self,
                 input_type: str = "",
                 default: str = '',
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 ):
        self.__input_type = input_type
        self.__value = ''
        self.__default = default
        self.__placeholder = placeholder
        self.__required = required
        self.__readonly = readonly
    # --------------------------------------------------------------------------

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
    def default(self) -> str:
        """Value by default."""
        return self.__default

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

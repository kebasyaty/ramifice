"""General additional parameters for password field."""


class PasswordGroup:
    """General additional parameters for password field."""

    def __init__(self,
                 input_type: str = "",
                 placeholder: str = '',
                 required: bool = False,
                 ):
        self.__input_type = input_type
        self.__value = ''
        self.__placeholder = placeholder
        self.__required = required

    # --------------------------------------------------------------------------
    @property
    def input_type(self) -> str:
        """Input type for a web form field.
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

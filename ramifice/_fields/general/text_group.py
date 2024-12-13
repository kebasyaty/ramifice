"""General additional parameters for text fields."""


class TextGroup:
    """General additional parameters for text fields."""

    def __init__(self,
                 input_type: str = "",
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 ):
        self.__input_type = input_type
        self.__value: str | None = None
        self.__placeholder = placeholder
        self.__required = required
        self.__readonly = readonly
        self.__unique = unique

    @property
    def input_type(self) -> str:
        """Input type for a web form field.
        Html tag: input type="text".
        """
        return self.__input_type

    # --------------------------------------------------------------------------
    @property
    def value(self) -> str | None:
        """Sets the value of an element."""
        return self.__value

    @value.setter
    def value(self, value: str | None) -> None:
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

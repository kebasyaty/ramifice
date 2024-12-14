"""General additional parameters for choice fields."""


class ChoiceGroup:
    """General additional parameters for choice fields."""

    def __init__(self,
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 multiple: bool = False,
                 ):
        self.__value: str | None = None
        self.__placeholder = placeholder
        self.__required = required
        self.__readonly = readonly
        self.__unique = unique
        self.__multiple = multiple

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

    # --------------------------------------------------------------------------
    @property
    def multiple(self) -> bool:
        """Specifies that multiple options can be selected at once."""
        return self.__multiple

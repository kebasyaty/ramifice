"""General additional parameters for number fields."""


class NumberGroup:
    """General additional parameters for number fields.

    Attributes:
    placeholder -- Displays prompt text.
    required -- Required field.
    readonly -- Specifies that the field cannot be modified by the user.
    unique -- The unique value of a field in a collection.
    """

    def __init__(self,
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 ):
        self.__placeholder = placeholder
        self.__required = required
        self.__readonly = readonly
        self.__unique = unique

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

"""General additional parameters for choice fields."""


class ChoiceGroup:
    """General additional parameters for choice fields.

    Attributes:
    input_type -- Input type for a web form field.
    placeholder -- Displays prompt text.
    required -- Required field.
    readonly -- Specifies that the field cannot be modified by the user.
    unique -- The unique value of a field in a collection.
    multiple -- Specifies that multiple options can be selected at once.
    """

    def __init__(self,
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 multiple: bool = False,
                 ):
        self.__placeholder = placeholder
        self.__required = required
        self.__readonly = readonly
        self.__unique = unique
        self.__multiple = multiple

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

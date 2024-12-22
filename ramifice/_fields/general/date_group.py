"""General additional parameters for date|datetime fields."""


class DateGroup:
    """General additional parameters for date|datetime fields.

    Attributes:
    input_type -- Input type for a web form field.
    placeholder -- Displays prompt text.
    required -- Required field.
    readonly -- Specifies that the field cannot be modified by the user.
    unique -- The unique value of a field in a collection.
    max_date -- Maximum allowed date.
    min_date -- Minimum allowed date.
    """

    def __init__(
        self,
        input_type: str = "",
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        max_date: str | None = None,
        min_date: str | None = None,
    ):
        self.__input_type = input_type
        self.__value: str | None = None
        self.__placeholder = placeholder
        self.__required = required
        self.__readonly = readonly
        self.__unique = unique
        self.__max_date = max_date
        self.__min_date = min_date

    @property
    def input_type(self) -> str:
        """Input type for a web form field.
        Html tag: input type="date|datetime".
        """
        return self.__input_type

    # --------------------------------------------------------------------------
    @property
    def value(self) -> str | None:
        """Sets value of field."""
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
    def max_date(self) -> str | None:
        """Maximum allowed date."""
        return self.__max_date

    # --------------------------------------------------------------------------
    @property
    def min_date(self) -> str | None:
        """Minimum allowed date."""
        return self.__min_date

"""General additional parameters for number fields."""


class NumberGroup:
    """General additional parameters for number fields.

    Attributes:
    placeholder -- Displays prompt text.
    required -- Required field.
    readonly -- Specifies that the field cannot be modified by the user.
    unique -- The unique value of a field in a collection.
    """

    def __init__(
        self,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ):
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique

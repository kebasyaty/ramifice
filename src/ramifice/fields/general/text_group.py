"""General additional parameters for text fields."""


class TextGroup:
    """General additional parameters for text fields.

    Attributes:
        input_type -- Input type for a web form field.
        placeholder -- Displays prompt text.
        required -- Required field.
        readonly -- Specifies that the field cannot be modified by the user.
        unique -- The unique value of a field in a collection.
    """

    def __init__(  # noqa: D107
        self,
        input_type: str = "",
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ):
        self.input_type = input_type
        self.value: str | None = None
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique

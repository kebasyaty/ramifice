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

    def __init__(
        self,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        multiple: bool = False,
    ):
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique
        self.multiple = multiple

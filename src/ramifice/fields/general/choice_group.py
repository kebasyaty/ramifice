"""General additional parameters for choice fields."""

__all__ = ("ChoiceGroup",)

from abc import ABCMeta


class ChoiceGroup(metaclass=ABCMeta):
    """General additional parameters for choice fields.

    Args:
        input_type: Input type for a web form field.
        placeholder: Displays prompt text.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        unique: The unique value of a field in a collection.
        multiple: Specifies that multiple options can be selected at once.
    """

    def __init__(  # noqa: D107
        self,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        multiple: bool = False,
    ) -> None:
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique
        self.multiple = multiple

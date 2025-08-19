"""General additional parameters for text fields."""

from __future__ import annotations

__all__ = ("TextGroup",)


class TextGroup:
    """General additional parameters for text fields.

    Args:
        input_type: Input type for a web form field.
        placeholder: Displays prompt text.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        unique: The unique value of a field in a collection.
    """

    def __init__(  # noqa: D107
        self,
        input_type: str = "",
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ) -> None:
        self.input_type = input_type
        self.value: str | None = None
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique

    def __len__(self) -> int:
        """Return length of field `value`."""
        value = self.value
        if value is None:
            return 0
        return len(value)

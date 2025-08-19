"""General additional parameters for number fields."""

from __future__ import annotations

__all__ = ("NumberGroup",)


class NumberGroup:  # noqa: B903
    """General additional parameters for number fields.

    Args:
        placeholder: Displays prompt text.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        unique: The unique value of a field in a collection.
    """

    def __init__(  # noqa: D107
        self,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ) -> None:
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique

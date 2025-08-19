"""General additional parameters for date|datetime fields."""

from __future__ import annotations

__all__ = ("DateGroup",)

from datetime import datetime


class DateGroup:
    """General additional parameters for date|datetime fields.

    Args:
        input_type: Input type for a web form field.
        placeholder: Displays prompt text.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
        unique: The unique value of a field in a collection.
        max_date: Maximum allowed date.
        min_date: Minimum allowed date.
    """

    def __init__(  # noqa: D107
        self,
        input_type: str = "",
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        max_date: datetime | None = None,
        min_date: datetime | None = None,
    ) -> None:
        self.input_type = input_type
        self.value: datetime | None = None
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique
        self.max_date = max_date
        self.min_date = min_date

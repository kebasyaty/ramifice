"""Unit - Data management in dynamic fields."""

from __future__ import annotations

__all__ = ("Unit",)

import logging

from ramifice.utils.errors import PanicError
from ramifice.utils.mixins import JsonMixin

logger = logging.getLogger(__name__)


class Unit(JsonMixin):
    """Unit of information for `choices` parameter in dynamic field types.

    Args:
        field: The name of the dynamic field.
        title: The name of the choice item.
        value: The value of the choice item.
        is_delete: True - if you need to remove the item of choice.
    """

    def __init__(  # noqa: D107
        self,
        field: str,
        title: dict[str, str],  # Example: {"en": "Title", "ru": "Заголовок"}
        value: float | int | str,
        is_delete: bool = False,
    ) -> None:
        # Check the match of types.
        if not isinstance(field, str):
            msg = "Class: `Unit` > Field: `field` => Not а `str` type!"
            raise PanicError(msg)
        if not isinstance(title, dict):
            msg = "Class: `Unit` > Field: `title` => Not а `str` type! " + 'Example: {"en": "Title", "ru": "Заголовок"}'
            raise PanicError(msg)
        if not isinstance(value, (float, int, str)):
            msg = "Class: `Unit` > Field: `value` => Not a `float | int | str` type!"
            raise PanicError(msg)
        if not isinstance(is_delete, bool):
            msg = "Class: `Unit` > Field: `is_delete` => Not a `bool` type!"
            raise PanicError(msg)

        JsonMixin.__init__(self)

        self.field = field
        self.title = title
        self.value = value
        self.is_delete = is_delete

        self.check_empty_arguments()

    def check_empty_arguments(self) -> None:
        """Check the arguments for empty values.

        Returns:
            `None` or raised exception `PanicError`.
        """
        field_name: str = ""

        if len(self.field) == 0:
            field_name = "field"
        elif len(self.title) == 0:
            field_name = "title"
        elif isinstance(self.value, str) and len(self.value) == 0:
            field_name = "value"

        if len(field_name) > 0:
            msg = (
                "Method: `unit_manager` > "
                + "Argument: `unit` > "
                + f"Field: `{field_name}` => "
                + "Must not be empty!"
            )
            logger.critical(msg)
            raise PanicError(msg)

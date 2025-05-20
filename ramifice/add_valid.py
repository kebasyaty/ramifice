"""Additional validation of fields."""

from abc import ABCMeta


class AddValidMixin(metaclass=ABCMeta):
    """Additional validation of fields."""

    async def add_validation(self) -> dict[str, str]:
        """It is supposed to be use to additional validation of fields.
        Format: <"field_name", "Error message">
        """
        error_map: dict[str, str] = {}
        return error_map

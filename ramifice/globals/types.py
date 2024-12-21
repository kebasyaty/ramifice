"""Global data types."""

from typing import Any


class OutputData:
    """Output data type for the `Model.check()` method."""

    def __init__(self, data: dict[str, Any], valid: bool, update: bool):
        self.__data = data
        self.__valid = valid
        self.__update = update

    @property
    def data(self) -> dict[str, Any]:
        """Output data."""
        return self.__data

    @property
    def valid(self) -> bool:
        """Status of output data."""
        return self.__valid

    @valid.setter
    def valid(self, value: bool) -> None:
        self.__valid = value

    @property
    def update(self) -> bool:
        """How to use data?
        For create a new document or to update the existing document.
        """
        return self.__update


class Unit:
    """Unit of information for `choices` parameter in dynamic field types."""

    def __init__(self, field: str, title: str, value: float | int | str, delete: bool = False):
        self.__field = field
        self.__title = title
        self.__value = value
        self.__delete = delete

    @property
    def field(self) -> str:
        """Field name."""
        return self.__field

    @property
    def title(self) -> str:
        """Title of dynamic item in parameter `choices`."""
        return self.__title

    @property
    def value(self) -> float | int | str:
        """Value of dynamic item in parameter `choices`."""
        return self.__value

    @property
    def delete(self) -> bool:
        """How to use `unit`?
        To add or to remove the dynamic element.
        """
        return self.__delete

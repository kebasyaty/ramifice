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

    @property
    def update(self) -> bool:
        """How to use data?
        For create a new document or to update the existing document.
        """
        return self.__update

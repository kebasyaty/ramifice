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


class FileData:
    """Data type for `FileField.value`."""

    def __init__(self):
        self.__path = ""
        self.__url = ""
        self.__name = ""
        self.__size = 0
        self.__new_file_data = False
        self.__delete = False
        self.__extension = ""
        self.__save_as_is = False

    @property
    def path(self) -> str:
        """Path to file."""
        return self.__path

    @path.setter
    def path(self, value: str) -> None:
        self.__path = value

    # --------------------------------------------------------------------------
    @property
    def url(self) -> str:
        """URL to file."""
        return self.__url

    @url.setter
    def url(self, value: str) -> None:
        self.__url = value

    # --------------------------------------------------------------------------
    @property
    def name(self) -> str:
        """Original file name."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    # --------------------------------------------------------------------------
    @property
    def size(self) -> int:
        """File size in bytes."""
        return self.__size

    @size.setter
    def size(self, value: str) -> None:
        self.__size = value

    # --------------------------------------------------------------------------
    @property
    def new_file_data(self) -> bool:
        """A sign of a new file.
        true - if there is no file in the database.
        """
        return self.__new_file_data

    @new_file_data.setter
    def new_file_data(self, value: str) -> None:
        self.__new_file_data = value

    # --------------------------------------------------------------------------
    @property
    def delete(self) -> bool:
        """If the file needs to be deleted: `delete=True`.
        By default: True.
        """
        return self.__delete

    @delete.setter
    def delete(self, value: bool) -> None:
        self.__delete = value

    # --------------------------------------------------------------------------
    @property
    def extension(self) -> str:
        """File extension.
        Examples: `.txt|.xml|.doc|.svg`.
        """
        return self.__extension

    @extension.setter
    def extension(self, value: str) -> None:
        self.__extension = value

    # --------------------------------------------------------------------------
    @property
    def save_as_is(self) -> bool:
        """To copy data from a related document and use the same files."""
        return self.__save_as_is

    @save_as_is.setter
    def save_as_is(self, value: bool) -> None:
        self.__save_as_is = value

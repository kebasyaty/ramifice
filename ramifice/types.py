"""A collection of additional data types."""

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


class ImageData:
    """Data type for `ImageField.value`."""

    def __init__(self):
        self.__path = ""
        self.__path_xs = ""
        self.__path_sm = ""
        self.__path_md = ""
        self.__path_lg = ""
        self.__url = ""
        self.__url_xs = ""
        self.__url_sm = ""
        self.__url_md = ""
        self.__url_lg = ""

    @property
    def path(self) -> str:
        """Path to a copy of original image."""
        return self.__path

    @path.setter
    def path(self, value: str) -> None:
        self.__path = value

    # --------------------------------------------------------------------------
    @property
    def path_xs(self) -> str:
        """Path to miniature of image, size of `xs`."""
        return self.__path_xs

    @path_xs.setter
    def path_xs(self, value: str) -> None:
        self.__path_xs = value

    # --------------------------------------------------------------------------
    @property
    def path_sm(self) -> str:
        """Path to miniature of image, size of `sm`."""
        return self.__path_sm

    @path_sm.setter
    def path_sm(self, value: str) -> None:
        self.__path_sm = value

    # --------------------------------------------------------------------------
    @property
    def path_md(self) -> str:
        """Path to miniature of image, size of `md`."""
        return self.__path_md

    @path_md.setter
    def path_md(self, value: str) -> None:
        self.__path_md = value

    # --------------------------------------------------------------------------
    @property
    def path_lg(self) -> str:
        """Path to miniature of image, size of `lg`."""
        return self.__path_lg

    @path_lg.setter
    def path_lg(self, value: str) -> None:
        self.__path_lg = value

    # --------------------------------------------------------------------------
    @property
    def url(self) -> str:
        """URL path to a copy of original image."""
        return self.__url

    @url.setter
    def url(self, value: str) -> None:
        self.__url = value

    # --------------------------------------------------------------------------
    @property
    def url_xs(self) -> str:
        """URL path to miniature of image, size of `xs`."""
        return self.__url_xs

    @url_xs.setter
    def url_xs(self, value: str) -> None:
        self.__url_xs = value

    # --------------------------------------------------------------------------
    @property
    def url_sm(self) -> str:
        """URL path to miniature of image, size of `sm`."""
        return self.__url_sm

    @url_sm.setter
    def url_sm(self, value: str) -> None:
        self.__url_sm = value

    # --------------------------------------------------------------------------
    @property
    def url_md(self) -> str:
        """URL path to miniature of image, size of `md`."""
        return self.__url_md

    @url_md.setter
    def url_md(self, value: str) -> None:
        self.__url_md = value

    # --------------------------------------------------------------------------
    @property
    def url_lg(self) -> str:
        """URL path to miniature of image, size of `lg`."""
        return self.__url_lg

    @url_lg.setter
    def url_lg(self, value: str) -> None:
        self.__url_lg = value

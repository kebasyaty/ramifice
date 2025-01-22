"""A collection of additional data types."""

import json
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

    def __init__(
        self, field: str, title: str, value: float | int | str, delete: bool = False
    ):
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
        self.__is_new_file = False
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
    def is_new_file(self) -> bool:
        """A sign of a new file.
        true - if there is no file in the database.
        """
        return self.__is_new_file

    @is_new_file.setter
    def is_new_file(self, value: str) -> None:
        self.__is_new_file = value

    # --------------------------------------------------------------------------
    @property
    def delete(self) -> bool:
        """If the file needs to be deleted: `delete=True`.
        By default: False.
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

    # --------------------------------------------------------------------------
    def to_dict(self) -> dict[str, str | int | bool | None]:
        """Convert fields to a dictionary."""
        json_dict: dict[str, str | int | bool | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                json_dict[f_name] = f_type
        return json_dict

    @classmethod
    def from_dict(cls, json_dict: dict[str, str | int | bool | None]) -> Any:
        """Convert the JSON string to a FileData instance."""
        file_obj = cls()
        for f_name, f_type in json_dict.items():
            file_obj.__dict__[f_name] = f_type
        return file_obj

    def to_json(self):
        """Convert a dictionary of fields to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert the JSON string to a FileData instance."""
        file_obj = cls()
        json_dict = json.loads(json_str)
        for f_name, f_type in json_dict.items():
            file_obj.__dict__[f_name] = f_type
        return file_obj


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
        self.__name = ""
        self.__width = 0
        self.__height = 0
        self.__size = 0
        self.__is_new_img = False
        self.__delete = False
        self.__extension = ""
        self.__imgs_dir_path = ""
        self.__imgs_dir_url = ""
        self.__save_as_is = False

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

    # --------------------------------------------------------------------------
    @property
    def name(self) -> str:
        """Name of original image."""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    # --------------------------------------------------------------------------
    @property
    def width(self) -> int:
        """Width in pixels of original image."""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        self.__width = value

    # --------------------------------------------------------------------------
    @property
    def height(self) -> int:
        """Height in pixels of original image."""
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        self.__height = value

    # --------------------------------------------------------------------------
    @property
    def size(self) -> int:
        """Size in pixels of original image."""
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        self.__size = value

    # --------------------------------------------------------------------------
    @property
    def is_new_img(self) -> bool:
        """A sign of a new image.
        True - If there is no this image in the database.
        """
        return self.__is_new_img

    @is_new_img.setter
    def is_new_img(self, value: bool) -> None:
        self.__is_new_img = value

    # --------------------------------------------------------------------------
    @property
    def delete(self) -> bool:
        """If the image needs to be deleted: `delete=True`.
        By default: False.
        """
        return self.__delete

    @delete.setter
    def delete(self, value: bool) -> None:
        self.__delete = value

    # --------------------------------------------------------------------------
    @property
    def extension(self) -> str:
        """Image extension.
        Examples: `.png|.jpeg|.jpg|.webp`.
        """
        return self.__extension

    @extension.setter
    def extension(self, value: str) -> None:
        self.__extension = value

    # ---------------------------------------------------------------------------
    @property
    def imgs_dir_path(self) -> str:
        """Path to target directory with images."""
        return self.__imgs_dir_path

    @imgs_dir_path.setter
    def imgs_dir_path(self, value: str) -> None:
        self.__imgs_dir_path = value

    # ---------------------------------------------------------------------------
    @property
    def imgs_dir_url(self) -> str:
        """URL path to target directory with images."""
        return self.__imgs_dir_url

    @imgs_dir_url.setter
    def imgs_dir_url(self, value: str) -> None:
        self.__imgs_dir_url = value

    # --------------------------------------------------------------------------
    @property
    def save_as_is(self) -> bool:
        """To copy data from a related document and use the same images."""
        return self.__save_as_is

    @save_as_is.setter
    def save_as_is(self, value: bool) -> None:
        self.__save_as_is = value

    # --------------------------------------------------------------------------
    def to_dict(self) -> dict[str, str | int | bool | None]:
        """Convert fields to a dictionary."""
        json_dict: dict[str, str | int | bool | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                json_dict[f_name] = f_type
        return json_dict

    @classmethod
    def from_dict(cls, json_dict: dict[str, str | int | bool | None]) -> Any:
        """Convert the JSON string to a ImageData instance."""
        img_obj = cls()
        for f_name, f_type in json_dict.items():
            img_obj.__dict__[f_name] = f_type
        return img_obj

    def to_json(self):
        """Convert a dictionary of fields to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert the JSON string to a ImageData instance."""
        img_obj = cls()
        json_dict = json.loads(json_str)
        for f_name, f_type in json_dict.items():
            img_obj.__dict__[f_name] = f_type
        return img_obj

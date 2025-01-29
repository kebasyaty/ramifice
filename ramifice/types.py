"""A collection of additional data types."""

from typing import Any

from .mixins import JsonMixin


class OutputData:
    """Output data type for the `Model.check()` method."""

    def __init__(self, data: dict[str, Any], is_valid: bool, is_update: bool):
        self.data = data
        self.is_valid = is_valid
        self.is_update = is_update


class Unit(JsonMixin):
    """Unit of information for `choices` parameter in dynamic field types."""

    def __init__(
        self, field: str, title: str, value: float | int | str, is_delete: bool = False
    ):
        JsonMixin.__init__(self)
        self.field = field
        self.title = title
        self.value = value
        self.is_delete = is_delete


class FileData(JsonMixin):
    """Data type for `FileField.value`."""

    def __init__(self):
        JsonMixin.__init__(self)
        self.path = ""
        self.url = ""
        self.name = ""
        self.size = 0
        self.is_new_file = False
        self.is_delete = False
        self.extension = ""
        self.save_as_is = False


class ImageData(JsonMixin):
    """Data type for `ImageField.value`."""

    def __init__(self):
        JsonMixin.__init__(self)
        self.path = ""
        self.path_xs = ""
        self.path_sm = ""
        self.path_md = ""
        self.path_lg = ""
        self.url = ""
        self.url_xs = ""
        self.url_sm = ""
        self.url_md = ""
        self.url_lg = ""
        self.name = ""
        self.width = 0
        self.height = 0
        self.size = 0
        self.is_new_img = False
        self.is_delete = False
        self.extension = ""
        self.imgs_dir_path = ""
        self.imgs_dir_url = ""
        self.save_as_is = False

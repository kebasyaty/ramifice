"""A collection of additional data types."""

from typing import Any

from .mixins import JsonMixin


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


# For `FileField.value`.
FILE_DATA_TYPE = dict(
    path="",
    url="",
    name="",
    size=0,
    is_new_file=False,
    is_delete=False,
    extension="",
    save_as_is=False,
)

# For `ImageField.value`.
IMAGE_DATA_TYPE = dict(
    path="",
    path_xs="",
    path_sm="",
    path_md="",
    path_lg="",
    url="",
    url_xs="",
    url_sm="",
    url_md="",
    url_lg="",
    name="",
    width=0,
    height=0,
    size=0,
    is_new_img=False,
    is_delete=False,
    extension="",
    imgs_dir_path="",
    imgs_dir_url="",
    save_as_is=False,
    # Extension to the upper register and delete the point.
    ext_upper="",
)

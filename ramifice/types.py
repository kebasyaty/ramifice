"""Auxiliary types collection.

These types are used to transfer information.

The module contains the following types:

- `Unit` - Used for data management in dynamic fields.
- `FILE_DATA_TYPE` - To transmit file information.
- `IMAGE_DATA_TYPE` - To transmit information about the image..
"""

from .errors import PanicError
from .mixins import JsonMixin


class Unit(JsonMixin):
    """Unit of information for `choices` parameter in dynamic field types.

    Attributes:
        field -- The name of the field.
        title -- The name of the choice item.
        value -- The value of the choice item.
        is_delete -- True - if you need to remove the item of choice.
    """

    def __init__(
        self, field: str, title: str, value: float | int | str, is_delete: bool = False
    ):
        # Check the match of types.
        if not isinstance(field, str):
            msg = "Class: `Unit` > Field: `field` => Not а `str` type!"
            raise PanicError(msg)
        if not isinstance(title, str):
            msg = "Class: `Unit` > Field: `title` => Not а `str` type!"
            raise PanicError(msg)
        if not isinstance(value, (float, int, str)):
            msg = "Class: `Unit` > Field: `value` => Not а `float | int | str` type!"
            raise PanicError(msg)
        if not isinstance(is_delete, bool):
            msg = "Class: `Unit` > Field: `is_delete` => Not а `bool` type!"
            raise PanicError(msg)

        JsonMixin.__init__(self)

        self.field = field
        self.title = title
        self.value = value
        self.is_delete = is_delete

        self.check_empty_arguments()

    def check_empty_arguments(self) -> None:
        """Error: If any of the arguments in the Unit is empty.

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
            raise PanicError(msg)


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

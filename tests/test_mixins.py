"""Testing the class `ramifice.mixins.JsonMixin`."""

import unittest

from ramifice import model
from ramifice.fields import (
    BooleanField,
    ChoiceFloatDynField,
    ChoiceFloatField,
    ChoiceFloatMultDynField,
    ChoiceFloatMultField,
    ChoiceIntDynField,
    ChoiceIntField,
    ChoiceIntMultDynField,
    ChoiceIntMultField,
    ChoiceTextDynField,
    ChoiceTextField,
    ChoiceTextMultDynField,
    ChoiceTextMultField,
    ColorField,
    DateField,
    DateTimeField,
    EmailField,
    FileField,
    FloatField,
    IDField,
    ImageField,
    IntegerField,
    IPField,
    PasswordField,
    PhoneField,
    SlugField,
    TextField,
    URLField,
)
from ramifice.utils.mixins import JsonMixin

# For `FileField.value`.
FILE_INFO_DICT: dict[str, str | int | bool] = dict(
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
IMG_INFO_DICT: dict[str, str | int | bool] = dict(
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
    ext_upper="",
)


class StandardTypes(JsonMixin):
    """Class for testing."""

    def __init__(self) -> None:  # noqa: D107
        JsonMixin.__init__(self)
        self.x1 = {"x": 1, "y": 2}
        self.x2 = [1, 2, 3]
        self.x3 = (1, 2, 3)
        self.x4 = "Hello world!"
        self.x5 = 12
        self.x6 = 12.3
        self.x7 = True
        self.x8 = False
        self.x9 = None


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self) -> None:
        """For adding fields."""
        self.url = URLField()
        self.txt = TextField()
        self.txt2 = TextField(multi_language=True)
        self.slug = SlugField()
        self.phone = PhoneField()
        self.password = PasswordField()
        self.ip = IPField()
        self.num_int = IntegerField()
        self.num_float = FloatField()
        self.img = ImageField()
        self.hash2 = IDField()
        self.file = FileField()
        self.email = EmailField()
        self.date_time = DateTimeField()
        self.date = DateField()
        self.color = ColorField()
        self.bool = BooleanField()
        self.choice_float_dyn = ChoiceFloatDynField()
        self.choice_float = ChoiceFloatField()
        self.choice_float_mult_dyn = ChoiceFloatMultDynField()
        self.choice_float_mult = ChoiceFloatMultField()
        self.choice_int_dyn = ChoiceIntDynField()
        self.choice_int_mult_dyn = ChoiceIntMultDynField()
        self.choice_int_mult = ChoiceIntMultField()
        self.choice_txt_dyn = ChoiceTextDynField()
        self.choice_txt = ChoiceTextField()
        self.choice_txt_mult_dyn = ChoiceTextMultDynField()
        self.choice_txt_mult = ChoiceTextMultField()
        self.choice_int = ChoiceIntField(choices=[[1, "Title"], [2, "Title 2"]])


class TestJsonMixin(unittest.TestCase):
    """Testing the class `JsonMixin`."""

    def test_standard_types(self) -> None:
        """Testing standard types to JSON."""
        x = StandardTypes()
        json_str = x.to_json()
        y = StandardTypes.from_json(json_str)
        self.assertEqual(x.x1, y.x1)
        self.assertEqual(x.x2, y.x2)
        self.assertEqual(x.x3, (1, 2, 3))  # y.x3 == [1, 2, 3]
        self.assertEqual(x.x4, y.x4)
        self.assertEqual(x.x5, y.x5)
        self.assertEqual(x.x6, y.x6)
        self.assertEqual(x.x7, y.x7)
        self.assertEqual(x.x8, y.x8)
        self.assertEqual(x.x9, y.x9)

    def test_fields(self) -> None:
        """Testing the Ramifice fields to JSON."""
        m = User()

        json_str = m.to_json()
        User.from_json(json_str)
        m2 = User.from_json(json_str)
        for name, data in m.__dict__.items():
            if not callable(data):
                self.assertEqual(m2.__dict__[name].__dict__, data.__dict__)

        json_str = m.to_json_only_value()
        User.from_json_only_value(json_str)
        m3 = User.from_json_only_value(json_str)
        for name, data in m.__dict__.items():
            if not callable(data):
                self.assertEqual(m3.__dict__[name].__dict__, data.__dict__)

        m = User()
        m.img.value = IMG_INFO_DICT.copy()
        m.file.value = FILE_INFO_DICT.copy()

        json_str = m.to_json()
        m2 = User.from_json(json_str)
        for name, data in m.__dict__["img"].__dict__["value"].items():
            if not callable(data):
                data2 = m2.__dict__["img"].__dict__["value"][name]
                self.assertEqual(data, data2)
        for name, data in m.__dict__["file"].__dict__["value"].items():
            if not callable(data):
                data2 = m2.__dict__["file"].__dict__["value"][name]
                self.assertEqual(data, data2)

        json_str = m.to_json_only_value()
        m3 = User.from_json_only_value(json_str)
        for name, data in m.__dict__["img"].__dict__["value"].items():
            if not callable(data):
                data2 = m2.__dict__["img"].__dict__["value"][name]
                self.assertEqual(data, data2)
        for name, data in m.__dict__["file"].__dict__["value"].items():
            if not callable(data):
                data2 = m2.__dict__["file"].__dict__["value"][name]
                self.assertEqual(data, data2)


if __name__ == "__main__":
    unittest.main()

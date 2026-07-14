"""Testing the class `ramifice.json.JsonMixin`."""

from __future__ import annotations

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


@model(service_name="Accounts")
class User:
    """Model for testing."""

    url = URLField()
    txt = TextField()
    txt2 = TextField(multi_language=True)
    slug = SlugField()
    phone = PhoneField()
    password = PasswordField()
    ip = IPField()
    num_int = IntegerField()
    num_float = FloatField()
    img = ImageField()
    hash2 = IDField()
    file = FileField()
    email = EmailField()
    date_time = DateTimeField()
    date = DateField()
    color = ColorField()
    bool = BooleanField()
    choice_float_dyn = ChoiceFloatDynField()
    choice_float = ChoiceFloatField()
    choice_float_mult_dyn = ChoiceFloatMultDynField()
    choice_float_mult = ChoiceFloatMultField()
    choice_int_dyn = ChoiceIntDynField()
    choice_int_mult_dyn = ChoiceIntMultDynField()
    choice_int_mult = ChoiceIntMultField()
    choice_txt_dyn = ChoiceTextDynField()
    choice_txt = ChoiceTextField()
    choice_txt_mult_dyn = ChoiceTextMultDynField()
    choice_txt_mult = ChoiceTextMultField()
    choice_int = ChoiceIntField(choices=[[1, "Title"], [2, "Title 2"]])


class TestJsonMixin(unittest.TestCase):
    """Testing the class `JsonMixin`."""

    def test_fields(self) -> None:
        """Testing all fields."""
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

    def test_file_fields(self) -> None:
        """Testing file type fields."""
        m = User()
        m.img = IMG_INFO_DICT.copy()
        m.file = FILE_INFO_DICT.copy()

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


if __name__ == "__main__":
    unittest.main()

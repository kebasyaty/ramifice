"""Testing the class `ramifice.json.JsonMixin`."""

from __future__ import annotations

import unittest
from datetime import datetime

from bson.objectid import ObjectId

from ramifice import Model, meta
from ramifice.config import Config
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


@meta(service_name="Accounts")
class User(Model):
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

    def test_with_default_values(self) -> None:
        """Testing with default values."""
        metadata = User.META
        descriptor_fields = metadata["all_descriptor_fields"]

        m = User()
        json_dict = m.to_dict()
        json_str = m.to_json()

        m2 = User.from_dict(json_dict)
        for f_name in descriptor_fields:
            self.assertEqual(getattr(m2, f_name), None)
            self.assertTrue(hasattr(m2, f"{f_name}_html_attrs"))

        m3 = User.from_json(json_str)
        for f_name in descriptor_fields:
            self.assertEqual(getattr(m3, f_name), None)
            self.assertTrue(hasattr(m3, f"{f_name}_html_attrs"))

    def test_with_custom_values(self) -> None:
        """Testing with custom values."""
        metadata = User.META
        descriptor_fields = metadata["all_descriptor_fields"]

        m = User()

        m.id = ObjectId("507f1f77bcf86cd799439011")
        m.created_at = datetime.now(Config.UTC_TIMEZONE)
        m.updated_at = datetime.now(Config.UTC_TIMEZONE)
        m.url = "https://translate.google.com"
        m.txt = "Hello World!"
        m.slug = "hello-world"
        m.phone = "+1 806 589 2932"
        m.password = "*X71M6pWIQ£ZE:0t"  # noqa: S105
        m.ip = "192.178.24.142"
        m.num_int = 12
        m.num_float = 5.2
        m.img = IMG_INFO_DICT.copy()
        m.hash2 = ObjectId("507f1f77bcf86cd799439011")
        m.file = FILE_INFO_DICT.copy()
        m.email = "fllabrst6wi@zumnime.me"
        m.date_time = datetime.now(Config.UTC_TIMEZONE)
        m.date = datetime.now(Config.UTC_TIMEZONE)
        m.color = "#F54927"
        m.bool = True
        m.choice_float_dyn = 5.2
        m.choice_float = 5.2
        m.choice_float_mult_dyn = [5.1, 5.2]
        m.choice_float_mult = [5.1, 5.2]
        m.choice_int_dyn = 12
        m.choice_int_mult_dyn = [10, 12]
        m.choice_int_mult = [10, 12]
        m.choice_txt_dyn = "Hello World!"
        m.choice_txt = "Hello World!"
        m.choice_txt_mult_dyn = ["Hello World!", "Hello World!"]
        m.choice_txt_mult = ["Hello World!", "Hello World!"]
        m.choice_int = 12

        json_dict = m.to_dict()
        json_str = m.to_json()

        m2 = User.from_dict(json_dict)
        for f_name in descriptor_fields:
            field_type = getattr(m, f"{f_name}_html_attrs")["field_type"]
            if field_type == "PasswordField":
                self.assertIsNone(getattr(m2, f_name))
            else:
                self.assertEqual(getattr(m2, f_name), getattr(m, f_name))
            self.assertTrue(hasattr(m2, f"{f_name}_html_attrs"))

        m3 = User.from_json(json_str)
        for f_name in descriptor_fields:
            field_type = getattr(m, f"{f_name}_html_attrs")["field_type"]
            if field_type == "PasswordField":
                self.assertIsNone(getattr(m3, f_name))
            else:
                self.assertEqual(getattr(m3, f_name), getattr(m, f_name))
            self.assertTrue(hasattr(m3, f"{f_name}_html_attrs"))


if __name__ == "__main__":
    unittest.main()

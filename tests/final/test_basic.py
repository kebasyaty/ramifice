"""Testing the `basic` example."""

from __future__ import annotations

import re
import unittest
from datetime import datetime

from pymongo import AsyncMongoClient

from ramifice import (
    UTC_TIMEZONE,
    Migration,
    Model,
    NamedTuple,
    Translator,
    fields,
    meta,
    to_human_size,
)
from ramifice.config import Config

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELDS


@meta(service_name="Accounts")
class User(Model):
    """Model of User."""

    avatar = fields.ImageField(
        label=_("Avatar"),
        placeholder=_("Upload your photo"),
        default="public/media/default/no-photo.png",
        # Directory for images inside media directory.
        target_dir="users/avatars",
        # Available 4 sizes from lg to xs or None.
        # Hint: By default = None
        thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
        # The maximum size of the original image in bytes.
        # Hint: By default = 2 MB
        max_size=524288,  # 512 KB = 0.5 MB = 524288 Bytes (in binary)
        warning=[
            _("Maximum size: {}").format(to_human_size(524288)),
        ],
    )
    username = fields.TextField(
        label=_("Username"),
        placeholder=_("Enter your username"),
        max_length=150,
        required=True,
        unique=True,
        warning=[
            _("Allowed chars: {}").format("a-z A-Z 0-9 _"),
        ],
    )
    first_name = fields.TextField(
        label=_("First name"),
        placeholder=_("Enter your First name"),
        multi_language=True,  # Support for several language.
        max_length=150,
        required=True,
    )
    last_name = fields.TextField(
        label=_("Last name"),
        placeholder=_("Enter your Last name"),
        multi_language=True,  # Support for several language.
        max_length=150,
        required=True,
    )
    email = fields.EmailField(
        label=_("Email"),
        placeholder=_("Enter your email"),
        required=True,
        unique=True,
    )
    phone = fields.PhoneField(
        label=_("Phone number"),
        placeholder=_("Enter your phone number"),
        unique=True,
    )
    birthday = fields.DateField(
        label=_("Birthday"),
        placeholder=_("Enter your date of birth"),
    )
    description = fields.TextField(
        label=_("About yourself"),
        placeholder=_("Tell us a little about yourself ..."),
        multi_language=True,  # Support for several language.
    )
    password = fields.PasswordField(
        label=_("Password"),
        placeholder=_("Enter your password"),
    )
    confirm_password = fields.PasswordField(
        label=_("Confirm password"),
        placeholder=_("Repeat your password"),
        # If true, the value of this field is not saved in the database.
        ignored=True,
    )
    is_admin = fields.BooleanField(
        label=_("Is Administrator?"),
        warning=[
            _("Can this user access the admin panel?"),
        ],
    )
    is_active = fields.BooleanField(
        label=_("Is active?"),
        warning=[
            _("Is this an active account?"),
        ],
    )
    slug = fields.SlugField(
        label=_("Slug"),
        slug_sources=["username"],
        disabled=True,
        hide=True,
    )
    last_login = fields.DateTimeField(
        label=_("Last login"),
        disabled=True,
        hide=True,
        warning=[
            _("Date and time of user last login."),
        ],
    )

    # Optional method
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        _ = self._CUSTOM_TRANSLATOR.gettext
        err_map = self.get_error_map()

        username = self.username
        id = self.id
        password = self.password
        confirm_password = self.confirm_password

        # Check username
        if username is not None and re.match(r"^[a-zA-Z0-9_]+$", username) is None:
            err_map.update("username", _("Allowed chars: {}").format("a-z A-Z 0-9 _"))

        # Check password
        if id is None and password != confirm_password:
            err_map.update("password", _("Passwords do not match!"))

        return err_map


class TestBasicExample(unittest.IsolatedAsyncioTestCase):
    """Testing the `basic` example."""

    async def test_basic_example(self):
        """Testing the `basic` example."""
        # Maximum number of characters 60.
        database_name = "test_save_method"

        client = AsyncMongoClient(host=Config.MONGO_HOST)

        # Delete database before test.
        # (if the test fails)
        await client.drop_database(database_name)
        await client.close()
        #
        # ----------------------------------------------------------------------
        client = AsyncMongoClient(host=Config.MONGO_HOST)
        await Migration(
            database_name=database_name,
            mongo_client=client,
        ).migrate()

        user = User()
        user.username = "pythondev"
        user.first_name = {"en": "John", "ru": "Джон"}
        user.last_name = {"en": "Smith", "ru": "Смит"}
        user.email = "John_Smith@gmail.com"
        user.phone = "+447986123456"
        user.birthday = datetime(2000, 1, 25, tzinfo=UTC_TIMEZONE)
        user.description = {"en": "I program on Python!", "ru": "Я программирую на Python!"}
        user.password = "12345678"  # ruff:ignore[hardcoded-password-string]
        user.confirm_password = "12345678"  # ruff:ignore[hardcoded-password-string]

        # Create User.
        is_saved = await user.save()
        if not is_saved:
            user.print_err()
        self.assertTrue(is_saved)

        user_details = await User.find_one_to_instance_model({"_id": user.id})
        self.assertIsNotNone(user_details)
        self.assertEqual(user_details.created_at, user.created_at)
        self.assertEqual(user_details.updated_at, user.updated_at)
        self.assertEqual(user_details.username, user.username)
        self.assertEqual(user_details.first_name, user.first_name)
        self.assertEqual(user_details.last_name, user.last_name)
        self.assertEqual(user_details.email, user.email)
        self.assertEqual(user_details.phone, user.phone)
        self.assertEqual(user_details.birthday, user.birthday)
        self.assertEqual(user_details.description, user.description)
        self.assertIsNone(user_details.password)

        # Update User.
        user.username = "pythondev_123"
        is_saved = await user.save()
        if not is_saved:
            user.print_err()
        self.assertTrue(is_saved)

        user_details = await User.find_one_to_instance_model({"_id": user.id})
        self.assertIsNotNone(user_details)
        self.assertEqual(user_details.created_at, user.created_at)
        self.assertEqual(user_details.updated_at, user.updated_at)
        self.assertEqual(user_details.username, user.username)
        self.assertEqual(user_details.first_name, user.first_name)
        self.assertEqual(user_details.last_name, user.last_name)
        self.assertEqual(user_details.email, user.email)
        self.assertEqual(user_details.phone, user.phone)
        self.assertEqual(user_details.birthday, user.birthday)
        self.assertEqual(user_details.description, user.description)
        self.assertIsNone(user_details.password)
        # ----------------------------------------------------------------------
        #
        # Delete database after test.
        await client.drop_database(database_name)
        await client.close()


if __name__ == "__main__":
    unittest.main()

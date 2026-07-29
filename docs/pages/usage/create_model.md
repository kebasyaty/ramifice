[It is recommended to look at examples here.](https://github.com/kebasyaty/ramifice/tree/v2/examples "It is recommended to look at examples here.")

```py title="main.py" linenums="1"
import re
import asyncio
from pprint import pprint as pp

from pymongo import AsyncMongoClient

from ramifice import (
    Migration,
    Model,
    Translator,
    fields,
    meta,
    to_human_size,
)

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@model(service_name="Accounts")
class User:
    """User Model."""

    avatar = fields.ImageField(
        label=_("Avatar"),
        default="public/media/default/no-photo.png",
        # Directory for images inside media directory.
        target_dir="users/avatars",
        # Available 4 sizes from lg to xs or None.
        # Hint: Default = None
        thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
        # The maximum size of the original image in bytes.
        # Hint: Default = 2 MB
        max_size=524288,  # 0.5 MB = 512 KB = 524288 Bytes (in binary)
        warning=[
            _("Maximum size: {}").format(to_human_size(524288)),
        ],
    )
    username = fields.TextField(
        label=_("Username"),
        max_length=150,
        is_require=True,
        is_unique=True,
        warning=[
            _("Allowed characters: {}").format("a-z A-Z 0-9 _"),
            _("Maximum length: {}").format(150),
        ],
    )
    password = fields.PasswordField(
        label=_("Password"),
        warning=[
            _("Maximum length: {}").format(256),  # this is an immutable size
            _("Minimum length: {}").format(8),  # this is an immutable size
        ],
    )
    сonfirm_password = fields.PasswordField(
        label=_("Confirm password"),
        # If true, the value of this field is not saved in the database.
        is_ignore=True,
    )

    # Optional method
    async def add_validation(self) -> dict[str, Any]:
        """Additional validation of fields."""
        _ = self._CUSTOM_TRANSLATOR.gettext
        err_map = self.get_error_map()

        _id = self.id
        password = self.password
        сonfirm_password = self.сonfirm_password
        username = self.username

        # Check password
        if _id is None and password != сonfirm_password:
            err_map.update("password", _("Passwords do not match!"))

        # Check username
        if username is not None and re.match(r"^[a-zA-Z0-9_]+$", username) is None:
            err_map.update("username", _("Allowed characters: {}").format("a-z A-Z 0-9 _"))

        return err_map


async def main():
    client = AsyncMongoClient()

    await Migration(
        database_name="test_db",
        mongo_client=client,
    ).migrate()

    # Create User
    user = User("ru")
    # user.avatar__core.from_path("public/media/default/no-photo.png")
    # user.avatar__core.from_base64("base64-string")
    user.username = "pythondev"
    user.password = "12345678"
    user.сonfirm_password = "12345678"

    # Save User
    if not await user.save():
        # Convenient to use during development
        user.print_err()

    # Update User
    user.username = "pythondev_123"
    if not await user.save():
        user.print_err()

    print("User details:")
    user_details: dict | None = await User.find_one_to_model_dict(filter={"_id": user.id})
    if user_details is not None:
        pp(user_details)
    else:
        print("No User!")

    # Close connection
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
```

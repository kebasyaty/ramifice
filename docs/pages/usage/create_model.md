[It is recommended to look at examples here.](https://github.com/kebasyaty/ramifice/tree/v0/examples "It is recommended to look at examples here.")

```py title="main.py" linenums="1"
import re
import asyncio
from typing import Any
from datetime import datetime
from pprint import pprint as pp

from pymongo import AsyncMongoClient
from ramifice import (
    NamedTuple,
    model,
    translations,
    Migration,
    to_human_size,
)
from ramifice.fields import (
    ImageField,
    PasswordField,
    TextField,
)


@model(service_name="Accounts")
class User:
    """Model of User."""

    def fields(self) -> None:
        """Adding fields."""
        # For custom translations.
        gettext = translations.gettext
        # ngettext = translations.ngettext
        self.avatar = ImageField(
            label=gettext("Avatar"),
            default="public/media/default/no-photo.png",
            # Directory for images inside media directory.
            target_dir="users/avatars",
            # Available 4 sizes from lg to xs or None.
            # Hint: By default = None
            thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
            # The maximum size of the original image in bytes.
            # Hint: By default = 2 MB
            max_size=524288,  # 0.5 MB = 512 KB = 524288 Bytes (in binary)
            warning=[
                gettext("Maximum size: {}").format(to_human_size(524288)),
            ],
        )
        self.username = TextField(
            label=gettext("Username"),
            maxlength=150,
            required=True,
            unique=True,
            warning=[
                gettext("Allowed chars: {}").format("a-z A-Z 0-9 _"),
            ],
        )
        self.password = PasswordField(
            label=gettext("Password"),
        )
        self.сonfirm_password = PasswordField(
            label=gettext("Confirm password"),
            # If true, the value of this field is not saved in the database.
            ignored=True,
        )

    # Optional method
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        gettext = translations.gettext
        cd, err = self.get_clean_data()

        # Check username
        if re.match(r"^[a-zA-Z0-9_]+$", cd.username) is None:
            err.update("username", gettext("Allowed chars: {}").format("a-z A-Z 0-9 _"))

        # Check password
        if cd._id is None and (cd.password != cd.сonfirm_password):
            err.update("password", gettext("Passwords do not match!"))

        return err


async def main():
    client = AsyncMongoClient()

    await Migration(
        database_name="test_db",
        mongo_client=client,
    ).migrate()

    # If you need to change the language of translation.
    # Hint: For Ramifice by default = "en"
    translations.change_locale("en")

    user = User()
    # user.avatar.from_path("public/media/default/no-photo.png")
    user.username.value = "pythondev"
    user.password.value = "12345678"
    user.сonfirm_password.value = "12345678"

    # Create User.
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    # Update User.
    user.username.value = "pythondev_123"
    if not await user.save():
        user.print_err()

    print("User details:")
    user_details = await User.find_one_to_raw_doc(
        # {"_id": user.id.value}
        {f"username": user.username.value}
    )
    if user_details is not None:
        pp(user_details)
    else:
        print("No User!")

    # Remove User.
    # (if necessary)
    # await user.delete()
    # await user.delete(remove_files=False)

    # Remove collection.
    # (if necessary)
    # await User.collection().drop()

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
```

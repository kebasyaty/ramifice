# Getting started

<hr>

#### Installation

1. Install MongoDB (if not installed):

- [![Fedora](https://img.shields.io/badge/Fedora-294172?style=for-the-badge&logo=fedora&logoColor=white)](https://github.com/kebasyaty/ramifice/blob/v0/assets/FEDORA_INSTALL_MONGODB.md)
- [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://github.com/kebasyaty/ramifice/blob/v0/assets/UBUNTU_INSTALL_MONGODB.md)
- [![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.mongodb.com/try/download/community)

2. Run:

```shell
# Fedora:
sudo dnf install gettext
gettext --version
# Ubuntu:
sudo apt install gettext
gettext --version
# Windows:
https://mlocati.github.io/articles/gettext-iconv-windows.html
gettext --version

cd project_name
uv add ramifice
```

3. Add `config` and `public` directories in root of your project:

- [Download config directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/main/config "Download config directory")
- [Download public directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/main/public "Download public directory")

#### Usage

It is recommended to look at examples [here](https://github.com/kebasyaty/ramifice/tree/v0/examples "here").

```python
import re
import asyncio
from typing import Any
from datetime import datetime
import pprint

from pymongo import AsyncMongoClient
from ramifice import (
    NamedTuple,
    model,
    translations,
    Migration,
)
from ramifice.fields import (
    ImageField,
    PasswordField,
    TextField,
)
from ramifice.utils.tools import to_human_size


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
                gettext("Maximum size: %s") % to_human_size(524288),
            ],
        )
        self.username = TextField(
            label=gettext("Username"),
            maxlength=150,
            required=True,
            unique=True,
            warning=[
                gettext("Allowed chars: %s") % "a-z A-Z 0-9 _",
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
            err.update("username", gettext("Allowed chars: %s") % "a-z A-Z 0-9 _")

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
        pprint.pprint(user_details)
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

#### How to create custom translations ?

```python
from ramifice import translations

translations.add_languages(
    default_locale="en",  # For Ramifice by default = "en"
    languages=frozenset(("en", "ru")),  # For Ramifice by default = ["en", "ru"]
)
```

```shell
cd project_name
# Add your custom translations:
uv run pybabel extract -o config/translations/custom.pot src
uv run pybabel init -i config/translations/custom.pot -d config/translations/custom -l en
uv run pybabel init -i config/translations/custom.pot -d config/translations/custom -l ru
...
# Hint: Do not forget to add translations for new languages.
uv run pybabel compile -d config/translations/custom

# Update your custom translations:
uv run pybabel extract -o config/translations/custom.pot src
uv run pybabel update -i config/translations/custom.pot -d config/translations/custom
# Hint: Do not forget to check the translations for existing languages.
uv run pybabel compile -d config/translations/custom
```

#### How to add new languages ​​to Ramifice ?

```python
from ramifice import translations

translations.add_languages(
    default_locale="en",  # For Ramifice by default = "en"
    languages=frozenset(("en", "ru", "de", "de_ch")),  # For Ramifice by default = ["en", "ru"]
)
```

```shell
cd project_name
# Example:
uv run pybabel init -i config/translations/ramifice.pot -d config/translations/ramifice -l de
uv run pybabel init -i config/translations/ramifice.pot -d config/translations/ramifice -l de_ch
...
# Hint: Do not forget to add translations for new languages.
uv run pybabel compile -d config/translations/ramifice

# Update translations to Ramifice:
uv run pybabel extract -o config/translations/ramifice.pot ramifice
uv run pybabel update -i config/translations/ramifice.pot -d config/translations/ramifice
# Hint: Do not forget to check the translations for existing languages.
uv run pybabel compile -d config/translations/ramifice
```

<hr>

<div align="center">
  <p align="center">
    <a href="https://github.com/kebasyaty/ramifice">
      <img
        height="100"
        alt="Logo"
        src="https://raw.githubusercontent.com/kebasyaty/ramifice/v2/assets/logo.svg">
    </a>
  </p>
  <p>
    <h1>ramifice</h1>
    <h3>ORM-pseudo-like API MongoDB for Python language.</h3>
    <p align="center">
      <a href="https://github.com/kebasyaty/ramifice/actions/workflows/test.yml" alt="Build Status"><img src="https://github.com/kebasyaty/ramifice/actions/workflows/test.yml/badge.svg" alt="Build Status"></a>
      <a href="https://kebasyaty.github.io/ramifice/" alt="Docs"><img src="https://img.shields.io/badge/docs-available-brightgreen.svg" alt="Docs"></a>
      <a href="https://pypi.python.org/pypi/ramifice/" alt="PyPI pyversions"><img src="https://img.shields.io/pypi/pyversions/ramifice.svg" alt="PyPI pyversions"></a>
      <a href="https://pypi.python.org/pypi/ramifice/" alt="PyPI status"><img src="https://img.shields.io/pypi/status/ramifice.svg" alt="PyPI status"></a>
      <a href="https://pypi.python.org/pypi/ramifice/" alt="PyPI version fury.io"><img src="https://badge.fury.io/py/ramifice.svg" alt="PyPI version fury.io"></a>
      <br>
      <a href="https://pyrefly.org/" alt="Types: Pyrefly"><img src="https://img.shields.io/badge/types-Pyrefly-FFB74D.svg" alt="Types: Pyrefly"></a>
      <a href="https://docs.astral.sh/ruff/" alt="Code style: Ruff"><img src="https://img.shields.io/badge/code%20style-Ruff-FDD835.svg" alt="Code style: Ruff"></a>
      <a href="https://pypi.org/project/ramifice"><img src="https://img.shields.io/pypi/format/ramifice" alt="Format"></a>
      <a href="https://pepy.tech/projects/ramifice"><img src="https://static.pepy.tech/badge/ramifice" alt="PyPI Downloads"></a>
      <a href="https://github.com/kebasyaty/ramifice/blob/v2/LICENSE" alt="GitHub license"><img src="https://img.shields.io/github/license/kebasyaty/ramifice" alt="GitHub license"></a>
    </p>
    <p align="center">
      Ramifice is built around <a href="https://pypi.org/project/pymongo/" alt="PyMongo">PyMongo</a>.
      <br>
      For simulate relationship Many-to-One and Many-to-Many,
      <br>
      a simplified alternative (Types of selective fields with dynamic addition of elements) is used.
      <br>
      The project is more concentrated for web development or for applications with a graphic interface.
    </p>
  </p>
</div>

##

<p>
  <b>Version 2.0</b>
  <br>
  <a href="https://github.com/kebasyaty/ramifice" alt="Project Status">
    <img src="https://raw.githubusercontent.com/kebasyaty/ramifice/v2/assets/project_status/pre-alpha.svg"
      alt="Project Status">
  </a>
</p>

<br>
<br>

[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
<br>
_Supports MongoDB 3.6, 4.0, 4.2, 4.4, 5.0, 6.0, 7.0, and 8.0._
<br>
_For more information see [PyMongo](https://pypi.org/project/pymongo/ "PyMongo")_.

<br>

[![Documentation](https://raw.githubusercontent.com/kebasyaty/ramifice/v2/assets/links/documentation.svg "Documentation")](https://kebasyaty.github.io/ramifice/ "Documentation")

[![Requirements](https://raw.githubusercontent.com/kebasyaty/ramifice/v2/assets/links/requirements.svg "Requirements")](https://github.com/kebasyaty/ramifice/blob/v2/REQUIREMENTS.md "Requirements")

## Installation

1. Install MongoDB (if not installed):<br>
   [![Fedora](https://img.shields.io/badge/Fedora-294172?style=for-the-badge&logo=fedora&logoColor=white)](https://github.com/kebasyaty/ramifice/blob/v2/assets/FEDORA_INSTALL_MONGODB.md)
   [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://github.com/kebasyaty/ramifice/blob/v2/assets/UBUNTU_INSTALL_MONGODB.md)
   [![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.mongodb.com/try/download/community)

2. Install system dependencies:

```shell
# Fedora:
sudo dnf install gettext
# Ubuntu:
sudo apt install gettext
# MacOS
brew install gettext
brew link gettext --force
# Windows:
https://mlocati.github.io/articles/gettext-iconv-windows.html
```

3. Install Ramifice in your project:

```shell
uv add ramifice
```

4. Add `config` and `public` directories in root of your project:<br>
   [Download config directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/v2/config "Download config directory")<br>
   [Download public directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/v2/public "Download public directory")

5. Run

```shell
# Run Development:
uv run python main.py
# Run Production:
uv run python -OOP main.py
```

## Usage

[![Examples](https://raw.githubusercontent.com/kebasyaty/ramifice/v2/assets/links/more-examples.svg "Examples")](https://github.com/kebasyaty/ramifice/tree/v2/examples "Examples")

```python
import re
import asyncio
from typing import Any
from datetime import datetime
from pprint import pprint as pp

from pymongo import AsyncMongoClient
from ramifice import (
    Migration,
    Model,
    Translations,
    fields,
    meta,
    to_human_size,
)
from ramifice import Translations as trans

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELDS


@model(service_name="Accounts")
class User:
    """Model of User."""

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
        required=True,
        unique=True,
        warning=[
            _("Allowed chars: {}").format("a-z A-Z 0-9 _"),
        ],
    )
    password = fields.PasswordField(
        label=_("Password"),
    )
    сonfirm_password = fields.PasswordField(
        label=_("Confirm password"),
        # If true, the value of this field is not saved in the database.
        ignored=True,
    )

    # Optional method
    async def add_validation(self) -> dict[str, Any]:
        """Additional validation of fields."""
        _ = self.custom_translator.gettext
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
            err_map.update("username", _("Allowed chars: {}").format("a-z A-Z 0-9 _"))

        return err_map


async def main():
    client = AsyncMongoClient()

    await Migration(
        database_name="test_db",
        mongo_client=client,
    ).migrate()


    user = User("ru")
    # user.avatar_funcs["from_path"]("public/media/default/no-photo.png")
    # user.avatar_funcs["from_base64"]("base64-string")
    user.username = "pythondev"
    user.password = "12345678"
    user.сonfirm_password = "12345678"

    # Create User.
    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    # Update User.
    user.username = "pythondev_123"
    if not await user.save():
        user.print_err()

    print("User details:")
    user_details = await User.find_one_to_raw_doc(
        # filter={"_id": user.id}
        # or
        filter={"username": user.username}
    )
    if user_details is not None:
        pp(user_details)
    else:
        print("No User!")

    # Close connection.
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
```

## Model Parameters

( only `service_name` is a required parameter )

<div>
   <table>
     <tr>
       <th align="left">Parameter</th>
       <th align="left">Default</th>
       <th align="left">Description</th>
     </tr>
     <tr>
       <td align="left">service_name</td>
       <td align="left">no</td>
       <td align="left"><b>Examples:</b> Accounts | Smartphones | Washing machines | etc ... </td>
     </tr>
     <tr>
       <td align="left">fixture_name</td>
       <td align="left">None</td>
       <td align="left">
         The name of the fixture in the <b>config/fixtures</b> directory (without extension).
         <br>
         <b>Examples:</b> SiteSettings | AppSettings | etc ...
       </td>
     </tr>
     <tr>
       <td align="left">db_query_docs_limit</td>
       <td align="left">1000</td>
       <td align="left">Limiting the number of request results.</td>
     </tr>
     <tr>
       <td align="left">is_create_doc</td>
       <td align="left">True</td>
       <td align="left">
         Can a Model create new documents in a collection?<br>
         Set to <b>False</b> if you only need one document in the collection and the Model is using a fixture.
       </td>
     </tr>
     <tr>
       <td align="left">is_update_doc</td>
       <td align="left">True</td>
       <td align="left">Can a Model update documents in a collection?</td>
     </tr>
     <tr>
       <td align="left">is_delete_doc</td>
       <td align="left">True</td>
       <td align="left">Can a Model remove documents from a collection?</td>
     </tr>
   </table>
</div>

<br>

**Example:**

```python
@meta(
    service_name="ServiceName",
    fixture_name="FixtureName",
    db_query_docs_limit=1000,
    is_create_doc = True,
    is_update_doc = True,
    is_delete_doc = True,
)
class User(Model):
  username = TextField(
      label="Username",
      required=True,
      unique=True,
  )
```

<br>

[![Changelog](https://raw.githubusercontent.com/kebasyaty/ramifice/v2/assets/links/changelog.svg "Changelog")](https://github.com/kebasyaty/ramifice/blob/v2/CHANGELOG.md "Changelog")

[![MIT](https://raw.githubusercontent.com/kebasyaty/ramifice/v2/assets/links/mit.svg "MIT")](https://github.com/kebasyaty/ramifice/blob/v2/MIT-LICENSE "MIT")

[![APACHE-2.0](https://raw.githubusercontent.com/kebasyaty/ramifice/v2/assets/links/apache-2.0.svg "GPL-3.0")](https://github.com/kebasyaty/ramifice/blob/v2/APACHE-2.0-LICENSE "APACHE-2.0")

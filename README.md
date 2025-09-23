<div align="center">
  <p align="center">
    <a href="https://github.com/kebasyaty/ramifice">
      <img
        height="60"
        alt="Logo"
        src="https://raw.githubusercontent.com/kebasyaty/ramifice/v0/assets/logo.svg">
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
      <a href="https://github.com/kebasyaty/ramifice/issues"><img src="https://img.shields.io/github/issues/kebasyaty/ramifice.svg" alt="GitHub issues"></a>
      <a href="https://pepy.tech/projects/ramifice"><img src="https://static.pepy.tech/badge/ramifice" alt="PyPI Downloads"></a>
      <a href="https://github.com/kebasyaty/ramifice/blob/main/LICENSE" alt="GitHub license"><img src="https://img.shields.io/github/license/kebasyaty/ramifice" alt="GitHub license"></a>
      <a href="https://mypy-lang.org/" alt="Types: Mypy"><img src="https://img.shields.io/badge/types-Mypy-202235.svg?color=0c7ebf" alt="Types: Mypy"></a>
      <a href="https://docs.astral.sh/ruff/" alt="Code style: Ruff"><img src="https://img.shields.io/badge/code%20style-Ruff-FDD835.svg" alt="Code style: Ruff"></a>
      <a href="https://github.com/kebasyaty/ramifice" alt="PyPI implementation"><img src="https://img.shields.io/pypi/implementation/ramifice" alt="PyPI implementation"></a>
      <br>
      <a href="https://pypi.org/project/ramifice"><img src="https://img.shields.io/pypi/format/ramifice" alt="Format"></a>
      <a href="https://github.com/kebasyaty/ramifice"><img src="https://img.shields.io/github/languages/top/kebasyaty/ramifice" alt="Top"></a>
      <a href="https://github.com/kebasyaty/ramifice"><img src="https://img.shields.io/github/repo-size/kebasyaty/ramifice" alt="Size"></a>
      <a href="https://github.com/kebasyaty/ramifice"><img src="https://img.shields.io/github/last-commit/kebasyaty/ramifice/main" alt="Last commit"></a>
      <a href="https://github.com/kebasyaty/ramifice/releases/" alt="GitHub release"><img src="https://img.shields.io/github/release/kebasyaty/ramifice" alt="GitHub release"></a>
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

[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
<br>
_Supports MongoDB 3.6, 4.0, 4.2, 4.4, 5.0, 6.0, 7.0, and 8.0._
<br>
_For more information see [PyMongo](https://pypi.org/project/pymongo/ "PyMongo")_.

## Documentation

Online browsable documentation is available at [https://kebasyaty.github.io/ramifice/](https://kebasyaty.github.io/ramifice/ "Documentation").

## Requirements

[View the list of requirements](https://github.com/kebasyaty/ramifice/blob/v0/REQUIREMENTS.md "Requirements").

## Installation

1. Install MongoDB (if not installed):<br>
   [![Fedora](https://img.shields.io/badge/Fedora-294172?style=for-the-badge&logo=fedora&logoColor=white)](https://github.com/kebasyaty/ramifice/blob/v0/assets/FEDORA_INSTALL_MONGODB.md)
   [![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://github.com/kebasyaty/ramifice/blob/v0/assets/UBUNTU_INSTALL_MONGODB.md)
   [![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.mongodb.com/try/download/community)

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

3. Add `config` and `public` directories in root of your project:<br>
   [Download config directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/main/config "Download config directory")
   [Download public directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/main/public "Download public directory")

## Usage

[It is recommended to look at examples here](https://github.com/kebasyaty/ramifice/tree/v0/examples "It is recommended to look at examples here").

```python
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
@model(
    service_name="ServiceName",
    fixture_name="FixtureName",
    db_query_docs_limit=1000,
    is_create_doc = True,
    is_update_doc = True,
    is_delete_doc = True,
)
class User:
    def fields(self):
        self.username = TextField(
            label=gettext("Username"),
            required=True,
            unique=True,
        )
```

## Class methods

_List of frequently used methods:_

```python
# Gets an estimate of the count of documents in a collection using collection metadata.
count: int = await User.estimated_document_count()

# Gets an estimate of the count of documents in a collection using collection metadata.
q_filter = {"first_name": "John"}
count: int = await User.count_documents(q_filter)

# Runs an aggregation framework pipeline.
from bson.bson import BSON
pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
    {"$sort": BSON([("count", -1), ("_id", -1)])},
]
docs = await User.aggregate(pipeline)

# Finds the distinct values for a specified field across a single collection.
q_filter = "key_name"
values = await User.distinct(q_filter)

# Get collection name.
name = await User.collection_name()

# The full name is of the form database_name.collection_name.
name = await User.collection_full_name()

# Get AsyncBatabase for the current Model.
database = await User.database()

# Get AsyncCollection for the current Model.
collection = await User.collection()

# Find a single document.
q_filter = {"email": "John_Smith@gmail.com"}
mongo_doc = await User.find_one(q_filter)

# Create object instance from Mongo document.
q_filter = {"email": "John_Smith@gmail.com"}
mongo_doc = await User.find_one(q_filter)
user = User.from_mongo_doc(mongo_doc)

# Find a single document and converting to raw document.
q_filter = {"email": "John_Smith@gmail.com"}
raw_doc = await User.find_one_to_raw_doc(q_filter)

# Find a single document and convert it to a Model instance.
q_filter = {"email": "John_Smith@gmail.com"}
user = await User.find_one_to_instance(q_filter)

# Find a single document and convert it to a JSON string.
q_filter = {"email": "John_Smith@gmail.com"}
json = await User.find_one_to_json(q_filter)

# Find a single document and delete it.
q_filter = {"email": "John_Smith@gmail.com"}
delete_result = await User.delete_one(q_filter)

# Find a single document and delete it, return original.
q_filter = {"email": "John_Smith@gmail.com"}
mongo_doc = await User.find_one_and_delete(q_filter)

# Find documents.
q_filter = {"first_name": "John"}
mongo_docs = await User.find_many(q_filter)

# Find documents and convert to a raw documents.
q_filter = {"first_name": "John"}
raw_docs = await User.find_many_to_raw_docs(q_filter)

# Find documents and convert to a json string.
q_filter = {"email": "John_Smith@gmail.com"}
json = await User.find_many_to_json(q_filter)

# Find documents matching with Model.
q_filter = {"email": "John_Smith@gmail.com"}
delete_result = await User.delete_many(q_filter)

# Creates an index on this collection.
from pymongo import ASCENDING
keys = [("email", ASCENDING)]
result: str = await User.create_index(keys, name="idx_email")

# Drops the specified index on this collection.
User.drop_index("idx_email")

# Create one or more indexes on this collection.
from pymongo import ASCENDING, DESCENDING
index_1 = IndexModel([("username", DESCENDING), ("email", ASCENDING)], name="idx_username_email")
index_2 = IndexModel([("first_name", DESCENDING)], name="idx_first_name")
result: list[str] = await User.create_indexes([index_1, index_2])

# Drops all indexes on this collection.
User.drop_index()

# Get information on this collection’s indexes.
result = await User.index_information()

# Get a cursor over the index documents for this collection.
async for index in await User.list_indexes():
    print(index)

# Units Management.
# Management for `choices` parameter in dynamic field types.
# Units are stored in a separate collection.
from ramifice import Unit
unit = Unit(
  field="field_name",  # The name of the dynamic field.
  title={"en": "Title", "ru": "Заголовок"},  # The name of the choice item.
  value="Some text ...",  # The value of the choice item.
                          # Hint: float | int | str
  is_delete=False, # True - if you need to remove the item of choice.
                   # by default = False (add item to choice)
)
await User.unit_manager(unit)
```

## Instance methods

_List of frequently used methods:_

```python
# Check data validity.
# The main use is to check data from web forms.
# It is also used to verify Models that do not migrate to the database.
user = User()
if not await user.is_valid():
    user.print_err()  # Convenient to use during development.

# Create or update document in database.
# This method pre-uses the `check` method.
user = User()
if not await user.save():
    user.print_err()  # Convenient to use during development.

# Delete document from database.
user = User()
await user.delete()
# or
await user.delete(remove_files=False)

# Verification, replacement and recoverang of password.
user = User()
await user.verify_password(password="12345678")
await user.update_password(  # + verify_password
  old_password="12345678",
  new_password="O2eA4GIr38KGGlS",
)
```

## General auxiliary methods

```python
from ramifice import to_human_size
from ramifice.utils.tools import (
    get_file_size,
    hash_to_obj_id,
    is_color,
    is_email,
    is_ip,
    is_mongo_id,
    is_password,
    is_phone,
    is_url,
    normal_email,
)

# Validate Password.
if is_password("12345678"):
    ...

# Validate Email address.
if await is_email("kebasyaty@gmail.com"):
    ...

# Normalizing email address.
# Use this before requeste to a database.
# For example, on the login page.
email: str | None = normal_email("kebasyaty@gmail.com")  # None, if not valid

# Validate URL address.
if is_url("https://www.google.com"):
    ...

# Validate IP address.
if is_ip("127.0.0.1"):
    ...

# Validate Color code.
if is_color("#000"):
    ...

# Validate Phone number.
if is_phone("+447986123456"):
    ...

# Validation of the Mongodb identifier.
if is_mongo_id("666f6f2d6261722d71757578"):
    ...

# Get ObjectId from hash string.
from bson.objectid import ObjectId
_id: ObjectId | None = hash_to_obj_id("666f6f2d6261722d71757578")

# Convert number of bytes to readable format.
size: str = to_human_size(2097152)  # => 2 MB

# Get file size in bytes.
path = "public/media/default/no_doc.odt"
size: int = get_file_size(path)  # => 9843
```

## Changelog

[View the change history](https://github.com/kebasyaty/ramifice/blob/v0/CHANGELOG.md "Changelog").

## License

This project is licensed under the [MIT](https://github.com/kebasyaty/ramifice/blob/main/LICENSE "MIT").

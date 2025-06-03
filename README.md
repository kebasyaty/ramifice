<div align="center">
  <p align="center">
    <a href="https://github.com/kebasyaty/ramifice">
      <img
        height="90"
        alt="Logo"
        src="https://raw.githubusercontent.com/kebasyaty/ramifice/v0/assets/logo.svg">
    </a>
  </p>
  <p>
    <h1>ramifice</h1>
    <h3>ORM-like API MongoDB for Python language.</h3>
    <p align="center">
      <a href="https://github.com/kebasyaty/ramifice/actions/workflows/test.yml" alt="Build Status"><img src="https://github.com/kebasyaty/ramifice/actions/workflows/test.yml/badge.svg" alt="Build Status"></a>
      <a href="https://kebasyaty.github.io/ramifice/" alt="Docs"><img src="https://img.shields.io/badge/docs-available-brightgreen.svg" alt="Docs"></a>
      <a href="https://pypi.python.org/pypi/ramifice/" alt="PyPI pyversions"><img src="https://img.shields.io/pypi/pyversions/ramifice.svg" alt="PyPI pyversions"></a>
      <a href="https://pypi.python.org/pypi/ramifice/" alt="PyPI status"><img src="https://img.shields.io/pypi/status/ramifice.svg" alt="PyPI status"></a>
      <a href="https://pypi.python.org/pypi/ramifice/" alt="PyPI version fury.io"><img src="https://badge.fury.io/py/ramifice.svg" alt="PyPI version fury.io"></a>
      <a href="https://pepy.tech/projects/ramifice"><img src="https://static.pepy.tech/badge/ramifice" alt="PyPI Downloads"></a>
      <a href="https://github.com/kebasyaty/ramifice/blob/main/LICENSE" alt="GitHub license"><img src="https://img.shields.io/github/license/kebasyaty/ramifice" alt="GitHub license"></a>
      <a href="https://github.com/kebasyaty/ramifice" alt="GitHub repository"><img src="https://img.shields.io/badge/--ecebeb?logo=github&logoColor=000000" alt="GitHub repository"></a>
    </p>
    <div align="center">
      Ramifice is built around <a href="https://pypi.org/project/pymongo/" alt="PyMongo">PyMongo</a>.
      <br>
      For simulate relationship Many-to-One and Many-to-Many,
      <br>
      a simplified alternative (Types of selective fields with dynamic addition of elements) is used.
      <br>
      The project is more concentrated for web development or for applications with a graphic interface.
    </div>
  </p>
</div>

##

[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
<br>
_Supports MongoDB 3.6, 4.0, 4.2, 4.4, 5.0, 6.0, 7.0, and 8.0._
<br>
_For more information see [PyMongo](https://pypi.org/project/pymongo/ "PyMongo")_.

<p>
  <a href="https://github.com/kebasyaty/ramifice" alt="Project Status">
    <img src="https://raw.githubusercontent.com/kebasyaty/ramifice/v0/assets/project_status/project-status-alpha.svg"
      alt="Project Status">
  </a>
</p>

## Documentation

Online browsable documentation is available at [https://kebasyaty.github.io/ramifice/](https://kebasyaty.github.io/ramifice/ "Documentation").

## Requirements

[View the list of requirements.](https://github.com/kebasyaty/ramifice/blob/v0/REQUIREMENTS.md "View the list of requirements.")

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
poetry add ramifice
```

3. Add the configuration and public directories to the root of your project:<br>
   [Download config directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/main/config "Download config directory")
   <br>
   [Download public directory](https://downgit.github.io/#/home?url=https://github.com/kebasyaty/ramifice/tree/main/public "Download public directory")

## Usage

It is recommended to look at examples [here](https://github.com/kebasyaty/ramifice/tree/v0/examples "here").

```python
import asyncio
import pprint
from datetime import datetime

from pymongo import AsyncMongoClient
from ramifice import model, translations
from ramifice.fields import DateField, EmailField, ImageField, PasswordField, TextField
from ramifice.migration import Monitor


@model(service_name="Accounts")
class User:
    def fields(self, gettext):
        # ngettext = translations.get_translator(
        #     translations.CURRENT_LOCALE).ngettext
        self.avatar = ImageField(
            label=gettext("Avatar"),
            default="public/media/default/no-photo.png",
            # Available 4 sizes from lg to xs or None.
            thumbnails={"lg": 480, "md": 240, "sm": 120, "xs": 60},
            # True is high quality and low performance.
            is_high_quality=True,
        )
        self.username = TextField(
            label=gettext("Username"),
            required=True,
            unique=True,
        )
        self.first_name = TextField(label=gettext("First name"), required=True)
        self.last_name = TextField(
            label=gettext("Last name"),
            required=True,
        )
        self.email = EmailField(
            label=gettext("Email"),
            required=True,
            unique=True,
        )
        self.birthday = DateField(label=gettext("Birthday"))
        self.password = PasswordField(label=gettext("Password"))
        self.сonfirm_password = PasswordField(
            label=gettext("Confirm password"),
            # If true, the value of this field is not saved in the database.
            ignored=True,
        )

    async def add_validation(self) -> dict[str, str]:
        """For additional validation of fields."""
        error_map: dict[str, str] = {}
        if self.password != self.сonfirm_password:
            error_map["password"] = "Passwords do not match!"
        return error_map


async def main():
    client = AsyncMongoClient()

    await Monitor(
        database_name="test_db",
        mongo_client=client,
    ).migrat()

    user = User()
    user.username.value = "pythondev"
    user.avatar.from_path("public/media/default/no-photo.png")
    user.first_name.value = "John"
    user.last_name.value = "Smith"
    user.email.value = "John_Smith@gmail.com"
    user.birthday.value = datetime(2000, 1, 25)
    user.password.value = "12345678"
    user.сonfirm_password.value = "12345678"

    if not await user.save():
        # Convenient to use during development.
        user.print_err()

    doc_count = await User.estimated_document_count()
    print(f"Document count: {doc_count}")  # => 1

    print("User details:")
    user_details = await User.find_one_to_raw_doc({"_id": user._id.value})
    pprint.pprint(user_details)

    # await user.delete()
    # doc_count = await User.estimated_document_count()
    # print(f"Document count: {doc_count}")  # => 0

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
```

### [See more examples here.](https://github.com/kebasyaty/ramifice/tree/v0/examples "See more examples here.")

## Model Parameters

See the documentation [here](https://kebasyaty.github.io/ramifice/ "here").

###### ( only `service_name` is a required parameter )

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
       <td align="left">no</td>
       <td align="left">
         The name of the fixture in the <b>config/fixtures</b> directory (without extension).
         <br>
         <b>Examples:</b> SiteSettings | AppSettings | etc ...
       </td>
     </tr>
     <tr>
       <td align="left">db_query_docs_limit</td>
       <td align="left">1000</td>
       <td align="left">limiting query results.</td>
     </tr>
     <tr>
       <td align="left">is_migrat_model</td>
       <td align="left">True</td>
       <td align="left">
         Set to <b>False</b> if you do not need to migrate the Model to the database.<br>
         This can be use to validate a web forms - Search form, Contact form, etc.
       </td>
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
    is_migrat_model=True,
    is_create_doc = True,
    is_update_doc = True,
    is_delete_doc = True,
)
class User:
    def fields(self, gettext):
        self.username = TextField(
            label=gettext("Username"),
            required=True,
            unique=True,
        )
```

## Contributing

1. Fork it (<https://github.com/kebasyaty/ramifice/fork>)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## Install for development of Ramifice

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
poetry install --with dev docs
```

## Contributors

- [kebasyaty](https://github.com/kebasyaty) Gennady Kostyunin - creator and maintainer

## Changelog

[View the change history.](https://github.com/kebasyaty/ramifice/blob/v0/CHANGELOG.md "Changelog")

## License

**This project is licensed under the** [MIT](https://github.com/kebasyaty/ramifice/blob/main/LICENSE "MIT")**.**

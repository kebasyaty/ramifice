"""Accounts."""

from ramifice import model, translations
from ramifice.fields import (
    EmailField,
    TextField,
)


@model(service_name="Accounts")
class User:
    """Model of User."""

    def fields(self) -> None:
        """For adding fields."""
        # For custom translations.
        gettext = translations.gettext

        self.username = TextField(
            label=gettext("Username"),
            required=True,
            unique=True,
        )
        self.email = EmailField(
            label=gettext("Email"),
            required=True,
            unique=True,
        )

    # Optional method.
    async def pre_create(self) -> None:
        """Called before a new document is created in the database."""
        print("!!!-pre_create-!!!")

    # Optional method.
    async def post_create(self) -> None:
        """Called after a new document has been created in the database."""
        print("!!!-post_create-!!!")

    # Optional method.
    async def pre_update(self) -> None:
        """Called before updating an existing document in the database."""
        print("!!!-pre_update-!!!")

    # Optional method.
    async def post_update(self) -> None:
        """Called after an existing document in the database is updated."""
        print("!!!-post_update-!!!")

    # Optional method.
    async def pre_delete(self) -> None:
        """Called before deleting an existing document in the database."""
        print("!!!-pre_delete-!!!")

    # Optional method.
    async def post_delete(self) -> None:
        """Called after an existing document in the database has been deleted."""
        print("!!!-post_delete-!!!")

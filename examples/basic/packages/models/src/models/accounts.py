"""Accounts."""

from ramifice import model, translations
from ramifice.fields import (
    DateField,
    EmailField,
    PasswordField,
    TextField,
)


@model(service_name="Accounts")
class User:
    """Model of User."""

    def fields(self) -> None:
        """For adding fields."""
        # For custom translations.
        gettext = translations.gettext
        # ngettext = translations.ngettext
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

    # Optional method.
    async def add_validation(self) -> dict[str, str]:
        """Additional validation of fields."""
        gettext = translations.gettext
        error_map: dict[str, str] = {}

        # Get clean data.
        id = self.id.value
        password = self.password.value
        сonfirm_password = self.сonfirm_password.value

        if id is None and (password != сonfirm_password):
            error_map["password"] = gettext("Passwords do not match!")
        return error_map

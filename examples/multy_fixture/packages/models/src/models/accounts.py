"""Accounts."""

from ramifice import model, translations
from ramifice.fields import (
    BooleanField,
    DateField,
    EmailField,
    FileField,
    ImageField,
    PasswordField,
    TextField,
)


@model(
    service_name="Accounts",
    fixture_name="User",  # config\fixtures\User.yml
)
class User:
    """Model of User."""

    def fields(self) -> None:
        """For adding fields."""
        # For custom translations.
        gettext = translations.gettext
        ngettext = translations.ngettext
        self.avatar = ImageField(
            label=gettext("Avatar"),
            default="public/media/default/no-photo.png",
            # Available 4 sizes from lg to xs or None.
            # Hint: By default = None
            thumbnails={"lg": 512, "md": 256, "sm": 128, "xs": 64},
            # True - high quality and low performance for thumbnails.
            # Hint: By default = False
            high_quality=True,
            # The maximum size of the original image in bytes.
            # Hint: By default = 2 MB
            max_size=524288,  # 0.5 MB = 524288 Bytes (in binary)
        )
        self.resume = FileField(
            label=gettext("Resume"),
            default="public/media/default/no_doc.odt",
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
        self.is_admin = BooleanField(
            label=gettext("Is Administrator?"),
        )

    # Optional method.
    async def add_validation(self) -> dict[str, str]:
        """Additional validation of fields."""
        gettext = translations.gettext
        error_map: dict[str, str] = {}
        if self.password != self.сonfirm_password:
            error_map["password"] = gettext("Passwords do not match!")
        return error_map

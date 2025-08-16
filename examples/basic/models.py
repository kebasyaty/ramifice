"""Models."""

import re

from ramifice import NamedTuple, model, translations, to_human_size
from ramifice.fields import (
    BooleanField,
    DateField,
    DateTimeField,
    EmailField,
    ImageField,
    PasswordField,
    PhoneField,
    SlugField,
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
            placeholder=gettext("Upload your photo"),
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
                gettext("Maximum size: %s") % to_human_size(524288),
            ],
        )
        self.username = TextField(
            label=gettext("Username"),
            placeholder=gettext("Enter your username"),
            maxlength=150,
            required=True,
            unique=True,
            warning=[
                gettext("Allowed chars: %s") % "a-z A-Z 0-9 _",
            ],
        )
        self.first_name = TextField(
            label=gettext("First name"),
            placeholder=gettext("Enter your First name"),
            multi_language=True,  # Support for several language.
            maxlength=150,
            required=True,
        )
        self.last_name = TextField(
            label=gettext("Last name"),
            placeholder=gettext("Enter your Last name"),
            multi_language=True,  # Support for several language.
            maxlength=150,
            required=True,
        )
        self.email = EmailField(
            label=gettext("Email"),
            placeholder=gettext("Enter your email"),
            required=True,
            unique=True,
        )
        self.phone = PhoneField(
            label=gettext("Phone number"),
            placeholder=gettext("Enter your phone number"),
            unique=True,
        )
        self.birthday = DateField(
            label=gettext("Birthday"),
            placeholder=gettext("Enter your date of birth"),
        )
        self.description = TextField(
            label=gettext("About yourself"),
            placeholder=gettext("Tell us a little about yourself ..."),
            multi_language=True,  # Support for several language.
        )
        self.password = PasswordField(
            label=gettext("Password"),
            placeholder=gettext("Enter your password"),
        )
        self.сonfirm_password = PasswordField(
            label=gettext("Confirm password"),
            placeholder=gettext("Repeat your password"),
            # If true, the value of this field is not saved in the database.
            ignored=True,
        )
        self.is_admin = BooleanField(
            label=gettext("Is Administrator?"),
            warning=[
                gettext("Can this user access the admin panel?"),
            ],
        )
        self.is_active = BooleanField(
            label=gettext("Is active?"),
            warning=[
                gettext("Is this an active account?"),
            ],
        )
        self.slug = SlugField(
            label=gettext("Slug"),
            slug_sources=["username"],
            disabled=True,
            hide=True,
        )
        self.last_login = DateTimeField(
            label=gettext("Last login"),
            disabled=True,
            hide=True,
            warning=[
                gettext("Date and time of user last login."),
            ],
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

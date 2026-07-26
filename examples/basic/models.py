"""Models."""

import re
from ramifice import (
    Model,
    NamedTuple,
    Translator,
    fields,
    meta,
    to_human_size,
)

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(service_name="Accounts")
class User(Model):
    """Model of User."""

    avatar = fields.ImageField(
        label=_("Avatar"),
        placeholder=_("Upload your photo"),
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
            _("Maximum size: {}").format(to_human_size(524288)),
        ],
    )
    username = fields.TextField(
        label=_("Username"),
        placeholder=_("Enter your username"),
        max_length=150,
        required=True,
        unique=True,
        warning=[
            _("Allowed characters: {}").format("a-z A-Z 0-9 _"),
            _("Maximum length: {}").format(150),
        ],
    )
    first_name = fields.TextField(
        label=_("First name"),
        placeholder=_("Enter your First name"),
        is_multilingual=True,  # Support for several language.
        max_length=150,
        required=True,
        warning=[
            _("Maximum length: {}").format(150),
        ],
    )
    last_name = fields.TextField(
        label=_("Last name"),
        placeholder=_("Enter your Last name"),
        is_multilingual=True,  # Support for several language.
        max_length=150,
        required=True,
        warning=[
            _("Maximum length: {}").format(150),
        ],
    )
    email = fields.EmailField(
        label=_("Email"),
        placeholder=_("Enter your email"),
        required=True,
        unique=True,
    )
    phone = fields.PhoneField(
        label=_("Phone number"),
        placeholder=_("Enter your phone number"),
        unique=True,
    )
    birthday = fields.DateField(
        label=_("Birthday"),
        placeholder=_("Enter your date of birth"),
    )
    description = fields.TextField(
        label=_("About yourself"),
        placeholder=_("Tell us a little about yourself ..."),
        is_multilingual=True,  # Support for several language.
    )
    password = fields.PasswordField(
        label=_("Password"),
        placeholder=_("Enter your password"),
    )
    confirm_password = fields.PasswordField(
        label=_("Confirm password"),
        placeholder=_("Repeat your password"),
        # If true, the value of this field is not saved in the database.
        ignored=True,
    )
    is_admin = fields.BooleanField(
        label=_("Is Administrator?"),
        warning=[
            _("Can this user access the admin panel?"),
        ],
    )
    is_active = fields.BooleanField(
        label=_("Is active?"),
        warning=[
            _("Is this an active account?"),
        ],
    )
    slug = fields.SlugField(
        label=_("Slug"),
        slug_sources=["username"],
        disabled=True,
        hide=True,
    )
    last_login = fields.DateTimeField(
        label=_("Last login"),
        disabled=True,
        hide=True,
        warning=[
            _("Date and time of user last login."),
        ],
    )

    # Optional method
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        _ = self._CUSTOM_TRANSLATOR.gettext
        err_map = self.get_error_map()

        username = self.username
        id = self.id
        password = self.password
        confirm_password = self.confirm_password

        # Check username
        if username is not None and re.match(r"^[a-zA-Z0-9_]+$", username) is None:
            err_map.update("username", _("Allowed characters: {}").format("a-z A-Z 0-9 _"))

        # Check password
        if id is None and password != confirm_password:
            err_map.update("password", _("Passwords do not match!"))

        return err_map

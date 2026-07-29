"""Models."""

import re

from pymongo import ASCENDING

from ramifice import (
    Model,
    NamedTuple,
    Translator,
    fields,
    meta,
)

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELD


@meta(service_name="Accounts")
class User(Model):
    """User Model."""

    username = fields.TextField(
        label=_("Username"),
        placeholder=_("Enter your username"),
        max_length=150,
        is_require=True,
        is_unique=True,
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
        is_require=True,
        warning=[
            _("Maximum length: {}").format(150),
        ],
    )
    last_name = fields.TextField(
        label=_("Last name"),
        placeholder=_("Enter your Last name"),
        is_multilingual=True,  # Support for several language.
        max_length=150,
        is_require=True,
        warning=[
            _("Maximum length: {}").format(150),
        ],
    )
    email = fields.EmailField(
        label=_("Email"),
        placeholder=_("Enter your email"),
        is_require=True,
        is_unique=True,
    )

    # Optional method
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        _ = self._CUSTOM_TRANSLATOR.gettext
        err_map = self.get_error_map()
        username = self.username
        # Check username
        if username is not None and re.match(r"^[a-zA-Z0-9_]+$", username) is None:
            err_map.update("username", _("Allowed characters: {}").format("a-z A-Z 0-9 _"))

        return err_map

    # Optional method
    @classmethod
    async def indexing(cls) -> None:
        """To set up and start indexing."""
        await cls.create_index(
            [("username", ASCENDING)],
            name="username_Idx",
        )
        await cls.create_index(
            [("email", ASCENDING)],
            name="email_Idx",
        )

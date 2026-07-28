"""Models."""

import logging

from ramifice import (
    Model,
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
        is_require=True,
        is_unique=True,
    )
    email = fields.EmailField(
        label=_("Email"),
        is_require=True,
        is_unique=True,
    )

    # Optional method
    async def pre_create(self) -> None:
        """Called before a new document is created in the database."""
        logging.info("!!!-pre_create-!!!")

    # Optional method
    async def post_create(self) -> None:
        """Called after a new document has been created in the database."""
        logging.info("!!!-post_create-!!!")

    # Optional method
    async def pre_update(self) -> None:
        """Called before updating an existing document in the database."""
        logging.info("!!!-pre_update-!!!")

    # Optional method
    async def post_update(self) -> None:
        """Called after an existing document in the database is updated."""
        logging.info("!!!-post_update-!!!")

    # Optional method
    async def pre_delete(self) -> None:
        """Called before deleting an existing document in the database."""
        logging.info("!!!-pre_delete-!!!")

    # Optional method
    async def post_delete(self) -> None:
        """Called after an existing document in the database has been deleted."""
        logging.info("!!!-post_delete-!!!")

"""Migration are `Ramifice` way of
propagating changes you make to
your models (add or delete a Model, add or delete a field in Model, etc.) into
your database schema.
"""  # noqa: D205

from __future__ import annotations

__all__ = ("Migration",)

import logging
from datetime import datetime
from typing import Any

from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection
from termcolor import colored

from ramifice.models.model import Model
from ramifice.utils import constants
from ramifice.utils.constants import UTC_TIMEZONE
from ramifice.utils.errors import (
    DoesNotMatchRegexError,
    NoModelsForMigrationError,
    PanicError,
)
from ramifice.utils.fixtures import apply_fixture

logger = logging.getLogger(__name__)


class Migration:
    """Migration of models to database."""

    def __init__(self, database_name: str, mongo_client: AsyncMongoClient) -> None:  # noqa: D107
        constants.DEBUG = False
        #
        db_name_regex = constants.REGEX["database_name"]
        if db_name_regex.match(database_name) is None:
            regex_str: str = "^[a-zA-Z][-_a-zA-Z0-9]{0,59}$"
            msg: str = f"Does not match the regular expression: {regex_str}"
            logger.critical(msg)
            raise DoesNotMatchRegexError(regex_str)
        #
        constants.DATABASE_NAME = database_name
        constants.MONGO_CLIENT = mongo_client
        constants.MONGO_DATABASE = constants.MONGO_CLIENT[constants.DATABASE_NAME]
        # Get Model list.
        self.model_list: list[Any] = Model.__subclasses__()
        # Raise the exception if there are no models for migration.
        if len(self.model_list) == 0:
            logger.critical("No Models for Migration!")
            raise NoModelsForMigrationError()

    async def reset(self) -> None:
        """Reset the condition of the models in a super collection.

        Switch the `is_model_exist` parameter in the condition `False`.
        """
        # Get access to super collection.
        # (Contains Model state and dynamic field data.)
        super_collection: AsyncCollection = constants.MONGO_DATABASE[constants.SUPER_COLLECTION_NAME]
        # Switch the `is_model_exist` parameter in `False`.
        async for model_state in super_collection.find():
            q_filter = {"collection_name": model_state["collection_name"]}
            update = {"$set": {"is_model_exist": False}}
            await super_collection.update_one(q_filter, update)

    async def model_state(self, metadata: dict[str, Any]) -> dict[str, Any]:
        """Get the state of the current model from a super collection."""
        # Get access to super collection.
        # (Contains Model state and dynamic field data.)
        super_collection: AsyncCollection = constants.MONGO_DATABASE[constants.SUPER_COLLECTION_NAME]
        # Get state of current Model.
        model_state: dict[str, Any] | None = await super_collection.find_one(
            {"collection_name": metadata["collection_name"]},
        )
        if model_state is not None:
            model_state["is_model_exist"] = True
        else:
            # Create a state for new Model.
            model_state = {
                "collection_name": metadata["collection_name"],
                "field_name_and_type": metadata["field_name_and_type"],
                "data_dynamic_fields": metadata["data_dynamic_fields"],
                "is_model_exist": True,
            }
            await super_collection.insert_one(model_state)
        return model_state

    def new_fields(self, metadata: dict[str, Any], model_state: dict[str, Any]) -> list[str]:
        """Get a list of new fields that were added to Model."""
        new_fields: list[str] = []
        for field_name, field_type in metadata["field_name_and_type"].items():
            old_field_type: str | None = model_state["field_name_and_type"].get(field_name)
            if old_field_type is None or old_field_type != field_type:
                new_fields.append(field_name)
        return new_fields

    async def napalm(self) -> None:
        """Delete data for non-existent Models from a super collection,
        delete collections associated with those Models.
        """  # noqa: D205
        # Get access to database.
        database = constants.MONGO_DATABASE
        # Get access to super collection.
        # (Contains Model state and dynamic field data.)
        super_collection: AsyncCollection = constants.MONGO_DATABASE[constants.SUPER_COLLECTION_NAME]
        # Delete data for non-existent Models.
        async for model_state in super_collection.find():
            if model_state["is_model_exist"] is False:
                # Get the name of the collection associated with the Model.
                collection_name = model_state["collection_name"]
                # Delete data for non-existent Model.
                await super_collection.delete_one({"collection_name": collection_name})
                # Delete collection associated with non-existent Model.
                await database.drop_collection(collection_name)  # type: ignore[union-attr]

    async def migrate(self) -> None:
        """Run migration process.

        1) Update the state of Models in the super collection.
        2) Register new Models in the super collection.
        3) Check changes in models and (if necessary) apply in appropriate collections.
        """
        # Reset the condition of the models in a super collection.
        # Switch the `is_model_exist` parameter in the condition `False`.
        await self.reset()
        # Get access to database.
        database = constants.MONGO_DATABASE
        # Get access to super collection.
        super_collection: AsyncCollection = database[constants.SUPER_COLLECTION_NAME]
        #
        for cls_model in self.model_list:
            # Get metadata of current Model.
            metadata = cls_model.META
            # Get the state of the current model from a super collection.
            model_state = await self.model_state(metadata)
            # Review change of fields in the current Model and (if necessary)
            # update documents in the appropriate Collection.
            if model_state["field_name_and_type"] != metadata["field_name_and_type"]:
                # Get a list of new fields.
                new_fields: list[str] = self.new_fields(metadata, model_state)
                # Get collection for current Model.
                model_collection: AsyncCollection = database[model_state["collection_name"]]
                # Add new fields with default value or
                # update existing fields whose field type has changed.
                async for mongo_doc in model_collection.find():
                    for field_name in new_fields:
                        field_type = metadata["field_name_and_type"].get(field_name)
                        if field_type is not None:
                            if field_type == "FileField":
                                file_info = {
                                    "path": "",
                                    "is_delete": True,
                                    "save_as_is": False,
                                }
                                mongo_doc[field_name] = file_info
                            elif field_type == "ImageField":
                                img_info = {
                                    "path": "",
                                    "is_delete": True,
                                    "save_as_is": False,
                                }
                                mongo_doc[field_name] = img_info
                            else:
                                mongo_doc[field_name] = None
                    #
                    inst_model = cls_model.from_mongo_doc(mongo_doc)
                    result_check: dict[str, Any] = await inst_model.check(
                        is_save=True,
                        collection=model_collection,
                        is_migration_process=True,
                    )
                    if not result_check["is_valid"]:
                        print(colored("\n!!!>>MIGRATION<<!!!", "red", attrs=["bold"]))  # noqa: T201
                        inst_model.print_err()
                        msg: str = "Migration failed."
                        logger.critical(msg)
                        raise PanicError(msg)
                    # Get checked data.
                    checked_data = result_check["data"]
                    # Add password from mongo_doc to checked_data.
                    for field_name, field_type in metadata["field_name_and_type"].items():
                        if (
                            field_type == "PasswordField"
                            and model_state["field_name_and_type"].get(field_name) == "PasswordField"
                        ):
                            checked_data[field_name] = mongo_doc[field_name]
                    # Update date and time.
                    checked_data["updated_at"] = datetime.now(UTC_TIMEZONE)
                    # Update the document in the database.
                    await model_collection.replace_one(
                        filter={"_id": checked_data["_id"]},
                        replacement=checked_data,
                    )
            #
            # Refresh the dynamic fields data for the current model.
            for field_name, field_data in metadata["data_dynamic_fields"].items():
                if model_state["data_dynamic_fields"].get(field_name, False) == False:  # noqa: E712
                    model_state["data_dynamic_fields"][field_name] = field_data
                else:
                    metadata["data_dynamic_fields"][field_name] = model_state["data_dynamic_fields"][field_name]
            # Refresh state of current Model.
            model_state["data_dynamic_fields"] = metadata["data_dynamic_fields"]
            model_state["field_name_and_type"] = metadata["field_name_and_type"]
            await super_collection.replace_one(
                filter={"collection_name": model_state["collection_name"]},
                replacement=model_state,
            )
        #
        # Block the verification code.
        constants.DEBUG = False
        #
        # Delete data for non-existent Models from a
        # super collection and delete collections associated with those Models.
        await self.napalm()
        # Run indexing and apply fixture to current Model.
        for cls_model in self.model_list:
            # Run indexing.
            await cls_model.indexing()
            # Apply fixture to current Model.
            fixture_name: str | None = cls_model.META["fixture_name"]
            if fixture_name is not None:
                collection: AsyncCollection = constants.MONGO_DATABASE[cls_model.META["collection_name"]]
                if await collection.estimated_document_count() == 0:
                    await apply_fixture(
                        fixture_name=fixture_name,
                        cls_model=cls_model,
                        collection=collection,
                    )

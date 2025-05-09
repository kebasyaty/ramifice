"""Migration are `Ramifice` way of
propagating changes you make to
your models (add or delete a Model, add or delete a field in Model, etc.) into
your database schema.
"""

from datetime import datetime
from typing import Any

from pymongo import AsyncMongoClient
from pymongo.asynchronous.collection import AsyncCollection
from termcolor import colored

from . import store
from .errors import DoesNotMatchRegexError, NoModelsForMigrationError, PanicError
from .model import Model
from .tools import apply_fixture
from .types import CheckResult, FileData, ImageData


class Monitor:
    """Monitoring and updating database state for application."""

    def __init__(self, database_name: str, mongo_client: AsyncMongoClient):
        store.DEBUG = False
        #
        db_name_regex = store.REGEX["database_name"]
        if db_name_regex.match(database_name) is None:
            raise DoesNotMatchRegexError("^[a-zA-Z][-_a-zA-Z0-9]{0,59}$")
        #
        store.DATABASE_NAME = database_name
        store.MONGO_CLIENT = mongo_client
        store.MONGO_DATABASE = store.MONGO_CLIENT[store.DATABASE_NAME]
        # Get Model list.
        self.model_list: list[Any] = [
            model for model in Model.__subclasses__() if model.META["is_migrat_model"]
        ]
        # Raise the exception if there are no models for migration.
        if len(self.model_list) == 0:
            raise NoModelsForMigrationError()

    async def reset(self) -> None:
        """Reset the condition of the models in a super collection.
        Switch the `is_model_exist` parameter in the condition `False`.
        """
        # Get access to super collection.
        super_collection: AsyncCollection = store.MONGO_DATABASE[store.SUPER_COLLECTION_NAME]  # type: ignore[index]
        # Switch the `is_model_exist` parameter in `False`.
        async for model_state in super_collection.find():
            q_filter = {"collection_name": model_state["collection_name"]}
            update = {"$set": {"is_model_exist": False}}
            await super_collection.update_one(q_filter, update)

    async def model_state(self, metadata: dict[str, Any]) -> dict[str, Any]:
        """Get the state of the current model from a super collection."""
        # Get access to super collection.
        super_collection: AsyncCollection = store.MONGO_DATABASE[store.SUPER_COLLECTION_NAME]  # type: ignore[index]
        # Get state of current Model.
        model_state = await super_collection.find_one(
            {"collection_name": metadata["collection_name"]}
        )
        if model_state is not None:
            model_state["is_model_exist"] = True
        else:
            # Create a state for new Model.
            model_state = {
                "collection_name": metadata["collection_name"],
                "field_name_and_type_list": metadata["field_name_and_type_list"],
                "data_dynamic_fields": metadata["data_dynamic_fields"],
                "is_model_exist": True,
            }
            await super_collection.insert_one(model_state)
        return model_state

    def new_fields(
        self, metadata: dict[str, Any], model_state: dict[str, Any]
    ) -> list[str]:
        """Get a list of new fields that were added to Model."""
        new_fields: list[str] = []
        for field_name, field_type in metadata["field_name_and_type_list"].items():
            old_field_type: str | None = model_state["field_name_and_type_list"].get(
                field_name
            )
            if old_field_type is None or old_field_type != field_type:
                new_fields.append(field_name)
        return new_fields

    async def napalm(self) -> None:
        """Delete data for non-existent Models from a super collection,
        delete collections associated with those Models.
        """
        # Get access to database.
        database = store.MONGO_DATABASE
        # Get access to super collection.
        super_collection: AsyncCollection = store.MONGO_DATABASE[store.SUPER_COLLECTION_NAME]  # type: ignore[index]
        # Delete data for non-existent Models.
        async for model_state in super_collection.find():
            if model_state["is_model_exist"] is False:
                # Get the name of the collection associated with the Model.
                collection_name = model_state["collection_name"]
                # Delete data for non-existent Model.
                await super_collection.delete_one({"collection_name": collection_name})
                # Delete collection associated with non-existent Model.
                await database.drop_collection(collection_name)  # type: ignore[union-attr]

    async def migrat(self) -> None:
        """Run migration process:
        1) Update the state of Models in the super collection.
        2) Register new Models in the super collection.
        3) Check changes in models and (if necessary) apply in appropriate collections.
        """
        # Reset the condition of the models in a super collection.
        # Switch the `is_model_exist` parameter in the condition `False`.
        await self.reset()
        # Get access to database.
        database = store.MONGO_DATABASE
        # Get access to super collection.
        super_collection: AsyncCollection = database[store.SUPER_COLLECTION_NAME]  # type: ignore[index]
        #
        for cls_model in self.model_list:
            # Get metadata of current Model.
            metadata = cls_model.META
            # Get the state of the current model from a super collection.
            model_state = await self.model_state(metadata)
            # Review change of fields in the current Model and (if necessary)
            # update documents in the appropriate Collection.
            if (
                model_state["field_name_and_type_list"]
                != metadata["field_name_and_type_list"]
            ):
                # Get a list of new fields.
                new_fields: list[str] = self.new_fields(metadata, model_state)
                # Get collection for current Model.
                model_collection: AsyncCollection = database[model_state["collection_name"]]  # type: ignore[index]
                # Add new fields with default value or
                # update existing fields whose field type has changed.
                async for mongo_doc in model_collection.find():
                    for field_name in new_fields:
                        field_type = metadata["field_name_and_type_list"].get(
                            field_name
                        )
                        if field_type is not None:
                            if field_type == "FileField":
                                file = FileData()
                                file.is_delete = True
                                mongo_doc[field_name] = file.to_dict()
                            elif field_type == "ImageField":
                                img = ImageData()
                                img.is_delete = True
                                mongo_doc[field_name] = img.to_dict()
                            else:
                                mongo_doc[field_name] = None
                    #
                    inst_model = cls_model.from_doc(mongo_doc)
                    result_check: CheckResult = await inst_model.check(
                        is_save=True, collection=model_collection
                    )
                    if not result_check.is_valid:
                        print(colored("\n!!!>>MIGRATION<<!!!", "red", attrs=["bold"]))
                        inst_model.print_err()
                        raise PanicError("Migration failed.")
                    # Get checked data.
                    checked_data = result_check.data
                    # Add password from mongo_doc to checked_data.
                    for field_name, field_type in metadata[
                        "field_name_and_type_list"
                    ].items():
                        if (
                            field_type == "PasswordField"
                            and model_state["field_name_and_type_list"].get(field_name)
                            == "PasswordField"
                        ):
                            checked_data[field_name] = mongo_doc[field_name]
                    # Update date and time.
                    checked_data["updated_at"] = datetime.now()
                    # Update the document in the database.
                    await model_collection.replace_one(
                        filter={"_id": checked_data["_id"]}, replacement=checked_data
                    )
            #
            # Refresh the dynamic fields data for the current model.
            meta_dyn_field_list: list[str] = metadata["data_dynamic_fields"].keys()
            for field_name, field_data in model_state["data_dynamic_fields"].items():
                field_type = metadata["field_name_and_type_list"].get(field_name)
                if field_type is not None and field_name in meta_dyn_field_list:
                    model_state["field_name_and_type_list"][field_name] = field_type
                    metadata["data_dynamic_fields"][field_name] = field_data
            #
            model_state["data_dynamic_field"] = metadata["data_dynamic_fields"]
            model_state["field_name_and_type_list"] = metadata[
                "field_name_and_type_list"
            ]
            # Refresh state of current Model.
            await super_collection.replace_one(
                filter={"collection_name": model_state["collection_name"]},
                replacement=model_state,
            )
        #
        # Block the verification code.
        store.DEBUG = False
        #
        # Delete data for non-existent Models from a
        # super collection and delete collections associated with those Models.
        await self.napalm()
        # Run indexing and apply fixture to current Model.
        for cls_model in self.model_list:
            # Run indexing.
            cls_model.indexing()
            # Apply fixture to current Model.
            fixture_name: str | None = cls_model.META["fixture_name"]
            if fixture_name is not None:
                collection: AsyncCollection = store.MONGO_DATABASE[  # type: ignore[index, attr-defined]
                    cls_model.META["collection_name"]
                ]
                if collection.estimated_document_count() == 0:
                    await apply_fixture(
                        fixture_name=fixture_name,
                        collection=collection,
                    )

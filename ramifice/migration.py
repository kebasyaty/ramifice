"""Migration are `Ramifice` way of
propagating changes you make to
your models (add or delete a Model, add or delete a field in Model, etc.) into
your database schema.
"""

from typing import Any

from pymongo import AsyncMongoClient

from . import store
from .errors import DoesNotMatchRegexError, NoModelsForMigrationError
from .model import Model


class Monitor:
    """Monitoring and updating database state for application."""

    def __init__(self, database_name: str, mongo_client: AsyncMongoClient):
        store.DEBUG = False
        db_name_regex = store.REGEX["database_name"]
        if db_name_regex.match(database_name) is None:
            raise DoesNotMatchRegexError("^[a-zA-Z][-_a-zA-Z0-9]{0,59}$")
        #
        store.DATABASE_NAME = database_name
        store.MONGO_CLIENT = mongo_client
        store.MONGO_DATABASE = store.MONGO_CLIENT[store.DATABASE_NAME]

    async def reset(self) -> None:
        """Reset the condition of the models in a super collection.
        Switch the `is_model_exist` parameter in the condition `False`.
        """
        # Get access to super collection.
        super_collection = store.MONGO_DATABASE[store.SUPER_COLLECTION_NAME]  # type: ignore
        # Switch the `is_model_exist` parameter in `False`.
        async for model_state in super_collection.find():
            q_filter = {"collection_name": model_state["collection_name"]}
            update = {"$set": {"is_model_exist": False}}
            super_collection.update_one(q_filter, update)

    async def state(self, metadata: dict[str, Any]) -> dict[str, Any]:
        """Get the state of the current model from a super collection."""
        # Get access to super collection.
        super_collection = store.MONGO_DATABASE[store.SUPER_COLLECTION_NAME]  # type: ignore
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

    async def napalm(self) -> None:
        """Delete data for non-existent Models from a super collection,
        delete collections associated with those Models.
        """
        # Get access to database.
        database = store.MONGO_DATABASE  # type: ignore
        # Get access to super collection.
        super_collection = store.MONGO_DATABASE[store.SUPER_COLLECTION_NAME]  # type: ignore
        # Delete data for non-existent Models.
        async for model_state in super_collection.find():
            if model_state["is_model_exist"] is False:
                # Get the name of the collection associated with the Model.
                collection_name = model_state["collection_name"]
                # Delete data for non-existent Model.
                await super_collection.delete_one({"collection_name": collection_name})
                # Delete collection associated with non-existent Model.
                await database.drop_collection(collection_name)  # type: ignore

    async def migrat(self) -> None:
        """Run migration process:
        1) Update the state of Models in the super collection.
        2) Register new Models in the super collection.
        3) Check changes in models and (if necessary) apply in appropriate collections.
        """
        # Get Model list.
        model_list = [
            model for model in Model.__subclasses__() if model.META["is_migrat_model"]
        ]
        # Raise the exception if there are no models for migration.
        if len(model_list) == 0:
            raise NoModelsForMigrationError()
        # Reset the condition of the models in a super collection.
        # Switch the `is_model_exist` parameter in the condition `False`.
        await self.reset()
        # Get access to database.
        database = store.MONGO_DATABASE  # type: ignore
        # Get access to super collection.
        super_collection = database[store.SUPER_COLLECTION_NAME]  # type: ignore
        #
        for model_class in model_list:
            # Get metadata of current Model.
            metadata = model_class.META
            # Get the state of the current model from a super collection.
            model_state = await self.state(metadata)

"""Migration are `Ramifice` way of
propagating changes you make to
your models (add or delete a Model, add or delete a field in Model, etc.) into
your database schema.
"""

from pymongo import AsyncMongoClient

from . import errors, store


class ModelState:
    """For control state of Model in the super collection."""

    def __init__(self):
        self.collection_name = ""
        self.field_name_and_type_list = {}
        self.data_dynamic_fields = {}
        self.model_exists = False


class Monitor:
    """Monitoring and updating database state for application."""

    def __init__(self, database_name: str, mongo_client: AsyncMongoClient):
        db_name_regex = store.REGEX.get("database_name")
        if db_name_regex.match(database_name) is None:  # type: ignore
            raise errors.DoesNotMatchRegexError("^[a-zA-Z][-_a-zA-Z0-9]{0,59}$")
        #
        store.DATABASE_NAME = database_name
        store.MONGO_CLIENT = mongo_client
        store.MONGO_DATABASE = store.MONGO_CLIENT[store.DATABASE_NAME]

    async def refresh(self) -> None:
        """Get access to the super collection.
        Super collection contains data of Models state and dynamic field data.
        """
        super_collection = store.MONGO_DATABASE[store.SUPER_COLLECTION_NAME]  # type: ignore
        # Update model_exists for ModelState in super collection.
        async for model_state_doc in super_collection.find():
            q_filter = {"collection_name": model_state_doc.get("collection_name")}
            update = {"$set": {"model_exists": False}}
            super_collection.update_one(q_filter, update)

    async def napalm(self) -> None:
        """Delete data for non-existent Models from a super collection,
        delete collections associated with those Models.
        """
        # Get database of application.
        database = store.MONGO_DATABASE  # type: ignore
        # Get super collection.
        super_collection = store.MONGO_DATABASE[store.SUPER_COLLECTION_NAME]  # type: ignore
        # Delete data for non-existent Models.
        async for model_state_doc in super_collection.find():
            if not model_state_doc.get("model_exists"):
                # Get the name of the collection associated with the Model.
                model_collection_name = model_state_doc.get("collection_name")
                # Delete data for non-existent Model.
                await super_collection.delete_one(
                    {"collection_name": model_collection_name}
                )
                # Delete collection associated with non-existent Model.
                await database.drop_collection(model_collection_name)  # type: ignore

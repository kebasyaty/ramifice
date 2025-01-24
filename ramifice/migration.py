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
        if db_name_regex is not None and db_name_regex.match(database_name) is None:
            raise errors.DoesNotMatchRegexError("^[a-zA-Z][-_a-zA-Z0-9]{0,59}$")
        #
        store.DATABASE_NAME = database_name
        store.MONGO_CLIENT = mongo_client
        store.MONGO_DATABASE = store.MONGO_CLIENT[store.DATABASE_NAME]

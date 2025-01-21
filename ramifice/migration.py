"""Migration are `Ramifice` way of
propagating changes you make to
your models (add or delete a Model, add or delete a field in Model, etc.) into
your database schema.
"""


class ModelState:
    """For control state of Model in the super collection."""

    def __init__(self):
        self.collection_name = ""
        self.field_name_and_type_list = {}
        self.data_dynamic_fields = {}
        self.model_exists = False


class Monitor:
    """Monitoring and updating database state for application."""

    def __init__(self, database_name: str):
        pass

"""For converting Python classes into Ramifice Model."""

from bson.objectid import ObjectId

from .fields import DateTimeField, HashField


class Model:
    """For converting Python classes into Ramifice Model."""

    def __init__(self):
        self.__hash = HashField(
            label="Document ID", hide=True, ignored=True, disabled=True
        )
        self.__created_at = DateTimeField(
            label="Created at",
            warning=["When the document was created."],
            hide=True,
            disabled=True,
        )
        self.__updated_at = DateTimeField(
            label="Updated at",
            warning=["When the document was updated."],
            hide=True,
            disabled=True,
        )

    @property
    def hash(self):
        """Document ID"""
        return self.__hash

    @property
    def created_at(self):
        """When the document was created"""
        return self.__created_at

    @property
    def updated_at(self):
        """When the document was updated"""
        return self.__updated_at

    def model_name(self) -> str:
        """Get Model name - Class name."""
        return self.__class__.__name__

    def full_model_name(self) -> str:
        """Get full Model name - Module name + . + Class name."""
        cls = self.__class__
        return f"{cls.__module__}.{cls.__name__}"

    def object_id(self) -> ObjectId | None:
        """Get ObjectId from field `hash`."""
        value = self.__hash.value
        return ObjectId(value) if value else None

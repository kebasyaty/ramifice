"""For converting Python classes into Ramifice Model."""

from typing import Any

from bson.objectid import ObjectId

from .fields import DateTimeField, HashField
from .tools import MixinJSON


class Model(MixinJSON):
    """For converting Python classes into Ramifice Model."""

    META: dict[str, Any] = {}

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
        MixinJSON.__init__(self)
        self.inject()

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

    # --------------------------------------------------------------------------
    def model_name(self) -> str:
        """Get Model name - Class name."""
        return self.__class__.__name__

    def full_model_name(self) -> str:
        """Get full Model name - module_name + __ + ClassName."""
        cls = self.__class__
        return f"{cls.__module__}__{cls.__name__}"

    # --------------------------------------------------------------------------
    def object_id(self) -> ObjectId | None:
        """Get ObjectId from field `hash`."""
        value = self.__hash.value
        return ObjectId(value) if value else None

    # --------------------------------------------------------------------------
    def inject(self) -> None:
        """Injecting metadata from Model.META in params of fields.
        Parameters: id, name, dynamic choices.
        """
        metadata = self.__class__.META
        if bool(metadata):
            field_attrs = metadata["field_attrs"]
            data_dynamic_fields = metadata["data_dynamic_fields"]
            for f_name, f_type in self.__dict__.items():
                f_name = f_name.rsplit("__", maxsplit=1)[-1]
                if not callable(f_type):
                    f_type.id = field_attrs[f_name]["id"]
                    f_type.name = field_attrs[f_name]["name"]
                    if "Dyn" in f_name:
                        f_type.choices = data_dynamic_fields[f_name]

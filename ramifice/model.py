"""For converting Python classes into Ramifice Model."""

import json
from typing import Any

from bson.objectid import ObjectId

from .extra import Extra
from .fields import DateTimeField, FileField, HashField, ImageField
from .paladins import CheckMixin
from .types import FileData, ImageData


class Model(Extra, CheckMixin):
    """For converting Python classes into Ramifice Model."""

    META: dict[str, Any] = {}

    def __init__(self):
        self.hash = HashField(
            label="Document ID", hide=True, ignored=True, disabled=True
        )
        self.created_at = DateTimeField(
            label="Created at",
            warning=["When the document was created."],
            hide=True,
            disabled=True,
        )
        self.updated_at = DateTimeField(
            label="Updated at",
            warning=["When the document was updated."],
            hide=True,
            disabled=True,
        )
        super().__init__()
        self.inject()

    def model_name(self) -> str:
        """Get Model name - Class name."""
        return self.__class__.__name__

    def full_model_name(self) -> str:
        """Get full Model name - module_name + . + ClassName."""
        cls = self.__class__
        return f"{cls.__module__}.{cls.__name__}"

    # --------------------------------------------------------------------------
    def to_obj_id(self) -> ObjectId | None:
        """Get ObjectId from field `hash`."""
        value = self.hash.value
        return ObjectId(value) if bool(value) else None

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
                if not callable(f_type):
                    f_type.id = field_attrs[f_name]["id"]
                    f_type.name = field_attrs[f_name]["name"]
                    if "Dyn" in f_name:
                        f_type.choices = data_dynamic_fields[f_name]

    # Complect of methods for converting Model to JSON and back.
    # --------------------------------------------------------------------------
    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for name, data in self.__dict__.items():
            if not callable(data):
                json_dict[name] = data.to_dict()
        return json_dict

    def to_json(self) -> str:
        """Convert object instance to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        for name, data in json_dict.items():
            obj.__dict__[name] = obj.__dict__[name].__class__.from_dict(data)
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)

    def to_dict_only_value(self) -> dict[str, Any]:
        """Convert model.field.value (only the `value` attribute) to a dictionary."""
        json_dict: dict[str, Any] = {}
        for name, data in self.__dict__.items():
            if not callable(data):
                value = data.value
                if not hasattr(value, "to_dict"):
                    json_dict[name] = value
                else:
                    json_dict[name] = value.to_dict()
        return json_dict

    def to_json_only_value(self) -> str:
        """Convert model.field.value (only the `value` attribute) to a JSON string."""
        return json.dumps(self.to_dict_only_value())

    @classmethod
    def from_dict_only_value(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        for name, data in json_dict.items():
            field_data = obj.__dict__[name]
            if isinstance(field_data, FileField):
                obj.__dict__[name].value = (
                    FileData.from_dict(data) if bool(data) else None
                )
            elif isinstance(field_data, ImageField):
                obj.__dict__[name].value = (
                    ImageData.from_dict(data) if bool(data) else None
                )
            else:
                obj.__dict__[name].value = data
        return obj

    @classmethod
    def from_json_only_value(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict_only_value(json_dict)

    # --------------------------------------------------------------------------
    def refrash_fields(self, value_dict: dict[str, Any]) -> None:
        """Partial or complete update a value of fields."""
        for name, data in value_dict.items():
            field_data: Any | None = self.__dict__.get(name)
            if field_data is not None:
                if isinstance(field_data, FileField):
                    self.__dict__[name].value = (
                        FileData.from_dict(data) if bool(data) else None
                    )
                elif isinstance(field_data, ImageField):
                    self.__dict__[name].value = (
                        ImageData.from_dict(data) if bool(data) else None
                    )
                else:
                    self.__dict__[name].value = data

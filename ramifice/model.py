"""For converting Python classes into Ramifice Model."""

import copy
import json
from abc import ABCMeta, abstractmethod
from typing import Any

from bson.objectid import ObjectId

from .fields import DateTimeField, HashField
from .tools import date_parse, datetime_parse

_ID = HashField(
    label="Document ID",
    hide=True,
    disabled=True,
)
CREATED_AT = DateTimeField(
    label="Created at",
    warning=["When the document was created."],
    hide=True,
    disabled=True,
)
UPDATED_AT = DateTimeField(
    label="Updated at",
    warning=["When the document was updated."],
    hide=True,
    disabled=True,
)


class Model(metaclass=ABCMeta):
    """For converting Python classes into Ramifice Model."""

    META: dict[str, Any] = {}

    def __init__(self):
        self._id = copy.deepcopy(_ID)
        self.created_at = copy.deepcopy(CREATED_AT)
        self.updated_at = copy.deepcopy(UPDATED_AT)
        self.fields()
        self.inject()

    @abstractmethod
    def fields(self):
        pass

    def model_name(self) -> str:
        """Get Model name - Class name."""
        return self.__class__.__name__

    def full_model_name(self) -> str:
        """Get full Model name - module_name + . + ClassName."""
        cls = self.__class__
        return f"{cls.__module__}.{cls.__name__}"

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
                    if "Dyn" in f_type.field_type:
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

    # --------------------------------------------------------------------------
    def to_dict_only_value(self) -> dict[str, Any]:
        """Convert model.field.value (only the `value` attribute) to a dictionary."""
        json_dict: dict[str, Any] = {}
        for name, data in self.__dict__.items():
            if callable(data):
                continue
            value = data.value
            if value is not None:
                group = data.group
                if group == "date":
                    value = (
                        value.strftime("%Y-%m-%d")
                        if data.field_type == "DateField"
                        else value.strftime("%Y-%m-%d %H:%M:%S")
                    )
                elif group == "hash":
                    value = str(value)
                elif group == "pass":
                    value = None
            json_dict[name] = value
        return json_dict

    def to_json_only_value(self) -> str:
        """Convert model.field.value (only the `value` attribute) to a JSON string."""
        return json.dumps(self.to_dict_only_value())

    @classmethod
    def from_dict_only_value(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        for name, data in obj.__dict__.items():
            if callable(data):
                continue
            value = json_dict.get(name)
            if value is not None:
                group = data.group
                if group == "date":
                    value = (
                        date_parse(value)
                        if data.field_type == "DateField"
                        else datetime_parse(value)
                    )
                elif group == "hash":
                    value = ObjectId(value)
            obj.__dict__[name].value = value
        return obj

    @classmethod
    def from_json_only_value(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict_only_value(json_dict)

    def refrash_fields(self, only_value_dict: dict[str, Any]) -> None:
        """Partial or complete update a `value` of fields."""
        for name, data in self.__dict__.items():
            if callable(data):
                continue
            value = only_value_dict.get(name)
            if value is not None:
                group = data.group
                if group == "date":
                    value = (
                        date_parse(value)
                        if data.field_type == "DateField"
                        else datetime_parse(value)
                    )
                elif group == "hash":
                    value = ObjectId(value)
            self.__dict__[name].value = value

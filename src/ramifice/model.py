"""For converting Python classes into Ramifice Model."""

import copy
import json
from abc import ABCMeta, abstractmethod
from typing import Any

from babel.dates import format_date, format_datetime
from bson.objectid import ObjectId
from dateutil.parser import parse

from . import translations
from .fields import DateTimeField, IDField


class Model(metaclass=ABCMeta):
    """For converting Python classes into Ramifice Model."""

    META: dict[str, Any] = {}

    def __init__(self):  # noqa: D107
        _ = translations._
        self._id = IDField(
            label=_("Document ID"),
            placeholder=_("It is added automatically"),
            hint=_("It is added automatically"),
            hide=True,
            disabled=True,
        )
        self.created_at = DateTimeField(
            label=_("Created at"),
            placeholder=_("It is added automatically"),
            hint=_("It is added automatically"),
            warning=[_("When the document was created.")],
            hide=True,
            disabled=True,
        )
        self.updated_at = DateTimeField(
            label=_("Updated at"),
            placeholder=_("It is added automatically"),
            hint=_("It is added automatically"),
            warning=[_("When the document was updated.")],
            hide=True,
            disabled=True,
        )
        self.fields(translations.gettext)
        self.inject()

    @abstractmethod
    def fields(self, gettext):
        """For add fields."""
        pass

    def model_name(self) -> str:
        """Get Model name - Class name."""
        return self.__class__.__name__

    def full_model_name(self) -> str:
        """Get full Model name - module_name + . + ClassName."""
        cls = self.__class__
        return f"{cls.__module__}.{cls.__name__}"

    def inject(self) -> None:
        """Injecting metadata from Model.META in params of fields."""
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
        current_locale = translations.CURRENT_LOCALE
        for name, data in self.__dict__.items():
            if callable(data):
                continue
            value = data.value
            if value is not None:
                group = data.group
                if group == "date":
                    value = (
                        format_date(
                            date=value,
                            format="short",
                            locale=current_locale,
                        )
                        if data.field_type == "DateField"
                        else format_datetime(
                            datetime=value,
                            format="short",
                            locale=current_locale,
                        )
                    )
                elif group == "id":
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
                    value = parse(value)
                elif group == "id":
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
                    value = parse(value)
                elif group == "id":
                    value = ObjectId(value)
            self.__dict__[name].value = value

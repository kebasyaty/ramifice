"""For converting Python classes into Ramifice Model."""

import json
import os
import shutil
from abc import ABCMeta, abstractmethod
from typing import Any

from babel.dates import format_date, format_datetime
from bson.objectid import ObjectId
from dateutil.parser import parse

from . import translations
from .errors import PanicError
from .fields import IDField  # type: ignore[attr-defined]


class PseudoModel(metaclass=ABCMeta):
    """For convert the Python class into a pseudo model Ramifice.

    Used for a Model that do not migrate into the database.
    """

    META: dict[str, Any] = {}

    def __init__(self) -> None:  # noqa: D107
        self._id = IDField(
            label="Stub",
            placeholder="Stub",
            hint="Stub",
            hide=True,
            disabled=True,
        )
        self.fields()
        self.inject()

        for _, f_type in self.__dict__.items():
            if not callable(f_type) and f_type.group == "img":
                f_type.__dict__["add_width_height"] = True

    def __del__(self, remove_files: bool = True) -> None:  # noqa: D105
        # If the model is not migrated,
        # it must delete files and images in the destructor.
        if remove_files:
            for f_name, f_type in self.__dict__.items():
                if callable(f_type):
                    continue
                value = f_type.value
                if value is not None:
                    if f_type.group == "file":
                        value = value.get("path")
                        if value is not None:
                            os.remove(value)
                    elif f_type.group == "img":
                        value = value.get("imgs_dir_path")
                        if value is not None:
                            shutil.rmtree(value)

    @abstractmethod
    def fields(self) -> None:
        """For adding fields."""
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
            for f_name, f_type in self.__dict__.items():
                if callable(f_type):
                    continue
                f_type.id = field_attrs[f_name]["id"]
                f_type.name = field_attrs[f_name]["name"]
                if "Dyn" in f_type.field_type:
                    msg = (
                        f"Model: `{metadata['full_model_name']}` > "
                        + f"Field: `{f_name}` => "
                        + "Dynamic field only for a migrated Model."
                    )
                    raise PanicError(msg)

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

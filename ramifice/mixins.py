"""Complect of mixins."""

import json
from typing import Any


class JsonMixin:
    """Complect of methods for converting Fields to JSON and back."""

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for f_name, f_type in self.__dict__.items():
            if not callable(f_type):
                f_name = f_name.rsplit("__", maxsplit=1)[-1]
                json_dict[f_name] = f_type
        return json_dict

    def to_json(self) -> str:
        """Convert object instance to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        obj_dict = {key: val for key, val in obj.__dict__.items() if not callable(val)}
        for key, val in obj_dict.items():
            f_name = key.rsplit("__", maxsplit=1)[-1]
            obj.__dict__[key] = json_dict[f_name]
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)


class FileJsonMixin:
    """Complect of methods for converting FileField and ImageField to JSON and back."""

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for f_name, f_type in self.__dict__.items():
            if not callable(f_type):
                f_name = f_name.rsplit("__", maxsplit=1)[-1]
                if not hasattr(f_type, "to_dict"):
                    json_dict[f_name] = f_type
                else:
                    json_dict[f_name] = f_type.to_dict()
        return json_dict

    def to_json(self) -> str:
        """Convert object instance to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        obj_dict = {key: val for key, val in obj.__dict__.items() if not callable(val)}
        for key, val in obj_dict.items():
            f_name = key.rsplit("__", maxsplit=1)[-1]
            if f_name != "value":
                obj.__dict__[key] = json_dict[f_name]
            else:
                data = json_dict[f_name]
                obj.__dict__[key] = (
                    val.__class__.from_dict(data) if bool(data) else None
                )
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)


class ModelJsonMixin:
    """Complect of methods for converting Model to JSON and back."""

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for f_name, f_type in self.__dict__.items():
            if not callable(f_type):
                f_name = f_name.rsplit("__", maxsplit=1)[-1]
                json_dict[f_name] = f_type.to_dict()
        return json_dict

    def to_json(self) -> str:
        """Convert object instance to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        obj_dict = {key: val for key, val in obj.__dict__.items() if not callable(val)}
        for key, val in obj_dict.items():
            f_name = key.rsplit("__", maxsplit=1)[-1]
            obj.__dict__[key] = val.__class__.from_dict(json_dict[f_name])
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)

    def to_dict_only_value(self) -> dict[str, Any]:
        """Convert model.field.value (only the `value` attribute) to a dictionary."""
        json_dict: dict[str, Any] = {}
        for f_name, f_type in self.__dict__.items():
            if not callable(f_type):
                f_name = f_name.rsplit("__", maxsplit=1)[-1]
                value = f_type.value
                if not hasattr(value, "to_dict"):
                    json_dict[f_name] = value
                else:
                    json_dict[f_name] = value.to_dict()
        return json_dict

    def to_json_only_value(self) -> str:
        """Convert model.field.value (only the `value` attribute) to a JSON string."""
        return json.dumps(self.to_dict_only_value())

    @classmethod
    def from_dict_only_value(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        obj_dict = {key: val for key, val in obj.__dict__.items() if not callable(val)}
        for key, val in obj_dict.items():
            f_name = key.rsplit("__", maxsplit=1)[-1]
            if not val.group in ["file", "image"]:
                obj.__dict__[key].value = json_dict[f_name]
            else:
                data = json_dict[f_name]
                obj.__dict__[key].value = (
                    val.__class__.from_dict(data) if bool(data) else None
                )
        return obj

    @classmethod
    def from_json_only_value(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict_only_value(json_dict)

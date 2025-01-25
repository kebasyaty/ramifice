"""Complect of mixins."""

import json
from typing import Any


class JsonMixin:
    """Complect of methods for converting custom object to JSON and back to an object."""

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
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
        for f_name, f_type in obj.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                if not hasattr(f_type, "from_dict"):
                    obj.__dict__[f_name] = json_dict[f_name]
                else:
                    obj.__dict__[f_name] = f_type.from_dict(json_dict[f_name])
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)

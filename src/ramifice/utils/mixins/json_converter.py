"""Ramifice - JsonMixin - Contains the methods for converting Fields to JSON and back."""

__all__ = ("JsonMixin",)

from typing import Any

import orjson


class JsonMixin:
    """Ramifice - Contains the methods for converting Fields to JSON and back."""

    def to_dict(self) -> dict[str, Any]:
        """Ramifice - Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for name, data in self.__dict__.items():
            if not callable(data):
                json_dict[name] = data
        return json_dict

    def to_json(self) -> str:
        """Ramifice - Convert object instance to a JSON string."""
        return orjson.dumps(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Ramifice - Convert JSON string to a object instance."""
        obj = cls()
        for name, data in json_dict.items():
            obj.__dict__[name] = data
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Ramifice - Convert JSON string to a object instance."""
        json_dict = orjson.loads(json_str)
        return cls.from_dict(json_dict)

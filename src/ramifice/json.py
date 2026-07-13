# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""A mixin for converting models to a JSON string and back to a Model."""

from __future__ import annotations

__all__ = ("JsonMixin",)

from typing import Any

import orjson


class JsonMixin:
    """A mixin for converting Model to a JSON-string and back to a Model."""

    def to_dict(self) -> dict[str, Any]:
        """Convert Model instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for f_name, f_value in self.__dict__.items():
            if not callable(f_value):
                json_dict[f_name] = f_value
        return json_dict

    def to_json(self) -> str:
        """Convert Model instance to a JSON-string."""
        return orjson.dumps(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON-dictionary to a Model instance."""
        obj = cls()
        for f_name, f_value in json_dict.items():
            obj.__dict__[f_name] = f_value
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON-string to a Model instance."""
        json_dict = orjson.loads(json_str)
        return cls.from_dict(json_dict)

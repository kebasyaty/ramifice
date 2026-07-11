# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Converting Python classes into Ramifice Models."""

from __future__ import annotations

__all__ = ("Model",)


from typing import Any, ClassVar

import orjson
from babel.dates import format_date, format_datetime
from bson.objectid import ObjectId
from dateutil.parser import parse
from xloft import NamedTuple

from ramifice.fields import DateTimeField, IDField
from ramifice.utils import errors
from ramifice.utils import translations as trans


class Model:
    """Converting Python Class into Ramifice Model."""

    META: ClassVar[dict[str, Any]] = {}

    id = IDField(
        label=trans._("Document ID"),
        placeholder=trans._("It is added automatically"),
        hint=trans._("It is added automatically"),
        hide=True,
        disabled=True,
    )

    created_at = DateTimeField(
        label=trans._("Created at"),
        placeholder=trans._("It is added automatically"),
        hint=trans._("It is added automatically"),
        warning=[trans._("When the document was created.")],
        hide=True,
        disabled=True,
    )

    updated_at = DateTimeField(
        label=trans._("Updated at"),
        placeholder=trans._("It is added automatically"),
        hint=trans._("It is added automatically"),
        warning=[trans._("When the document was updated.")],
        hide=True,
        disabled=True,
    )

    def __init__(self) -> None:  # noqa: D107
        metadata = self.__class__.META

        assert bool(metadata), "No metadata"

        for f_name in metadata["all_descriptor_fields"]:
            tmp_name = f_name if f_name != "id" else "_id"
            self.__dict__[tmp_name] = None

        self.inject(metadata)

    def __delattr__(self, name: str) -> None:
        """Blocked Deleter."""
        raise errors.AttributeCannotBeDeleteError(name)

    def model_name(self) -> str:
        """Get Model name - Class name."""
        return self.__class__.__name__

    def full_model_name(self) -> str:
        """Get full Model name - module_name + . + ClassName."""
        cls = self.__class__
        return f"{cls.__module__}.{cls.__name__}"

    def inject(self, metadata: dict[str, Any]) -> None:
        """Update the state of dynamic fields from metadata of model."""
        lang = trans.CURRENT_LOCALE
        descriptor_fields = metadata["all_descriptor_fields"]
        data_dynamic_fields = metadata["data_dynamic_fields"]
        for f_name in descriptor_fields:
            f_html_attrs = self.__dict__[f"{f_name}_html_attrs"]
            if "Dyn" in f_html_attrs["field_type"]:
                dyn_data = data_dynamic_fields.get(f_name)
                if dyn_data is not None:
                    f_html_attrs["choices"] = [[item["value"], item["title"][lang]] for item in dyn_data]
                else:
                    # This is necessary for
                    # `paladins > refrash > RefrashMixin > refrash_from_db`.
                    f_html_attrs["choices"] = None

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
        return orjson.dumps(self.to_dict()).decode("utf-8")

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
        json_dict = orjson.loads(json_str)
        return cls.from_dict(json_dict)

    # --------------------------------------------------------------------------
    def to_dict_only_value(self) -> dict[str, Any]:
        """Convert model.field.value (only the `value` attribute) to a dictionary."""
        json_dict: dict[str, Any] = {}
        current_locale = trans.CURRENT_LOCALE
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
        return orjson.dumps(self.to_dict_only_value()).decode("utf-8")

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
        json_dict = orjson.loads(json_str)
        return cls.from_dict_only_value(json_dict)

    def refrash_fields_only_value(self, only_value_dict: dict[str, Any]) -> None:
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

    # --------------------------------------------------------------------------
    def get_clean_data(self) -> tuple[NamedTuple, NamedTuple]:
        """Get clean data."""
        clean_data: dict[str, Any] = {}
        error_map: dict[str, Any] = {}

        for name, data in self.__dict__.items():
            if not callable(data):
                clean_data[name] = data.value
                error_map[name] = None

        return (NamedTuple(**clean_data), NamedTuple(**error_map))

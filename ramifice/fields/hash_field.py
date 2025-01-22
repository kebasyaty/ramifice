"""Field of Model for enter identifier of document."""

import json

from bson.objectid import ObjectId

from .general.field import Field
from .general.text_group import TextGroup


class HashField(Field, TextGroup):
    """Field of Model for enter identifier of document."""

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="HashField",
            group="hash",
        )
        TextGroup.__init__(
            self,
            input_type="text",
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=unique,
        )

    def object_id(self) -> ObjectId | None:
        """Get ObjectId from parameter `value`."""
        value = self.value
        return ObjectId(value) if value else None

    def to_dict(self) -> dict[str, str | bool | list[str] | None]:
        """Convert fields to a dictionary."""
        json_dict: dict[str, str | bool | list[str] | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                json_dict[f_name] = f_type
        return json_dict

    def to_json(self):
        """Convert a dictionary of fields to a JSON string."""
        return json.dumps(self.to_dict())

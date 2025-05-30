"""Field of Model for enter identifier of document."""

import json
from typing import Any

from bson.objectid import ObjectId

from .. import translations
from .general.field import Field


class IDField(Field):
    """Field of Model for enter identifier of document.

    Attributes:
    input_type -- Input type for a web form field.
    placeholder -- Displays prompt text.
    required -- Required field.
    readonly -- Specifies that the field cannot be modified by the user.
    unique -- The unique value of a field in a collection.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        label: str = translations.gettext("Document ID"),
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = translations.gettext("Enter document ID"),
        warning: list[str] | None = None,
        placeholder: str = translations.gettext("Enter document ID"),
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ):

        if len(label) > 0:
            label = translations.gettext(label)
        if len(hint) > 0:
            hint = translations.gettext(hint)
        if len(placeholder) > 0:
            placeholder = translations.gettext(placeholder)
        if bool(warning):
            warning = [translations.gettext(item) for item in warning]

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="IDField",
            group="id",
        )

        self.input_type = "text"
        self.value: ObjectId | None = None
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique
        self.alerts: list[str] = []

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for name, data in self.__dict__.items():
            if not callable(data):
                if name == "value" and data is not None:
                    json_dict[name] = str(data)
                else:
                    json_dict[name] = data
        return json_dict

    def to_json(self) -> str:
        """Convert object instance to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        for name, data in json_dict.items():
            if name == "value" and data is not None:
                obj.__dict__[name] = ObjectId(data)
            else:
                obj.__dict__[name] = data
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)

"""Field of Model for enter date."""

import json
from datetime import datetime
from typing import Any

from ..store import DEBUG
from ..tools import date_parse
from .general.date_group import DateGroup
from .general.field import Field


class DateField(Field, DateGroup):
    """Field of Model for enter date."""

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-branches
    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: datetime | None = None,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        max_date: datetime | None = None,
        min_date: datetime | None = None,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="DateField",
            group="date",
        )
        DateGroup.__init__(
            self,
            input_type="date",
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=False,
            max_date=max_date,
            min_date=min_date,
        )

        if DEBUG:
            if max_date is not None:
                if not isinstance(max_date, datetime):
                    raise AssertionError("Parameter `max_date` - Not а `str` type!")
            if min_date is not None:
                if not isinstance(min_date, datetime):
                    raise AssertionError("Parameter `min_date` - Not а `str` type!")
            if max_date is not None and min_date is not None and max_date <= min_date:
                raise AssertionError(
                    "The `max_date` parameter should be more than the `min_date`!"
                )
            if default is not None:
                if not isinstance(default, datetime):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if max_date is not None and default > max_date:
                    raise AssertionError("Parameter `default` is more `max_date`!")
                if min_date is not None and default < min_date:
                    raise AssertionError("Parameter `default` is less `min_date`!")

        self.default = default

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for name, data in self.__dict__.items():
            if not callable(data):
                json_dict[name] = data if name != "value" else data.strftime("%Y-%m-%d")
        return json_dict

    def to_json(self) -> str:
        """Convert object instance to a JSON string."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Convert JSON string to a object instance."""
        obj = cls()
        for name, data in json_dict.items():
            obj.__dict__[name] = data
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)

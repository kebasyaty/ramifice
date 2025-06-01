"""Field of Model for enter date and time."""

import json
from datetime import datetime
from typing import Any

from babel.dates import format_datetime
from dateutil.parser import parse

from .. import translations
from ..store import DEBUG
from .general.date_group import DateGroup
from .general.field import Field


class DateTimeField(Field, DateGroup):
    """Field of Model for enter date and time."""

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

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="DateTimeField",
            group="date",
        )
        DateGroup.__init__(
            self,
            input_type="datetime",
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=False,
            max_date=max_date,
            min_date=min_date,
        )

        self.default = default

    def to_dict(self) -> dict[str, Any]:
        """Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        current_locale = translations.CURRENT_LOCALE
        for name, data in self.__dict__.items():
            if not callable(data):
                if name == "value" and data is not None:
                    json_dict[name] = format_datetime(
                        datetime=data,
                        format="short",
                        locale=current_locale,
                    )
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
                obj.__dict__[name] = parse(data)
            else:
                obj.__dict__[name] = data
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Convert JSON string to a object instance."""
        json_dict = json.loads(json_str)
        return cls.from_dict(json_dict)

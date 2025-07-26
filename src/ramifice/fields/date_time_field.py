"""Ramifice - Field of Model for enter date and time."""

__all__ = ("DateTimeField",)

import logging
from datetime import datetime
from typing import Any

import orjson
from babel.dates import format_datetime
from dateutil.parser import parse

from ramifice.fields.general.date_group import DateGroup
from ramifice.fields.general.field import Field
from ramifice.utils import constants, translations

logger = logging.getLogger(__name__)


class DateTimeField(Field, DateGroup):
    """Ramifice - Field of Model for enter date and time."""

    def __init__(  # noqa: D107
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
        if constants.DEBUG:
            try:
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
                if not isinstance(label, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if not isinstance(disabled, bool):
                    raise AssertionError("Parameter `disabled` - Not а `bool` type!")
                if not isinstance(hide, bool):
                    raise AssertionError("Parameter `hide` - Not а `bool` type!")
                if not isinstance(ignored, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(ignored, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(hint, str):
                    raise AssertionError("Parameter `hint` - Not а `str` type!")
                if warning is not None and not isinstance(warning, list):
                    raise AssertionError("Parameter `warning` - Not а `list` type!")
                if not isinstance(placeholder, str):
                    raise AssertionError("Parameter `placeholder` - Not а `str` type!")
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
            except AssertionError as err:
                logger.error(str(err))
                raise err

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
        """Ramifice - Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        current_locale = translations.CURRENT_LOCALE
        for name, value in self.__dict__.items():
            if not callable(value):
                if name == "value" and value is not None:
                    json_dict[name] = format_datetime(
                        datetime=value,
                        format="short",
                        locale=current_locale,
                    )
                else:
                    json_dict[name] = value
        return json_dict

    def to_json(self) -> str:
        """Ramifice - Convert object instance to a JSON string."""
        return orjson.dumps(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Ramifice - Convert JSON string to a object instance."""
        obj = cls()
        for name, value in json_dict.items():
            if name == "value" and value is not None:
                obj.__dict__[name] = parse(value)
            else:
                obj.__dict__[name] = value
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Ramifice - Convert JSON string to a object instance."""
        json_dict = orjson.loads(json_str)
        return cls.from_dict(json_dict)

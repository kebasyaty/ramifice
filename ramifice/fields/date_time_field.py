"""Field of Model for enter date and time."""

import json
from datetime import datetime

from ..errors import InvalidDateTimeError
from ..store import DEBUG
from ..tools import datetime_parse
from .general.date_group import DateGroup
from .general.field import Field


class DateTimeField(Field, DateGroup):
    """Field of Model for enter date and time.
    Formats: dd-mm-yyyy hh:mm:ss | dd/mm/yyyy hh:mm:ss | dd.mm.yyyy hh:mm:ss |
             dd-mm-yyyyThh:mm:ss | dd/mm/yyyyThh:mm:ss | dd.mm.yyyyThh:mm:ss |
             yyyy-mm-dd hh:mm:ss | yyyy/mm/dd hh:mm:ss | yyyy.mm.dd hh:mm:ss |
             yyyy-mm-ddThh:mm:ss | yyyy/mm/ddThh:mm:ss | yyyy.mm.ddThh:mm:ss
    """

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: str | None = None,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
        max_date: str | None = None,
        min_date: str | None = None,
    ):
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
            unique=unique,
            max_date=max_date,
            min_date=min_date,
        )

        if DEBUG:
            if max_date is not None:
                if not isinstance(max_date, str):
                    raise AssertionError("Parameter `max_date` - Not а `str` type!")
                if len(max_date) == 0:
                    raise AssertionError(
                        "The `max_date` parameter should not contain an empty string!"
                    )
                try:
                    datetime_parse(max_date)
                except InvalidDateTimeError:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        "Parameter `max_date` - Invalid date and time!"
                    )  # pylint: disable=raise-missing-from
            if min_date is not None:
                if not isinstance(min_date, str):
                    raise AssertionError("Parameter `min_date` - Not а `str` type!")
                if len(min_date) == 0:
                    raise AssertionError(
                        "The `min_date` parameter should not contain an empty string!"
                    )
                try:
                    datetime_parse(min_date)
                except InvalidDateTimeError:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        "Parameter `min_date` - Invalid date and time!"
                    )  # pylint: disable=raise-missing-from
            if (
                max_date is not None
                and min_date is not None
                and datetime_parse(max_date) <= datetime_parse(min_date)
            ):
                raise AssertionError(
                    "The `max_date` parameter should be more than the `min_date`!"
                )
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
                try:
                    datetime_parse(default)
                except InvalidDateTimeError:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        "Parameter `default` - Invalid date and time!"
                    )  # pylint: disable=raise-missing-from
                if max_date is not None and datetime_parse(default) > datetime_parse(
                    max_date
                ):
                    raise AssertionError("Parameter `default` is more `max_date`!")
                if min_date is not None and datetime_parse(default) < datetime_parse(
                    min_date
                ):
                    raise AssertionError("Parameter `default` is less `min_date`!")

        self.__default = default

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

    def to_datetime(self) -> datetime | None:
        """Convert parameter `value` or `default` into object of date and time."""
        value = self.value or self.__default or None
        return datetime_parse(value) if value is not None else None

    # --------------------------------------------------------------------------
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

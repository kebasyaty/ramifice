"""Field of Model for enter date."""

from datetime import datetime

from ..errors import InvalidDateError
from ..store import DEBUG
from ..tools import date_parse
from .general.date_group import DateGroup
from .general.field import Field


class DateField(Field, DateGroup):
    """Field of Model for enter date.
    Formats: dd-mm-yyyy | dd/mm/yyyy | dd.mm.yyyy |
             yyyy-mm-dd | yyyy/mm/dd | yyyy.mm.dd
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
            field_type="DateField",
            group="date",
        )
        DateGroup.__init__(
            self,
            input_type="date",
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
                    date_parse(max_date)
                except InvalidDateError:
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
                    date_parse(min_date)
                except InvalidDateError:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        "Parameter `min_date` - Invalid date and time!"
                    )  # pylint: disable=raise-missing-from
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
                try:
                    date_parse(default)
                except InvalidDateError:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        "Parameter `default` - Invalid date and time!"
                    )  # pylint: disable=raise-missing-from
                if max_date is not None and date_parse(default) > date_parse(max_date):
                    raise AssertionError("Parameter `default` is more `max_date`!")
                if min_date is not None and date_parse(default) < date_parse(min_date):
                    raise AssertionError("Parameter `default` is less `min_date`!")

        self.__default = default

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

    def to_datetime(self) -> datetime | None:
        """Convert parameter `value` or `default` into object of date and time."""
        value = self.value or self.__default or None
        return date_parse(value) if value is not None else None

"""Field of Model for enter date."""

from typing import Any
from ..errors import InvalidDateError
from ..globals.tools import date_parse
from .general.field import Field
from .general.date_group import DateGroup


class DateField(Field, DateGroup):
    """Field of Model for enter date.
    Formats: dd-mm-yyyy | dd/mm/yyyy | dd.mm.yyyy |
             yyyy-mm-dd | yyyy/mm/dd | yyyy.mm.dd
    """

    debug: bool = True
    meta: dict[str, Any] = {}

    def __init__(self,
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
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='DateField',
                       group='date',
                       )
        DateGroup.__init__(self,
                           input_type='date',
                           placeholder=placeholder,
                           required=required,
                           readonly=readonly,
                           unique=unique,
                           max_date=max_date,
                           min_date=min_date,
                           )

        if DateField.debug:
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError(
                        'Parameter `default` - Not а `str` type!')
                if len(default) == 0:
                    raise AssertionError(
                        'The `default` parameter should not contain an empty string!')
                try:
                    date_parse(default)
                except InvalidDateError:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        'Parameter `default` - Invalid date!')  # pylint: disable=raise-missing-from

        self.__default = default

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

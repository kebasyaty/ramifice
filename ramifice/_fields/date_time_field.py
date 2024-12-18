"""Field of Model for enter date and time."""

from typing import Any
from .general.field import Field
from .general.date_group import DateGroup


class DateTimeField(Field, DateGroup):
    """Field of Model for enter date and time.
    Formats: dd-mm-yyyy hh:mm:ss | dd/mm/yyyy hh:mm:ss | dd.mm.yyyy hh:mm:ss |
             dd-mm-yyyyThh:mm:ss | dd/mm/yyyyThh:mm:ss | dd.mm.yyyyThh:mm:ss |
             yyyy-mm-dd hh:mm:ss | yyyy/mm/dd hh:mm:ss | yyyy.mm.dd hh:mm:ss |
             yyyy-mm-ddThh:mm:ss | yyyy/mm/ddThh:mm:ss | yyyy.mm.ddThh:mm:ss
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
                       field_type='DateTimeField',
                       group='date',
                       )
        DateGroup.__init__(self,
                           input_type='datetime',
                           placeholder=placeholder,
                           required=required,
                           readonly=readonly,
                           unique=unique,
                           max_date=max_date,
                           min_date=min_date,
                           )
        self.__default = default

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

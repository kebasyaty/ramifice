"""Field of Model for enter date and time."""

from datetime import datetime

from ..errors import InvalidDateTimeError
from ..mixins import JsonMixin
from ..store import DEBUG
from ..tools import datetime_parse
from .general.date_group import DateGroup
from .general.field import Field


class DateTimeField(Field, DateGroup, JsonMixin):
    """Field of Model for enter date and time.
    Formats: dd-mm-yyyy hh:mm:ss | dd/mm/yyyy hh:mm:ss | dd.mm.yyyy hh:mm:ss |
             dd-mm-yyyyThh:mm:ss | dd/mm/yyyyThh:mm:ss | dd.mm.yyyyThh:mm:ss |
             yyyy-mm-dd hh:mm:ss | yyyy/mm/dd hh:mm:ss | yyyy.mm.dd hh:mm:ss |
             yyyy-mm-ddThh:mm:ss | yyyy/mm/ddThh:mm:ss | yyyy.mm.ddThh:mm:ss
    """

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
        JsonMixin.__init__(self)

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

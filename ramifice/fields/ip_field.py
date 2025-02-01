"""Field of Model for enter IP addresses."""

import ipaddress

from ..mixins import JsonMixin
from ..store import DEBUG
from .general.field import Field
from .general.text_group import TextGroup


class IPField(Field, TextGroup, JsonMixin):
    """Field of Model for enter IP addresses."""

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
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="IPField",
            group="text",
        )
        TextGroup.__init__(
            self,
            input_type="text",
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=unique,
        )
        JsonMixin.__init__(self)

        if DEBUG:
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
                try:
                    ipaddress.ip_address(default)
                except ValueError:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        "Parameter `default` - Invalid IP address!"
                    )  # pylint: disable=raise-missing-from

        self.default = default

    def __str__(self):
        return str(self.value)

    def is_valid(self, value: str | None = None) -> bool:
        """Validate IP address."""
        flag = True
        value = str(value or self.value or self.default)
        try:
            ipaddress.ip_address(value)
        except ValueError:
            flag = False
        return flag

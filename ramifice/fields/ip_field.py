"""Field of Model for enter IP address."""

import ipaddress

from .. import translations
from ..mixins import JsonMixin
from ..store import DEBUG
from .general.field import Field
from .general.text_group import TextGroup


class IPField(Field, TextGroup, JsonMixin):
    """Field of Model for enter IP address."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        label: str = translations.gettext("IP address"),
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = translations.gettext("Enter IP address"),
        warning: list[str] | None = None,
        default: str | None = None,
        placeholder: str = translations.gettext("Enter IP address"),
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ):
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

        self.default = default

    def is_valid(self, value: str | None = None) -> bool:
        """Validate IP address."""
        flag = True
        address = str(value or self.value or self.default)
        try:
            ipaddress.ip_address(address)
        except ValueError:
            flag = False
        return flag

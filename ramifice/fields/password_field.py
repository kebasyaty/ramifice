"""Field of Model for enter password."""

from ..mixins import JsonMixin
from ..store import REGEX
from .general.field import Field


class PasswordField(Field, JsonMixin):
    """Field of Model for enter password.
    WARNING:
    Default regular expression: ^[-._!"`'#%&,:;<>=@{}~$()*+/\\?[]^|a-zA-Z0-9]{8,256}$
    Valid characters by default: a-z A-Z 0-9 - . _ ! " ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |
    Number of characters by default: from 8 to 256.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        label: str = "",
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        placeholder: str = "",
        required: bool = False,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=False,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="PasswordField",
            group="pass",
        )
        JsonMixin.__init__(self)

        self.input_type = "password"
        self.value: str | None = None
        self.placeholder = placeholder
        self.required = required

    def __str__(self):
        return str(self.value)

    def is_valid(self, value: str | None = None) -> bool:
        """Validate Password."""
        flag = True
        value = str(value or self.value)
        if not REGEX["password"].match(value):
            flag = False
        return flag

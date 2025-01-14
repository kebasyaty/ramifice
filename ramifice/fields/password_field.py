"""Field of Model for enter password."""

from .general.field import Field


class PasswordField(Field):
    """Field of Model for enter password.
    WARNING:
    Default regular expression: ^[-._!"`'#%&,:;<>=@{}~$()*+/\\?[]^|a-zA-Z0-9]{8,256}$
    Valid characters by default: a-z A-Z 0-9 - . _ ! " ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |
    Number of characters by default: from 8 to 256.
    """

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
            group="password",
        )
        self.__input_type = "password"
        self.__value: str | None = None
        self.__placeholder = placeholder
        self.__required = required

    @property
    def input_type(self) -> str:
        """Input type for a web form field.
        Html tag: input type="password".
        """
        return self.__input_type

    # --------------------------------------------------------------------------
    @property
    def value(self) -> str | None:
        """Sets value of field."""
        return self.__value

    @value.setter
    def value(self, value: str | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def placeholder(self) -> str:
        """Displays prompt text."""
        return self.__placeholder

    # --------------------------------------------------------------------------
    @property
    def required(self) -> bool:
        """Required field."""
        return self.__required

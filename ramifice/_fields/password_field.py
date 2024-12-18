"""Field of Model for enter password."""

from typing import Any
from .general.field import Field


class PasswordField(Field):
    """Field of Model for enter password.
    WARNING:
    Default regular expression: ^[-._!"`'#%&,:;<>=@{}~$()*+/\\?[]^|a-zA-Z0-9]{8,256}$
    Valid characters by default: a-z A-Z 0-9 - . _ ! " ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |
    Number of characters by default: from 8 to 256.
    """

    debug: bool = True
    meta: dict[str, Any] = {}

    def __init__(self,
                 label: str = "",
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 placeholder: str = "",
                 required: bool = False,
                 regex: str = "",
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=False,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='PasswordField',
                       group='password',
                       )
        self.__input_type = 'password'
        self.__value: str | None = None
        self.__placeholder = placeholder
        self.__required = required
        self.__regex = regex

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
    # --------------------------------------------------------------------------

    @property
    def regex(self) -> str:
        """Regular expression to validate the `value`.
        Example: ^[a-zA-Z0-9_]{8,16}$
        """
        return self.__regex

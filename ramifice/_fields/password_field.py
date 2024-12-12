"""Field of Model for enter password."""

from .general import (field, password_group)


class PasswordField(field.Field, password_group.PasswordGroup):
    """Field of Model for enter password.
    WARNING:
    Default regular expression: ^[-._!"`'#%&,:;<>=@{}~$()*+/\\?[]^|a-zA-Z0-9]{8,256}$
    Valid characters by default: a-z A-Z 0-9 - . _ ! " ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |
    Number of characters by default: from 8 to 256.
    """

    def __init__(self,
                 label: str = "",
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 placeholder: str = '',
                 required: bool = False,
                 regex: str = '',
                 regex_err_msg: list[str] | None = None,
                 ):
        field.Field.__init__(self,
                             label=label,
                             disabled=False,
                             hide=hide,
                             ignored=ignored,
                             hint=hint,
                             warning=warning,
                             field_type='PasswordField',
                             group='password',
                             )
        password_group.PasswordGroup.__init__(self,
                                              input_type='password',
                                              placeholder=placeholder,
                                              required=required,
                                              )
        self.__regex = regex
        self.__regex_err_msg = regex_err_msg

    # --------------------------------------------------------------------------
    @property
    def regex(self) -> str:
        """Regular expression to validate the `value`.
        Example: ^[a-zA-Z0-9_]{8,16}$
        """
        return self.__regex

    # --------------------------------------------------------------------------
    @property
    def regex_err_msg(self) -> list[str] | None:
        """Error message.
        Example: ['Allowed chars: a-z, A-Z, 0-9, _',
                  'Number of characters: from 8 to 16.']
        """
        return self.__regex_err_msg

"""Field of Model for enter phone number."""

from .general.field import Field
from .general.text_group import TextGroup


class PhoneField(Field, TextGroup):
    """Field of Model for enter phone number.
    WARNING: By default is used validator `Valid.phone_number?`.
    Examples:
    4812504203260 | +4812504203260 |
    +48 504 203 260 | +48 (12) 504-203-260 |
    +48 (12) 504 203 260 | +48.504.203.260 |
    +48-504-203-260 | 555.5555.555
    """

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 default: str = "",
                 placeholder: str = "",
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 regex: str = "",
                 regex_err_msg: list[str] | None = None,
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='PhoneField',
                       group='text',
                       )
        TextGroup.__init__(self,
                           input_type='tel',
                           placeholder=placeholder,
                           required=required,
                           readonly=readonly,
                           unique=unique,
                           )
        self.__default = default
        self.__regex = regex
        self.__regex_err_msg = regex_err_msg

    @property
    def default(self) -> str:
        """Value by default."""
        return self.__default

    @property
    def regex(self) -> str:
        """Regular expression to validate the `value`.
        Example: "^.+$"
        """
        return self.__regex

    @property
    def regex_err_msg(self) -> list[str] | None:
        """Error message.
        Example: ['Invalid Phone']
        """
        return self.__regex_err_msg

"""Field of Model for enter IP addresses."""

from .general.field import Field
from .general.text_group import TextGroup


class IPField(Field, TextGroup):
    """Field of Model for enter IP addresses."""

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
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='IPField',
                       group='text',
                       )
        TextGroup.__init__(self,
                           input_type='text',
                           placeholder=placeholder,
                           required=required,
                           readonly=readonly,
                           unique=unique,
                           )
        self.__default = default

    @property
    def default(self) -> str:
        """Value by default."""
        return self.__default

"""Field of Model for enter URL addresses."""


from .general.field import Field
from .general.text_group import TextGroup


class URLField(Field, TextGroup):
    """Field of Model for enter URL addresses."""

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 default: str = '',
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 # Google Chrome: 2083
                 # Edge: 2083
                 # Internet Explorer: 2083
                 # Safari: 80 000
                 # Firefox: 65 536
                 maxlength: int = 2083,
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='URLField',
                       group='text',
                       )
        TextGroup.__init__(self,
                           input_type='url',
                           placeholder=placeholder,
                           required=required,
                           readonly=readonly,
                           unique=unique,
                           )
        self.__default = default
        self.__maxlength = maxlength

    @property
    def default(self) -> str:
        """Value by default."""
        return self.__default

    @property
    def maxlength(self) -> int:
        """Maximum allowed number of characters."""
        return self.__maxlength

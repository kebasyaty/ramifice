"""Field of Model for enter identifier of document."""

from .general.field import Field
from .general.text_group import TextGroup


class HashField(Field, TextGroup):
    """Field of Model for enter identifier of document."""

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 maxlength: int = 24,
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='HashField',
                       group='hash',
                       )
        TextGroup.__init__(self,
                           input_type='text',
                           placeholder=placeholder,
                           required=required,
                           readonly=readonly,
                           unique=unique,
                           )
        self.__maxlength = maxlength

    @property
    def maxlength(self) -> int:
        """Maximum allowed number of characters."""
        return self.__maxlength

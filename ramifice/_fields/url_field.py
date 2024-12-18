"""Field of Model for enter URL addresses."""

from typing import Any
from urllib.parse import urlparse
from .general.field import Field
from .general.text_group import TextGroup


class URLField(Field, TextGroup):
    """Field of Model for enter URL addresses."""

    debug: bool = True
    meta: dict[str, Any] = {}

    def __init__(self,
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
        if URLField.debug:
            if default is not None and default != '':
                if not isinstance(default, str):
                    raise AssertionError(
                        'Parameter `default` - Not а `str` type!')
                result = urlparse(default)
                if not result.scheme or not result.netloc:
                    raise AssertionError(
                        'Parameter `default` - Invalid URL address!')
            if not isinstance(maxlength, int):
                raise AssertionError(
                    'Parameter `maxlength` - Not а `int` type!')

        self.__default = default
        self.__maxlength = maxlength

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

    @property
    def maxlength(self) -> int:
        """Maximum allowed number of characters."""
        return self.__maxlength

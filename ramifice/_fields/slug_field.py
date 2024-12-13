"""Field of Model for automatic generation of string `slug`."""

from .general.field import Field
from .general.text_group import TextGroup


class SlugField(Field, TextGroup):
    """Field of Model for automatic generation of string `slug`.
    Convenient to use for Url addresses.
    """

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 placeholder: str = '',
                 readonly: bool = False,
                 slug_sources: list[str] = ['hash'],
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='SlugField',
                       group='slug',
                       )
        TextGroup.__init__(self,
                           input_type='text',
                           placeholder=placeholder,
                           required=False,
                           readonly=readonly,
                           unique=True,
                           )
        self.__slug_sources = slug_sources

    @property
    def slug_sources(self) -> list[str]:
        """Names of the fields whose contents will be used for the slug.
        The default is ['hash'].
        Examples: ['title'] | ['hash', 'username'] | ['email', 'first_name'],
        """
        return self.__slug_sources

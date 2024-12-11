"""Field of Model for automatic generation of string `slug`."""

from .general import (field, text_group)


class SlugField(field.Field, text_group.TextGroup):
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
                 # The default is ['hash'].
                 slug_sources: list[str] | None = None,
                 ):
        field.Field.__init__(self,
                             label=label,
                             disabled=disabled,
                             hide=hide,
                             ignored=ignored,
                             hint=hint,
                             warning=warning,
                             field_type='SlugField',
                             group='slug',
                             )
        text_group.TextGroup.__init__(self,
                                      input_type='text',
                                      default=['hash'],
                                      placeholder=placeholder,
                                      required=False,
                                      readonly=readonly,
                                      unique=True,
                                      )
        self.__slug_sources = slug_sources

    @property
    def slug_sources(self) -> list[str] | None:
        """Names of the fields whose contents will be used for the slug.
        The default is ['hash'].
        Examples: ['title'] | ['hash', 'username'] | ['email', 'first_name'],
        """
        return self.__slug_sources

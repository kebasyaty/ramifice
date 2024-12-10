"""A field of Model for entering a URL."""

from .general import (field, text_group)


class URLField(field.Field, text_group.TextGroup):
    """A field of Model for entering a URL."""

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
                 maxlength: int = 2083,
                 ):
        field.Field.__init__(self,
                             label=label,
                             disabled=disabled,
                             hide=hide,
                             ignored=ignored,
                             hint=hint,
                             warning=warning,
                             field_type='URLField',
                             group='text',
                             )
        text_group.TextGroup.__init__(self,
                                      input_type='url',
                                      default=default,
                                      placeholder=placeholder,
                                      required=required,
                                      readonly=readonly,
                                      unique=unique,
                                      )
        self.__maxlength = maxlength

    @property
    def maxlength(self) -> int:
        """The maximum number of characters allowed in the text."""
        return self.__maxlength

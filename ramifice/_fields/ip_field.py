"""Field of Model for enter IP addresses."""

from .general import (field, text_group)


class IPField(field.Field, text_group.TextGroup):
    """Field of Model for enter IP addresses."""

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
                 ):
        field.Field.__init__(self,
                             label=label,
                             disabled=disabled,
                             hide=hide,
                             ignored=ignored,
                             hint=hint,
                             warning=warning,
                             field_type='IPField',
                             group='text',
                             )
        text_group.TextGroup.__init__(self,
                                      input_type='text',
                                      default=default,
                                      placeholder=placeholder,
                                      required=required,
                                      readonly=readonly,
                                      unique=unique,
                                      )

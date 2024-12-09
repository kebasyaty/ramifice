"""A field of Model for entering a text."""

from . import (field, groups)


class TextField(field.Field, groups.TextGroup):
    """A field of Model for entering a text."""

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 textarea: bool = False,
                 ):
        field.Field.__init__(self,
                             label=label,
                             disabled=disabled,
                             hide=hide,
                             ignored=ignored,
                             hint=hint,
                             warning=warning,
                             field_type=type(self).__name__,
                             group='text',
                             )
        groups.TextGroup.__init__(self,
                                  input_type='text'
                                  )
        self.__textarea = textarea

    # --------------------------------------------------------------------------
    @property
    def textarea(self) -> bool:
        """\
        Input type for a web form field.
        Html tag: input type="text".
        """
        return self.__textarea

"""Field of Model for upload image."""

from typing import Any
from .general.field import Field
from .general.file_group import FileGroup


class ImageField(Field, FileGroup):
    """Field of Model for upload image.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/files" target="_blank">example</a>.
    """

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 required: bool = False,
                 max_size: int = 2097152,  # 2 MB
                 default: str | None = None,
                 placeholder: str = '',
                 target_dir: str = '',
                 accept: str = '',
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='ImageField',
                       group='image',
                       )
        FileGroup.__init__(self,
                           placeholder=placeholder,
                           required=required,
                           max_size=max_size,
                           default=default,
                           target_dir=target_dir,
                           accept=accept,
                           )

        self.__value: str | None = None

    @property
    def value(self) -> str | None:
        """Sets value of field."""
        return self.__value

    @value.setter
    def value(self, value: str | None) -> None:
        self.__value = value

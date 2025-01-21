"""Field of Model for automatic generation of string `slug`."""

import json

from .general.field import Field
from .general.text_group import TextGroup


class SlugField(Field, TextGroup):
    """Field of Model for automatic generation of string `slug`.
    Convenient to use for Url addresses.
    """

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        placeholder: str = "",
        readonly: bool = False,
        slug_sources: list[str] = ["hash"],
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="SlugField",
            group="slug",
        )
        TextGroup.__init__(
            self,
            input_type="text",
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

    def to_dict(self) -> dict[str, str | bool | list[str] | None]:
        """Convert the field object to a dictionary."""
        json_dict: dict[str, str | bool | list[str] | None] = {}
        for f_name, f_type in self.__dict__.items():
            f_name = f_name.rsplit("__", maxsplit=1)[-1]
            if not callable(f_type):
                json_dict[f_name] = f_type
        return json_dict

    def to_json(self):
        """Convert field object to a json string."""
        return json.dumps(self.to_dict())

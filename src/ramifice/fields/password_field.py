"""Ramifice - Field of Model for enter password."""

__all__ = ("PasswordField",)

import logging
from typing import Any

import orjson

from ramifice.fields.general.field import Field
from ramifice.utils import constants

logger = logging.getLogger(__name__)


class PasswordField(Field):
    r"""Ramifice - Field of Model for enter password.

    Warning:
            Regular expression: ^[-._!"`'#%&,:;<>=@{}~$()*+/\\?[]^|a-zA-Z0-9]{8,256}$
            Valid characters: a-z A-Z 0-9 - . _ ! " ` ' # % & , : ; < > = @ { } ~ $ ( ) * + / \\ ? [ ] ^ |
            Number of characters: from 8 to 256.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        placeholder: str = "",
        required: bool = False,
    ):
        if constants.DEBUG:
            try:
                if not isinstance(label, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if not isinstance(hide, bool):
                    raise AssertionError("Parameter `hide` - Not а `bool` type!")
                if not isinstance(ignored, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(ignored, bool):
                    raise AssertionError("Parameter `ignored` - Not а `bool` type!")
                if not isinstance(hint, str):
                    raise AssertionError("Parameter `hint` - Not а `str` type!")
                if warning is not None and not isinstance(warning, list):
                    raise AssertionError("Parameter `warning` - Not а `list` type!")
                if not isinstance(placeholder, str):
                    raise AssertionError("Parameter `placeholder` - Not а `str` type!")
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
            except AssertionError as err:
                logger.error(str(err))
                raise err

        Field.__init__(
            self,
            label=label,
            disabled=False,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="PasswordField",
            group="pass",
        )

        self.input_type = "password"
        self.value: str | None = None
        self.placeholder = placeholder
        self.required = required

    def to_dict(self) -> dict[str, Any]:
        """Ramifice - Convert object instance to a dictionary."""
        json_dict: dict[str, Any] = {}
        for name, data in self.__dict__.items():
            if not callable(data):
                json_dict[name] = data if name != "value" else None
        return json_dict

    def to_json(self) -> str:
        """Ramifice - Convert object instance to a JSON string."""
        return orjson.dumps(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]) -> Any:
        """Ramifice - Convert JSON string to a object instance."""
        obj = cls()
        for name, data in json_dict.items():
            obj.__dict__[name] = data
        return obj

    @classmethod
    def from_json(cls, json_str: str) -> Any:
        """Ramifice - Convert JSON string to a object instance."""
        json_dict = orjson.loads(json_str)
        return cls.from_dict(json_dict)

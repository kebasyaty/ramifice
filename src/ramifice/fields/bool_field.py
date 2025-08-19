"""Field of Model for enter boolean value."""

from __future__ import annotations

__all__ = ("BooleanField",)

import logging

from ramifice.fields.general.field import Field
from ramifice.utils import constants
from ramifice.utils.mixins import JsonMixin

logger = logging.getLogger(__name__)


class BooleanField(Field, JsonMixin):
    """Field of Model for enter boolean value.

    Args:
        label: Text label for a web form field.
        default: Default value.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        default: bool = False,
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
    ) -> None:
        if constants.DEBUG:
            try:
                if default is not None and not isinstance(default, bool):
                    raise AssertionError("Parameter `default` - Not а `bool` type!")
                if not isinstance(label, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if not isinstance(disabled, bool):
                    raise AssertionError("Parameter `disabled` - Not а `bool` type!")
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
            except AssertionError as err:
                logger.critical(str(err))
                raise err

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="BooleanField",
            group="bool",
        )
        JsonMixin.__init__(self)

        self.input_type = "checkbox"
        self.value: bool | None = None
        self.default = default

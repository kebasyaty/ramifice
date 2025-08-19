"""Field of Model for automatic generation of string `slug`."""

from __future__ import annotations

__all__ = ("SlugField",)

import logging

from ramifice.fields.general.field import Field
from ramifice.fields.general.text_group import TextGroup
from ramifice.utils import constants
from ramifice.utils.mixins import JsonMixin

logger = logging.getLogger(__name__)


class SlugField(Field, TextGroup, JsonMixin):
    """Field of Model for automatic generation of string `slug`.

    Convenient to use for Url addresses.

    Agrs:
        label: Text label for a web form field.
        placeholder: Displays prompt text.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        readonly: Specifies that the field cannot be modified by the user.
        slug_sources: List of sources fields.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        placeholder: str = "",
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        readonly: bool = False,
        slug_sources: list[str] = ["_id"],  # noqa: B006
    ) -> None:
        if constants.DEBUG:
            try:
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
                if not isinstance(placeholder, str):
                    raise AssertionError("Parameter `placeholder` - Not а `str` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
                if not isinstance(slug_sources, list):
                    raise AssertionError("Parameter `slug_sources` - Not а `list` type!")
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
        JsonMixin.__init__(self)

        self.slug_sources = slug_sources

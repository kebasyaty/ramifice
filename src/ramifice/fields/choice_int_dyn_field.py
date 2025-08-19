"""Field of Model.

Type of selective integer field with dynamic addition of elements.
"""

from __future__ import annotations

__all__ = ("ChoiceIntDynField",)

import logging

from ramifice.fields.general.choice_group import ChoiceGroup
from ramifice.fields.general.field import Field
from ramifice.utils import constants
from ramifice.utils.mixins import JsonMixin

logger = logging.getLogger(__name__)


class ChoiceIntDynField(Field, ChoiceGroup, JsonMixin):
    """Field of Model.

    Type of selective integer field with dynamic addition of elements.
    For simulate relationship Many-to-One.
    Element are (add|delete) via `ModelName.unit_manager(unit)` method.

    Args:
        label: Text label for a web form field.
        hide: Hide field from user.
        disabled: Blocks access and modification of the element.
        ignored: If true, the value of this field is not saved in the database.
        hint: An alternative for the `placeholder` parameter.
        warning: Warning information.
        required: Required field.
        readonly: Specifies that the field cannot be modified by the user.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        hide: bool = False,
        disabled: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        readonly: bool = False,
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
                if not isinstance(required, bool):
                    raise AssertionError("Parameter `required` - Not а `bool` type!")
                if not isinstance(readonly, bool):
                    raise AssertionError("Parameter `readonly` - Not а `bool` type!")
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
            field_type="ChoiceIntDynField",
            group="choice",
        )
        ChoiceGroup.__init__(
            self,
            required=required,
            readonly=readonly,
        )
        JsonMixin.__init__(self)

        self.value: int | None = None
        self.choices: list[list[int | str]] | None = None

    def has_value(self, is_migrate: bool = False) -> bool:
        """Does the field value match the possible options in choices."""
        if is_migrate:
            return True
        value = self.value
        if value is not None:
            choices = self.choices
            if not bool(choices):
                return False
            if value not in [item[0] for item in choices]:  # type: ignore[union-attr]
                return False
        return True

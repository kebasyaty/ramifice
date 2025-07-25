"""Ramifice - Field of Model.

Type of selective float field with dynamic addition of elements.
"""

__all__ = ("ChoiceFloatMultDynField",)

import logging

from ramifice.fields.general.choice_group import ChoiceGroup
from ramifice.fields.general.field import Field
from ramifice.utils import constants
from ramifice.utils.mixins.json_converter import JsonMixin

logger = logging.getLogger(__name__)


class ChoiceFloatMultDynField(Field, ChoiceGroup, JsonMixin):
    """Ramifice - Field of Model.

    Type of selective float field with dynamic addition of elements.
    For simulate relationship Many-to-Many.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        required: bool = False,
        readonly: bool = False,
    ):
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
                logger.error(str(err))
                raise err

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="ChoiceFloatMultDynField",
            group="choice",
        )
        ChoiceGroup.__init__(
            self,
            required=required,
            readonly=readonly,
            multiple=True,
        )
        JsonMixin.__init__(self)

        self.value: list[float] | None = None
        self.choices: list[list[float | str]] | None = None

    def has_value(self, is_migrate: bool = False) -> bool:
        """Ramifice - Does the field value match the possible options in choices."""
        if is_migrate:
            return True
        value = self.value
        if value is not None:
            choices = self.choices
            if len(value) == 0 or not bool(choices):
                return False
            value_list = [item[0] for item in choices]  # type: ignore[union-attr]
            for item in value:
                if item not in value_list:
                    return False
        return True

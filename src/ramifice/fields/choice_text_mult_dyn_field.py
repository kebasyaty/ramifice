"""Field of Model.

Type of selective text field with dynamic addition of elements.
"""

from ..utils import globals
from ..utils.mixins.json_converter import JsonMixin
from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceTextMultDynField(Field, ChoiceGroup, JsonMixin):
    """Field of Model.

    Type of selective text field with dynamic addition of elements.
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
        if globals.DEBUG:
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

        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="ChoiceTextMultDynField",
            group="choice",
        )
        ChoiceGroup.__init__(
            self,
            required=required,
            readonly=readonly,
            multiple=True,
        )
        JsonMixin.__init__(self)

        self.value: list[str] | None = None
        self.choices: dict[str, str] | None = None

    def has_value(self, is_migrat: bool = False) -> bool:
        """Does the field value match the possible options in choices."""
        if is_migrat:
            return True
        value = self.value
        if value is not None:
            choices = self.choices
            if len(value) == 0 or not bool(choices):
                return False
            value_list = choices.values()  # type: ignore[union-attr]
            for item in value:
                if item not in value_list:
                    return False
        return True

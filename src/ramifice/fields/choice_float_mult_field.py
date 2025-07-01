"""Field of Model.

Type of selective float field with static of elements.
"""

from ..utils import globals
from ..utils.mixins.json_converter import JsonMixin
from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceFloatMultField(Field, ChoiceGroup, JsonMixin):
    """Field of Model.

    Type of selective float field with static of elements.
    With multiple choice.
    """

    def __init__(  # noqa: D107
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: list[float] | None = None,
        required: bool = False,
        readonly: bool = False,
        choices: list[tuple[float | int | str, str]] | None = None,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="ChoiceFloatMultField",
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
        self.default = default
        self.choices = choices

        if globals.DEBUG:
            if choices is not None:
                if not isinstance(choices, list):
                    raise AssertionError("Parameter `choices` - Not а `list` type!")
                if len(choices) == 0:
                    raise AssertionError(
                        "The `choices` parameter should not contain an empty list!"
                    )
            if default is not None:
                if not isinstance(default, list):
                    raise AssertionError("Parameter `default` - Not а `list` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty list!"
                    )
                if choices is not None and not self.has_value():
                    raise AssertionError(
                        "Parameter `default` does not coincide with "
                        + "list of permissive values in `choicees`."
                    )
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

    def has_value(self, is_migrate: bool = False) -> bool:
        """Does the field value match the possible options in choices."""
        value = self.value
        if value is None:
            value = self.default
        if value is not None:
            choices = self.choices
            if len(value) == 0 or not bool(choices):
                return False
            value_list = [item[0] for item in choices]  # type: ignore[union-attr]
            for item in value:
                if item not in value_list:
                    return False
        return True

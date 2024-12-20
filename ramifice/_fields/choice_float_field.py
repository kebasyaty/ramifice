"""Field of Model.
Type of selective float field with static of elements.
"""

from typing import Any

from .general.field import Field
from .general.choice_group import ChoiceGroup


class ChoiceFloatField(Field, ChoiceGroup):
    """Field of Model.
    Type of selective integer float with static of elements.
    With a single choice.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/static_choices" target="_blank">example</a>.
    """

    debug: bool = True
    meta: dict[str, Any] = {}

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 default: float | None = None,
                 required: bool = False,
                 readonly: bool = False,
                 choices: list[tuple[float, str]] | None = None
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='ChoiceFloatField',
                       group='choice',
                       )
        ChoiceGroup.__init__(self,
                             required=required,
                             readonly=readonly,
                             )
        self.__value: float | None = None
        self.__default = default
        self.__choices = choices

        if ChoiceFloatField.debug:
            if choices is not None and not isinstance(choices, list):
                raise AssertionError(
                    'Parameter `choices` - Not а `list` type!')
            if default is not None and not isinstance(default, float):
                raise AssertionError(
                    'Parameter `default` - Not а `float` type!')
            if default is not None and choices is not None and not self.has_value():
                raise AssertionError(
                    'Parameter `default` does not coincide with ' +
                    'list of permissive values in `choicees`.')

    @property
    def value(self) -> float | None:
        """Sets value of field."""
        return self.__value

    @value.setter
    def value(self, value: float | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def default(self) -> float | None:
        """Value by default."""
        return self.__default

    # --------------------------------------------------------------------------
    @property
    def choices(self) -> list[tuple[float, str]] | None:
        """ Html tag: select.
        Example: [(1.0, 'Title'), (2.0, 'Title 2')]
        """
        return self.__choices

    # ---------------------------------------------------------------------------
    def has_value(self) -> bool:
        """Does the field value match the possible options in choices."""
        flag = True
        value = self.__value
        if value is None:
            value = self.__default
        choices = self.__choices
        if value is not None and choices is not None:
            value_list = [item[0] for item in choices]
            if value not in value_list:
                flag = False
        return flag

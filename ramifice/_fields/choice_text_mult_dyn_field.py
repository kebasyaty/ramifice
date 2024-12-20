"""Field of Model.
Type of selective text field with dynamic addition of elements.
"""

from typing import Any

from .general.choice_group import ChoiceGroup
from .general.field import Field


class ChoiceTextMultDynField(Field, ChoiceGroup):
    """Field of Model.
    Type of selective text field with dynamic addition of elements.
    For simulate relationship Many-to-Many.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/dynamic_choices" target="_blank">example</a>.
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
                 required: bool = False,
                 readonly: bool = False,
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='ChoiceTextMultDynField',
                       group='choice',
                       )
        ChoiceGroup.__init__(self,
                             required=required,
                             readonly=readonly,
                             multiple=True,
                             )
        self.__value: list[str] | None = None
        self.__choices: list[tuple[str, str]] | None = None

    @property
    def value(self) -> list[str] | None:
        """Sets value of field."""
        return self.__value

    @value.setter
    def value(self, value: list[str] | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def choices(self) -> list[tuple[str, str]] | None:
        """ Html tag: select.
        Example: [('value', 'Title'), ('value 2', 'Title 2')]
        """
        return self.__choices

    # --------------------------------------------------------------------------
    def has_value(self) -> bool:
        """Does the field value match the possible options in choices."""
        flag = True
        value = self.__value
        choices = self.__choices
        if value is not None and choices is not None:
            value_list = [item[0]
                          for item in choices]  # pylint: disable=not-an-iterable
            for item in value:
                if item not in value_list:
                    flag = False
                    break
        return flag

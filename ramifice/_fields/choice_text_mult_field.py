"""Field of Model.
Type of selective field with static of elements.
"""

from .general.field import Field
from .general.choice_group import ChoiceGroup


class ChoiceTextMultField(Field, ChoiceGroup):
    """Field of Model.
    Type of selective field with static of elements.
    With multiple choice.
    How to use, see <a href="https://github.com/kebasyaty/ramifice/tree/main/examples/static_choices" target="_blank">example</a>.
    """

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 default: list[str] | None = None,
                 required: bool = False,
                 readonly: bool = False,
                 choices: list[tuple[str]] | None = None
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='ChoiceTextMultField',
                       group='choice',
                       )
        ChoiceGroup.__init__(self,
                             required=required,
                             readonly=readonly,
                             multiple=True,
                             )
        self.__value: list[str] | None = None
        self.__default = default
        self.__choices = choices

    @property
    def value(self) -> list[str] | None:
        """Sets the value of an element."""
        return self.__value

    @value.setter
    def value(self, value: list[str] | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def default(self) -> list[str] | None:
        """Value by default."""
        return self.__default

    # --------------------------------------------------------------------------
    @property
    def choices(self) -> list[tuple[str]] | None:
        """ Html tag: select.
        Example: [('value', 'Title'), ('value 2', 'Title 2')]
        """
        return self.__choices

    # --------------------------------------------------------------------------
    def has_value(self) -> bool:
        """Does the field value match the possible options in choices."""
        flag = True
        value = self.__value
        if value is None:
            value = self.__default
        choices = self.__choices
        if value is not None and choices is not None:
            value_list = [item[0] for item in choices]
            for item in value:
                if item not in value_list:
                    flag = False
                    break
        return flag

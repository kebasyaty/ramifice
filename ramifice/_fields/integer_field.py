"""Field of Model for enter (int) number."""

from .general.field import Field
from .general.number_group import NumberGroup


class IntegerField(Field, NumberGroup):
    """Field of Model for enter (int) number."""

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 default: int | None = None,
                 placeholder: str = '',
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 max_number: int | None = None,
                 min_number: int | None = None,
                 step: int = 1,
                 input_type: str = 'number',  # number | range
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='IntegerField',
                       group='integer',
                       )
        NumberGroup.__init__(self,
                             placeholder=placeholder,
                             required=required,
                             readonly=readonly,
                             unique=unique,
                             )
        assert (input_type in ['number', 'range']), f'{
            input_type} - Invalid input type.'

        self.__input_type: str = input_type
        self.__value: int | None = None
        self.__default = default
        self.__max_number = max_number
        self.__min_number = min_number
        self.__step = step

    @property
    def input_type(self) -> str:
        """Input type for a web form field.
        Html tag: input type="number | range".
        """
        return self.__input_type

    # --------------------------------------------------------------------------
    @property
    def value(self) -> int | None:
        """Sets the value of an element."""
        return self.__value

    @value.setter
    def value(self, value: int | None) -> None:
        self.__value = value

    # --------------------------------------------------------------------------
    @property
    def default(self) -> int | None:
        """Value by default."""
        return self.__default

    # --------------------------------------------------------------------------
    @property
    def max_number(self) -> int | None:
        """Maximum allowed number."""
        return self.__max_number

    # --------------------------------------------------------------------------
    @property
    def min_number(self) -> int | None:
        """Minimum allowed number."""
        return self.__min_number

    # --------------------------------------------------------------------------
    @property
    def step(self) -> int:
        """Increment step for numeric fields."""
        return self.__step

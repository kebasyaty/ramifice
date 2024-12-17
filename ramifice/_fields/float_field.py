"""Field of Model for enter (float) number."""

from .general.field import Field
from .general.number_group import NumberGroup


class FloatField(Field, NumberGroup):
    """Field of Model for enter (float) number."""

    def __init__(self,
                 label: str = "",
                 disabled: bool = False,
                 hide: bool = False,
                 ignored: bool = False,
                 hint: str = "",
                 warning: list[str] | None = None,
                 default: float | None = None,
                 placeholder: str = "",
                 required: bool = False,
                 readonly: bool = False,
                 unique: bool = False,
                 max_number: int | None = None,
                 min_number: int | None = None,
                 step: float = 1,
                 input_type: str = 'number',  # number | range
                 ):
        Field.__init__(self,
                       label=label,
                       disabled=disabled,
                       hide=hide,
                       ignored=ignored,
                       hint=hint,
                       warning=warning,
                       field_type='FloatField',
                       group='float',
                       )
        NumberGroup.__init__(self,
                             placeholder=placeholder,
                             required=required,
                             readonly=readonly,
                             unique=unique,
                             )
        if __debug__:
            if input_type not in ['number', 'range']:
                raise AssertionError(
                    'Parameter `input_type` - Invalid input type! ' +
                    'The permissible value of `number` or` range`.'
                )
            if default is not None and not isinstance(default, int):
                raise AssertionError('Parameter `default` - Not a integer!')

        self.__input_type: str = input_type
        self.__value: float | None = None
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
    def max_number(self) -> float | None:
        """Maximum allowed number."""
        return self.__max_number

    # --------------------------------------------------------------------------
    @property
    def min_number(self) -> float | None:
        """Minimum allowed number."""
        return self.__min_number

    # --------------------------------------------------------------------------
    @property
    def step(self) -> float:
        """Increment step for numeric fields."""
        return self.__step

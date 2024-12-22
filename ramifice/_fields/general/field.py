"""General parameters for all types fields of Model."""


class Field:
    """General parameters for all types fields of Model.

    Attributes:
    label -- Text label for a web form field.
    disabled -- Blocks access and modification of the element.
    hide -- Hide field from user.
    ignored -- If true, the value of this field is not saved in the database.
    hint -- An alternative for the `placeholder` parameter.
    warning -- Warning information.
    errors -- The value is determined automatically.
    field_type -- Field type - ClassName.
    group -- To optimize field traversal in the `check` method.
    """

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        errors: list[str] | None = None,
        field_type: str = "",
        group: str = "",
    ):
        self.__id = ""
        self.__label = label
        self.__name = ""
        self.__field_type = field_type
        self.__disabled = disabled
        self.__hide = hide
        self.__ignored = ignored
        self.__hint = hint
        self.__warning = warning
        self.__errors = errors
        self.__group = group

    @property
    def id(self) -> str:
        """Identifier of document in string presentation.
        Format: <ModelName--field-name>.
        WARNING: The value is determined automatically.
        """
        return self.__id

    @id.setter
    def id(self, value: str) -> None:
        self.__id = value

    # --------------------------------------------------------------------------
    @property
    def label(self) -> str:
        """Text label for a web form field."""
        return self.__label

    @label.setter
    def label(self, value: str) -> None:
        self.__label = value

    # --------------------------------------------------------------------------
    @property
    def name(self) -> str:
        """Field name.
        WARNING: The value is determined automatically.
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    # --------------------------------------------------------------------------
    @property
    def field_type(self) -> str:
        """Field type - Class Name."""
        return self.__field_type

    # --------------------------------------------------------------------------
    @property
    def disabled(self) -> bool:
        """Blocks access and modification of the element."""
        return self.__disabled

    @disabled.setter
    def disabled(self, value: bool) -> None:
        self.__disabled = value

    # --------------------------------------------------------------------------
    @property
    def hide(self) -> bool:
        """Hide field from user."""
        return self.__hide

    @hide.setter
    def hide(self, value: bool) -> None:
        self.__hide = value

    # --------------------------------------------------------------------------
    @property
    def ignored(self) -> bool:
        """If true, the value of this field is not saved in the database."""
        return self.__ignored

    @ignored.setter
    def ignored(self, value: bool) -> None:
        self.__ignored = value

    # --------------------------------------------------------------------------
    @property
    def hint(self) -> str:
        """Additional explanation for the user.
        An alternative for the `placeholder` parameter.
        """
        return self.__hint

    @hint.setter
    def hint(self, value: str) -> None:
        self.__hint = value

    # --------------------------------------------------------------------------
    @property
    def warning(self) -> list[str] | None:
        """Warning information."""
        return self.__warning

    @warning.setter
    def warning(self, value: list[str]) -> None:
        self.__warning = value

    # --------------------------------------------------------------------------
    @property
    def errors(self) -> list[str] | None:
        """For accumulation of errors.
        WARNING: The value is determined automatically."""
        return self.__errors

    @errors.setter
    def errors(self, value: list[str]) -> None:
        self.__errors = value

    # --------------------------------------------------------------------------
    @property
    def group(self) -> str:
        """To optimize field traversal in the `check` method.
        WARNING: It is recommended not to change.
        """
        return self.__group

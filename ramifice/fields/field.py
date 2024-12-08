"""Common aiributs for all types of fields."""

from abc import ABCMeta, abstractmethod


class Field(metaclass=ABCMeta):

    """An abstract class with common aiributs for all types of fields."""

    def __init__(self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        errors: list[str]  | None = None,
    ):
        self.__id = ""
        self.__label = label
        self.__field_type = __name__
        self.__disabled = disabled
        self.__hide = hide
        self.__ignored = ignored
        self.__hint = hint
        self.__warning = warning
        self.__errors = errors
        self.__group = 0

    @property
    @abstractmethod
    def id(self) -> str:
        """\
        Format: <ModelName--field-name>.
        WARNING: The value is determined automatically.
        """
        return self.__id

    @property
    @abstractmethod
    def label(self) -> str:
        """Text label for a web form field."""
        return self.__label

    @label.setter
    @abstractmethod
    def label(self, value: str) -> None:
        self.__label = value

    @property
    @abstractmethod
    def name(self) -> str:
        """\
        Field name.
        WARNING: The value is determined automatically.
        """
        return self.__name

    @name.setter
    @abstractmethod
    def name(self, value: str) -> None:
        self.__name = value

    @property
    @abstractmethod
    def field_type(self) -> str:
        """Field type - Class Name."""
        return self.__field_type

    @property
    @abstractmethod
    def disabled(self) -> bool:
        """Blocks access and modification of the element."""
        return self.__disabled

    @disabled.setter
    @abstractmethod
    def disabled(self, value: bool) -> None:
        self.__disabled = value

    @property
    @abstractmethod
    def hide(self) -> bool:
        """Hide field from user."""
        return self.__hide

    @hide.setter
    @abstractmethod
    def hide(self, value: bool) -> None:
        self.__hide = value

    @property
    @abstractmethod
    def ignored(self) -> bool:
        """If true, the value of this field is not saved in the database."""
        return self.__ignored

    @ignored.setter
    @abstractmethod
    def ignored(self, value: bool) -> None:
        self.__ignored = value

    @property
    @abstractmethod
    def hint(self) -> str:
        """\
        Additional explanation for the user.
        An alternative for the `placeholder` parameter.
        """
        return self.__hint

    @hint.setter
    @abstractmethod
    def hint(self, value: str) -> None:
        self.__hint = value

    @property
    @abstractmethod
    def warning(self) -> list[str] | None:
        """Warning information."""
        return self.__warning

    @warning.setter
    @abstractmethod
    def warning(self, value: list[str]) -> None:
        self.__warning = value

    @property
    @abstractmethod
    def errors(self) -> list[str] | None:
        """WARNING: The value is determined automatically."""
        return self.__errors

    @errors.setter
    @abstractmethod
    def errors(self, value: list[str]) -> None:
        self.__errors = value

    @property
    @abstractmethod
    def group(self) -> int:
        """\
        To optimize field traversal in the `check` method.
        WARNING: It is recommended not to change.
        """
        return self.__group

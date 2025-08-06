"""General parameters for all types fields of Model."""

__all__ = ("Field",)

from abc import ABCMeta


class Field(metaclass=ABCMeta):
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

    def __init__(  # noqd: D107
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        errors: list[str] = [],
        field_type: str = "",
        group: str = "",
    ) -> None:
        self.id = ""
        self.label = label
        self.name = ""
        self.field_type = field_type
        self.disabled = disabled
        self.hide = hide
        self.ignored = ignored
        self.hint = hint
        self.warning = warning
        self.errors = errors
        self.group = group

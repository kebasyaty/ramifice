"""Field of Model for enter URL addresses."""

from urllib.parse import urlparse

from ..store import DEBUG
from ..tools import MixinJSON
from .general.field import Field
from .general.text_group import TextGroup


class URLField(Field, TextGroup, MixinJSON):
    """Field of Model for enter URL addresses.

    Attributes:
    label -- Text label for a web form field.
    disabled -- Blocks access and modification of the element.
    hide -- Hide field from user.
    ignored -- If true, the value of this field is not saved in the database.
    hint -- An alternative for the `placeholder` parameter.
    warning -- Warning information.
    default -- Value by default.
    placeholder -- Displays prompt text.
    required -- Required field.
    readonly -- Specifies that the field cannot be modified by the user.
    unique -- The unique value of a field in a collection.
    """

    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
        default: str | None = None,
        placeholder: str = "",
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ):
        Field.__init__(
            self,
            label=label,
            disabled=disabled,
            hide=hide,
            ignored=ignored,
            hint=hint,
            warning=warning,
            field_type="URLField",
            group="text",
        )
        TextGroup.__init__(
            self,
            input_type="url",
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=unique,
        )
        MixinJSON.__init__(self)

        if DEBUG:
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
                result = urlparse(default)
                if not result.scheme or not result.netloc:
                    raise AssertionError("Parameter `default` - Invalid URL address!")

        self.__default = default

    @property
    def default(self) -> str | None:
        """Value by default."""
        return self.__default

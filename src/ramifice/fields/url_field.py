"""Field of Model for enter URL address."""

from urllib.parse import urlparse

from .. import store
from ..mixins import JsonMixin
from .general.field import Field
from .general.text_group import TextGroup


class URLField(Field, TextGroup, JsonMixin):
    """Field of Model for enter URL address.

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

    def __init__(  # noqa: D107
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
        if store.DEBUG:
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
            if not isinstance(placeholder, str):
                raise AssertionError("Parameter `placeholder` - Not а `str` type!")
            if not isinstance(required, bool):
                raise AssertionError("Parameter `required` - Not а `bool` type!")
            if not isinstance(readonly, bool):
                raise AssertionError("Parameter `readonly` - Not а `bool` type!")
            if not isinstance(unique, bool):
                raise AssertionError("Parameter `unique` - Not а `bool` type!")

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
        JsonMixin.__init__(self)

        self.default = default

    def is_valid(self) -> bool:
        """Validate URL address."""
        url = str(self.value or self.default)
        result = urlparse(url)
        if not result.scheme or not result.netloc:
            return False
        return True

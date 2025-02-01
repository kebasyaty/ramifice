"""Field of Model for enter email address."""

from email_validator import EmailNotValidError, validate_email

from ..mixins import JsonMixin
from ..store import DEBUG
from .general.field import Field
from .general.text_group import TextGroup


class EmailField(Field, TextGroup, JsonMixin):
    """Field of Model for enter email address."""

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
            field_type="EmailField",
            group="text",
        )
        TextGroup.__init__(
            self,
            input_type="email",
            placeholder=placeholder,
            required=required,
            readonly=readonly,
            unique=unique,
        )
        JsonMixin.__init__(self)

        if DEBUG:
            if default is not None:
                if not isinstance(default, str):
                    raise AssertionError("Parameter `default` - Not а `str` type!")
                if len(default) == 0:
                    raise AssertionError(
                        "The `default` parameter should not contain an empty string!"
                    )
                try:
                    validate_email(default, check_deliverability=True)
                except EmailNotValidError:
                    raise AssertionError(  # pylint: disable=raise-missing-from
                        "Parameter `default` - Invalid Email address!"
                    )  # pylint: disable=raise-missing-from

        self.default = default

    def is_valid(self) -> bool:
        """Validate Email address."""
        value = str(self.value or self.default)
        flag = True
        try:
            validate_email(value, check_deliverability=True)
        except EmailNotValidError:
            flag = False
        return flag

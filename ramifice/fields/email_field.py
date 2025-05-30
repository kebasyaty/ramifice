"""Field of Model for enter email address."""

from email_validator import EmailNotValidError, validate_email

from .. import translations
from ..mixins import JsonMixin
from ..store import DEBUG
from .general.field import Field
from .general.text_group import TextGroup


class EmailField(Field, TextGroup, JsonMixin):
    """Field of Model for enter email address."""

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        label: str = translations.gettext("Email address"),
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = translations.gettext("Enter email address"),
        warning: list[str] | None = None,
        default: str | None = None,
        placeholder: str = translations.gettext("Enter email address"),
        required: bool = False,
        readonly: bool = False,
        unique: bool = False,
    ):
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

        if bool(label):
            label = translations.gettext(label)
        if bool(hint):
            hint = translations.gettext(hint)
        if bool(placeholder):
            placeholder = translations.gettext(placeholder)
        if bool(warning):
            warning = [translations.gettext(item) for item in warning]

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

        self.default = default

    def is_valid(self, value: str | None = None) -> bool:
        """Validate Email address."""
        email = str(value or self.value or self.default)
        flag = True
        try:
            validate_email(email, check_deliverability=True)
        except EmailNotValidError:
            flag = False
        return flag

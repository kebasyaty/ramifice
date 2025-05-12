"""Field of Model for enter identifier of document."""

from bson.objectid import ObjectId

from .general.field import Field


class HashField(Field):
    """Field of Model for enter identifier of document.

    Attributes:
    input_type -- Input type for a web form field.
    placeholder -- Displays prompt text.
    required -- Required field.
    readonly -- Specifies that the field cannot be modified by the user.
    unique -- The unique value of a field in a collection.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        label: str = "",
        disabled: bool = False,
        hide: bool = False,
        ignored: bool = False,
        hint: str = "",
        warning: list[str] | None = None,
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
            field_type="HashField",
            group="hash",
        )

        self.input_type = "text"
        self.value: ObjectId | None = None
        self.placeholder = placeholder
        self.required = required
        self.readonly = readonly
        self.unique = unique
        self.alerts: list[str] = []

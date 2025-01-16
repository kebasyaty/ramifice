"""For converting Python classes into Ramifice Model."""

from .fields import DateTimeField, HashField


class Model:
    """For converting Python classes into Ramifice Model."""

    hash = HashField(label="Document ID", hide=True, ignored=True, disabled=True)
    created_at = DateTimeField(
        label="Created at",
        warning=["When the document was created."],
        hide=True,
        disabled=True,
    )
    updated_at = DateTimeField(
        label="Updated at",
        warning=["When the document was updated."],
        hide=True,
        disabled=True,
    )

    def model_name(self) -> str:
        """Get Model name - Class name."""
        return self.__class__.__name__

    def full_model_name(self) -> str:
        """Get full Model name - Module name + . + Class name."""
        cls = self.__class__
        return f"{cls.__module__}.{cls.__name__}"

"""An abstraction for converting Python classes into Ramifice Model."""

from abc import ABCMeta

from .fields import DateTimeField, HashField


class Model(metaclass=ABCMeta):
    """An abstraction for converting Python classes into Ramifice Model."""

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

"""Ramifice - Custom Exceptions for Ramifice."""


class RamificeException(Exception):
    """Ramifice - Root Exception for Ramifice."""

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def] # noqa: D107
        super().__init__(*args, **kwargs)


class FileHasNoExtensionError(RamificeException):
    """Ramifice - Exception raised if the file has no extension.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "File has no extension!") -> None:  # noqa: D107
        self.message = message
        super().__init__(self.message)


class DoesNotMatchRegexError(RamificeException):
    """Ramifice - Exception raised if does not match the regular expression.

    Attributes:
        regex_str -- regular expression in string representation
    """

    def __init__(self, regex_str: str) -> None:  # noqa: D107
        self.message = f"Does not match the regular expression: {regex_str}"
        super().__init__(self.message)


class NoModelsForMigrationError(RamificeException):
    """Ramifice - Exception raised if no Models for migration."""

    def __init__(self):  # type: ignore[no-untyped-def] # noqa: D107
        self.message = "No Models for Migration!"
        super().__init__(self.message)


class PanicError(RamificeException):
    """Ramifice - Exception raised for cases of which should not be.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str) -> None:  # noqa: D107
        self.message = message
        super().__init__(self.message)


class OldPassNotMatchError(RamificeException):
    """Ramifice - Exception raised if when updating the password,
    the old password does not match.
    """  # noqa: D205

    def __init__(self) -> None:  # noqa: D107
        self.message = "Old password does not match!"
        super().__init__(self.message)

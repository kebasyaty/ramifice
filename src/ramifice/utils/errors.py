"""Custom Exceptions for Ramifice."""

from __future__ import annotations


class RamificeException(Exception):
    """Root Exception for Ramifice."""

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def] # noqa: D107
        super().__init__(*args, **kwargs)


class FileHasNoExtensionError(RamificeException):
    """Exception raised if the file has no extension.

    Args:
        message: explanation of the error
    """

    def __init__(self, message: str = "File has no extension!") -> None:  # noqa: D107
        self.message = message
        super().__init__(self.message)


class DoesNotMatchRegexError(RamificeException):
    """Exception raised if does not match the regular expression.

    Args:
        regex_str: regular expression in string representation
    """

    def __init__(self, regex_str: str) -> None:  # noqa: D107
        self.message = f"Does not match the regular expression: {regex_str}"
        super().__init__(self.message)


class NoModelsForMigrationError(RamificeException):
    """Exception raised if no Models for migration."""

    def __init__(self) -> None:  # noqa: D107
        self.message = "No Models for Migration!"
        super().__init__(self.message)


class PanicError(RamificeException):
    """Exception raised for cases of which should not be.

    Args:
        message: explanation of the error
    """

    def __init__(self, message: str) -> None:  # noqa: D107
        self.message = message
        super().__init__(self.message)


class OldPassNotMatchError(RamificeException):
    """Exception is raised when trying to update the password.

    Hint: If old password does not match.
    """

    def __init__(self) -> None:  # noqa: D107
        self.message = "Old password does not match!"
        super().__init__(self.message)


class ForbiddenDeleteDocError(RamificeException):
    """Exception is raised when trying to delete the document.

    Args:
        message: explanation of the error
    """

    def __init__(self, message: str) -> None:  # noqa: D107
        self.message = message
        super().__init__(self.message)


class NotPossibleAddUnitError(RamificeException):
    """Exception is raised when not possible to add Unit.

    Args:
        message: explanation of the error
    """

    def __init__(self, message: str) -> None:  # noqa: D107
        self.message = message
        super().__init__(self.message)


class NotPossibleDeleteUnitError(RamificeException):
    """Exception is raised when not possible to delete Unit.

    Args:
        message: explanation of the error
    """

    def __init__(self, message: str) -> None:  # noqa: D107
        self.message = message
        super().__init__(self.message)

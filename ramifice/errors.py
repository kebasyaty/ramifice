"""Custom Exceptions for Ramifice."""


class RamificeException(Exception):
    """Root Exception for Ramifice."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FileHasNoExtensionError(RamificeException):
    """Exception raised if the file has no extension.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "File has no extension!"):
        self.message = message
        super().__init__(self.message)


class DoesNotMatchRegexError(RamificeException):
    """Exception raised if does not match the regular expression.

    Attributes:
        regex_str -- regular expression in string representation
    """

    def __init__(self, regex_str: str):
        self.message = f"Does not match the regular expression: {regex_str}"
        super().__init__(self.message)


class NoModelsForMigrationError(RamificeException):
    """Exception raised if no Models for migration."""

    def __init__(self):
        self.message = "No Models for Migration!"
        super().__init__(self.message)


class PanicError(RamificeException):
    """Exception raised for cases of which should not be.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class OldPassNotMatchError(RamificeException):
    """Exception raised if when updating the password,
    the old password does not match."""

    def __init__(self):
        self.message = "Old password does not match!"
        super().__init__(self.message)

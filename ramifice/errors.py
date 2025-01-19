"""Custom Exceptions for Ramifice."""


class RamificeException(Exception):
    """Root Exception for Ramifice."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InvalidDateError(RamificeException):
    """Exception raised for invalid date.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "Invalid Date!"):
        self.message = message
        super().__init__(self.message)


class InvalidDateTimeError(RamificeException):
    """Exception raised for invalid date and time.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = "Invalid Date and Time!"):
        self.message = message
        super().__init__(self.message)


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

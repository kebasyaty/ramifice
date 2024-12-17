"""Custom Exceptions for Ramifice."""


class RamificeException(Exception):
    """Root Exception for Ramifice."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InvalidDate(RamificeException):
    """Exception raised for invalid date.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = 'Invalid Date!'):
        self.message = message
        super().__init__(self.message)


class InvalidDateTime(RamificeException):
    """Exception raised for invalid date and time.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str = 'Invalid Date and Time!'):
        self.message = message
        super().__init__(self.message)

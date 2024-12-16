"""Custom Exceptions for Ramifice."""


class RamificeException(Exception):
    """Root Exception for Ramifice."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InvalidDate(RamificeException):
    """Invalid date."""

    def __init__(self):
        msg = 'Invalid Date!'
        super().__init__()
        self.args = (msg)
        self.errmsg = msg


class InvalidDateTime(RamificeException):
    """Invalid date and time."""

    def __init__(self):
        msg = 'Invalid Date and Time!'
        super().__init__()
        self.args = (msg)
        self.errmsg = msg

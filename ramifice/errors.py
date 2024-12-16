"""Custom Exceptions for Ramifice."""


class RamificeException(Exception):
    """Root Exception for Ramifice."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InvalidDate(RamificeException):
    """Invalid date."""

    def __init__(self):
        msg = 'Invalid date!'
        super().__init__()
        self.args = (msg)
        self.errmsg = msg

"""Tools - A set of additional auxiliary methods for Paladins."""


class ToolsMixin:
    """A set of additional auxiliary methods for Paladins."""

    def is_valid(self) -> bool:
        """Check data validity.
        The main use is to check data from web forms.
        """
        output_data = self.check()  # type: ignore[attr-defined]
        return output_data.is_valid

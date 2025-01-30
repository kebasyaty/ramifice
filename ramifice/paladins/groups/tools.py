"""Tools - A set of additional auxiliary methods for Paladins."""


class ToolsMixin:
    """A set of additional auxiliary methods for Paladins."""

    def is_valid(self) -> bool:
        """Check data validity.
        The main use is to check data from web forms.
        """
        output_data = self.check()  # type: ignore[attr-defined]
        return output_data.is_valid

    def print_err(self) -> None:
        """Printing errors to the console.
        Convenient to use during development.
        """
        is_err: bool = False
        for field_name, field_data in self.__dict__.items():
            if callable(field_data):
                continue
            if bool(field_data.errors):
                # title
                if not is_err:
                    print("\nERRORS:")
                    print(f"Model: `{self.full_model_name()}`")  # type: ignore[attr-defined]
                    is_err = True
                # field name
                print(field_name, end="")
                print(" => ", end="")
                # error messages
                print(" || ".join(field_data.errors))
        if bool(self.hash.alerts):  # type: ignore[attr-defined]
            # title
            print("AlERTS:")
            # messages
            print("\n".join(self.hash.alerts), end="\n\n")  # type: ignore[attr-defined]

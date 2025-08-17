"""Validation of Model and printing errors to console."""

__all__ = ("ValidationMixin",)

from typing import Any

from termcolor import colored


class ValidationMixin:
    """Validation of Model and printing errors to console."""

    async def is_valid(self) -> bool:
        """Check data validity.

        The main use is to check data from web forms.
        It is also used to verify Models that do not migrate to the database.
        """
        result_check: dict[str, Any] = await self.check()
        return result_check["is_valid"]

    def print_err(self) -> None:
        """Printing errors to console.

        Convenient to use during development.
        """
        is_err: bool = False
        for field_name, field_data in self.__dict__.items():
            if callable(field_data):
                continue
            if len(field_data.errors) > 0:
                # title
                if not is_err:
                    print(colored("\nERRORS:", "red", attrs=["bold"]))
                    print(colored("Model: ", "blue", attrs=["bold"]), end="")
                    print(colored(f"`{self.full_model_name()}`", "blue"))
                    is_err = True
                # field name
                print(colored("Field: ", "green", attrs=["bold"]), end="")
                print(colored(f"`{field_name}`:", "green"))
                # error messages
                print(colored("\n".join(field_data.errors), "red"))
        if len(self._id.alerts) > 0:
            # title
            print(colored("AlERTS:", "yellow", attrs=["bold"]))
            # messages
            print(colored("\n".join(self._id.alerts), "yellow"), end="\n\n")
        else:
            print(end="\n\n")

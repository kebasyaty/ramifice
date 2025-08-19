"""Validation of Model and printing errors to console."""

from __future__ import annotations

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
                    print(colored("\nERRORS:", "red", attrs=["bold"]))  # noqa: T201
                    print(colored("Model: ", "blue", attrs=["bold"]), end="")  # noqa: T201
                    print(colored(f"`{self.full_model_name()}`", "blue"))  # noqa: T201
                    is_err = True
                # field name
                print(colored("Field: ", "green", attrs=["bold"]), end="")  # noqa: T201
                print(colored(f"`{field_name}`:", "green"))  # noqa: T201
                # error messages
                print(colored("\n".join(field_data.errors), "red"))  # noqa: T201
        if len(self._id.alerts) > 0:
            # title
            print(colored("AlERTS:", "yellow", attrs=["bold"]))  # noqa: T201
            # messages
            print(colored("\n".join(self._id.alerts), "yellow"), end="\n\n")  # noqa: T201
        else:
            print(end="\n\n")  # noqa: T201

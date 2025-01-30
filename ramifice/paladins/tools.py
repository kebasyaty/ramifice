"""Tools - A set of additional auxiliary methods for Paladins."""

from typing import Any

from termcolor import colored

from ..errors import PanicError


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
                    print(colored("\nERRORS:", "red", attrs=["bold"]))
                    print(colored(f"Model: `{self.full_model_name()}`", "blue", attrs=["bold"]))  # type: ignore[attr-defined]
                    is_err = True
                # field name
                print(colored(field_name, "green", attrs=["bold"]), end="")
                print(colored(" =>", "blue", attrs=["bold"]))
                # error messages
                print(colored("\n".join(field_data.errors), "red"))
        if bool(self.hash.alerts):  # type: ignore[attr-defined]
            # title
            print(colored("AlERTS:", "yellow", attrs=["bold"]))
            # messages
            print(colored("\n".join(self.hash.alerts), "yellow"), end="\n\n")  # type: ignore[attr-defined]

    def accumulate_error(self, err_msg: str, params: dict[str, Any]) -> None:
        """For accumulating errors to ModelName.field_name.errors"""
        if not params["field_data"].hide:
            params["field_data"].errors.appand(err_msg)
            if not params["is_error_symptom"]:
                params["is_error_symptom"] = True
        else:
            msg = (
                f">>hidden field<< - Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
                + f"Field: `{params["field_data"].name}`"
                + f" => {err_msg}"
            )
            raise PanicError(msg)

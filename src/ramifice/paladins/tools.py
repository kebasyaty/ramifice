"""Tools - A set of additional auxiliary methods for Paladins."""

from datetime import datetime
from typing import Any

from termcolor import colored

from ..errors import PanicError


class ToolMixin:
	"""A set of additional auxiliary methods for Paladins."""

	async def is_valid(self) -> bool:
		"""Check data validity.

		The main use is to check data from web forms.
		"""
		result_check: dict[str, Any] = await self.check()  # type: ignore[attr-defined]
		return result_check["is_valid"]

	def print_err(self) -> None:
		"""Printing errors to the console.

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
					print(colored(f"`{self.full_model_name()}`", "blue"))  # type: ignore[attr-defined]
					is_err = True
				# field name
				print(colored("Field: ", "green", attrs=["bold"]), end="")
				print(colored(f"`{field_name}`:", "green"))
				# error messages
				print(colored("\n".join(field_data.errors), "red"))
		if len(self._id.alerts) > 0:  # type: ignore[attr-defined]
			# title
			print(colored("AlERTS:", "yellow", attrs=["bold"]))
			# messages
			print(colored("\n".join(self._id.alerts), "yellow"), end="\n\n")  # type: ignore[attr-defined]
		else:
			print(end="\n\n")

	def accumulate_error(self, err_msg: str, params: dict[str, Any]) -> None:
		"""For accumulating errors to ModelName.field_name.errors ."""
		if not params["field_data"].hide:
			params["field_data"].errors.append(err_msg)
			if not params["is_error_symptom"]:
				params["is_error_symptom"] = True
		else:
			msg = (
				f">>hidden field<< - Model: `{self.full_model_name()}` > "  # type: ignore[attr-defined]
				+ f"Field: `{params['field_data'].name}`"
				+ f" => {err_msg}"
			)
			raise PanicError(msg)

	async def check_uniqueness(
		self,
		value: str | int | float | datetime,
		params: dict[str, Any],
	) -> bool:
		"""Check the uniqueness of the value in the collection."""
		if not self.__class__.META["is_migrat_model"]:  # type: ignore[attr-defined]
			return True
		q_filter = {
			"$and": [
				{"_id": {"$ne": params["doc_id"]}},
				{params["field_data"].name: value},
			],
		}
		return await params["collection"].find_one(q_filter) is None

	def ignored_fields_to_none(self):
		"""Reset the values of ignored fields to None."""
		for _, field_data in self.__dict__.items():
			if not callable(field_data) and field_data.ignored and field_data.name != "_id":
				field_data.value = None

	def refrash_from_mongo_doc(self, mongo_doc: dict[str, Any]):
		"""Update object instance from Mongo document."""
		for name, data in mongo_doc.items():
			field = self.__dict__[name]
			field.value = data if field.group != "pass" else None

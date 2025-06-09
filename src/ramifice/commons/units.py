"""Units Management.

Management for `choices` parameter in dynamic field types.
"""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from .. import store
from ..errors import PanicError
from ..types import Unit


class UnitMixin:
	"""Units Management.

	Management for `choices` parameter in dynamic field types.
	"""

	@classmethod
	async def unit_manager(cls, unit: Unit) -> None:
		"""Units Management.

		Management for `choices` parameter in dynamic field types.
		"""
		# Get access to super collection.
		# (Contains Model state and dynamic field data.)
		super_collection: AsyncCollection = store.MONGO_DATABASE[  # type: ignore[index]
			store.SUPER_COLLECTION_NAME
		]
		# Get Model state.
		model_state: dict[str, Any] | None = await super_collection.find_one(
			filter={"collection_name": cls.META["collection_name"]}  # type: ignore[attr-defined]
		)
		# Check the presence of a Model state.
		if model_state is None:
			raise PanicError("Error: Model State - Not found!")
		# Get the dynamic field type.
		field_type = model_state["field_name_and_type"][unit.field]
		# Get dynamic field data.
		choices: dict[str, float | int | str] | None = model_state["data_dynamic_fields"][
			unit.field
		]
		# Check whether the type of value is valid for the type of field.
		if not (
			("ChoiceFloat" in field_type and isinstance(unit.value, float))
			or ("ChoiceInt" in field_type and isinstance(unit.value, int))
			or ("ChoiceText" in field_type and isinstance(unit.value, str))
		):
			msg = (
				"Error: Method: `unit_manager(unit: Unit)` => unit.value - "
				+ f"The type of value `{type(unit.value)}` "
				+ f"does not correspond to the type of field `{field_type}`!"
			)
			raise PanicError(msg)
		# Add Unit to Model State.
		if not unit.is_delete:
			if choices is not None:
				choices = {**choices, **{unit.title: unit.value}}
			else:
				choices = {unit.title: unit.value}
			model_state["data_dynamic_fields"][unit.field] = choices
		# Delete Unit from Model State.
		else:
			if choices is None:
				msg = (
					"Error: It is not possible to delete Unit."
					+ f"Unit `{unit.title}: {unit.value}` not exists!"
				)
				raise PanicError(msg)
			is_key_exists: bool = unit.title in choices.keys()
			if not is_key_exists:
				msg = (
					"Error: It is not possible to delete Unit."
					+ f"Unit `{unit.title}: {unit.value}` not exists!"
				)
				raise PanicError(msg)
			del choices[unit.title]
			model_state["data_dynamic_fields"][unit.field] = choices or None
		# Update the state of the Model in the super collection.
		await super_collection.replace_one(
			filter={"collection_name": model_state["collection_name"]},
			replacement=model_state,
		)
		# Update metadata of the current Model.
		cls.META["data_dynamic_fields"][unit.field] = choices or None  # type: ignore[attr-defined]
		# Update documents in the collection of the current Model.
		if unit.is_delete:
			unit_field: str = unit.field
			unit_value: float | int | str = unit.value
			collection: AsyncCollection = store.MONGO_DATABASE[cls.META["collection_name"]]  # type: ignore[index, attr-defined]
			async for mongo_doc in collection.find():
				field_value = mongo_doc[unit_field]
				if field_value is not None:
					if isinstance(unit_value, list):
						value_list = mongo_doc[unit_field]
						value_list.remove(unit_value)
						mongo_doc[unit_field] = value_list or None
					else:
						mongo_doc[unit_field] = None
				await collection.replace_one(
					filter={"_id": mongo_doc["_id"]},
					replacement=mongo_doc,
				)

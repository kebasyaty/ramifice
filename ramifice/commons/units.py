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

    async def unit_manager(self, unit: Unit) -> None:
        """Units Management.
        Management for `choices` parameter in dynamic field types.
        """
        cls_model = self.__class__
        # Get access to super collection.
        # (Contains Model state and dynamic field data.)
        super_collection: AsyncCollection = store.MONGO_DATABASE[  # type: ignore[index]
            store.SUPER_COLLECTION_NAME
        ]
        # Get Model state.
        model_state: dict[str, Any] | None = await super_collection.find_one(
            filter={"collection_name": cls_model.META["collection_name"]}  # type: ignore[attr-defined]
        )
        # Check the presence of a Model state.
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        # Get the dynamic field type.
        field_type = model_state["field_name_and_type"][unit.field]
        # Get dynamic field data.
        choices: dict[str, float | int | str] = model_state["data_dynamic_fields"][
            unit.field
        ]
        # Check the existence of the key.
        is_key_exists = unit.title in choices.keys()
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
            model_state["data_dynamic_fields"][unit.field] = {
                **choices,
                **{unit.title: unit.value},
            }
        # Delete Unit from Model State.
        else:
            if not is_key_exists:
                msg = (
                    "Error: It is not possible to delete Unit."
                    + f"Unit `{unit.title}: {unit.value}` not exists!"
                )
                raise PanicError(msg)
            del choices[unit.title]
            model_state["data_dynamic_fields"][unit.field] = choices
        # Update the state of the Model in the super collection.
        await super_collection.replace_one(
            filter={"collection_name": model_state["collection_name"]},
            replacement=model_state,
        )
        # Update metadata of the current Model.
        cls_model.META["data_dynamic_fields"][unit.field] = choices  # type: ignore[attr-defined]
        # Update documents in the collection of the current Model.
        if unit.is_delete:
            pass

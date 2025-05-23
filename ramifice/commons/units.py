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
        if model_state is None:
            raise PanicError("Error: Model State - Not found!")
        # Check the presence of a dynamic field.
        if model_state["data_dynamic_fields"].get(unit.field) is None:
            msg = f"The Model is missing a dynamic field `{unit.field}`!"
            raise PanicError(msg)
        # Get the dynamic field type.

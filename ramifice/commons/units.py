"""Units Management.
Management for `choices` parameter in dynamic field types.
"""

from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from .. import store
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
        # Unit validation.
        # Raises panic if it finds inconsistencies.
        unit.is_valid(model_state)
        # Check the presence of a dynamic field.

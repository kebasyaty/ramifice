"""Units Management.
Management for `choices` parameter in dynamic field types.
"""

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
        # Unit validation.
        unit.is_valid()
        # Get access to super collection.
        # (Contains Model state and dynamic field data.)
        super_collection: AsyncCollection = store.MONGO_DATABASE[  # type: ignore[index]
            store.SUPER_COLLECTION_NAME
        ]

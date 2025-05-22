"""Units Management.
Management for `choices` parameter in dynamic field types.
"""

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
        # Check if this model is migrated to database.
        if not cls_model.META["is_migrat_model"]:  # type: ignore[index, attr-defined]
            msg = (
                f"Model: `{cls_model.META["full_model_name"]}` > "  # type: ignore[index, attr-defined]
                + "META param: `is_migrat_model` (False) => "
                + "This Model is not migrated to database!"
            )
            raise PanicError(msg)

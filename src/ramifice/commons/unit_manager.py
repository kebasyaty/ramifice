"""Units Management.

Management for `choices` parameter in dynamic field types.
"""

from __future__ import annotations

__all__ = ("UnitMixin",)

import logging
from typing import Any

from pymongo.asynchronous.collection import AsyncCollection

from ramifice.utils import constants, translations
from ramifice.utils.errors import (
    NotPossibleAddUnitError,
    NotPossibleDeleteUnitError,
    PanicError,
)
from ramifice.utils.unit import Unit

logger = logging.getLogger(__name__)


class UnitMixin:
    """Units Management.

    Management for `choices` parameter in dynamic field types.
    """

    @classmethod
    async def unit_manager(cls: Any, unit: Unit) -> None:
        """Units Management.

        Management for `choices` parameter in dynamic field types.
        """
        # Get access to super collection.
        # (Contains Model state and dynamic field data.)
        super_collection: AsyncCollection = constants.MONGO_DATABASE[constants.SUPER_COLLECTION_NAME]
        # Get Model state.
        model_state: dict[str, Any] | None = await super_collection.find_one(
            filter={"collection_name": cls.META["collection_name"]},
        )
        # Check the presence of a Model state.
        if model_state is None:
            msg = "Error: Model State - Not found!"
            logger.critical(msg)
            raise PanicError(msg)
        # Get language list.
        lang_list = translations.LANGUAGES
        # Get clean fields of Unit.
        unit_field: str = unit.field
        title = unit.title
        if len(title) != len(lang_list):
            msg = "Unit.title => There are no translations for some languages!"
            logger.critical(msg)
            raise PanicError(msg)
        title = {lang: title[lang] for lang in lang_list}
        target_value = unit.value
        # Get dynamic field data.
        choices: list | None = model_state["data_dynamic_fields"][unit_field]
        # Determine the presence of unit.
        is_unit_exists: bool = False
        if choices is not None:
            for item in choices:
                if item["value"] == target_value:
                    is_unit_exists = True
                    break
        # Add Unit to Model State.
        if not unit.is_delete:
            if choices is not None:
                if is_unit_exists:
                    main_lang = translations.DEFAULT_LOCALE
                    msg = (
                        "Error: It is not possible to add Unit - "
                        + f"Unit `{title[main_lang]}: {target_value}` is exists!"
                    )
                    logger.error(msg)
                    raise NotPossibleAddUnitError(msg)
                choices.append({"title": title, "value": target_value})
            else:
                choices = [{"title": title, "value": target_value}]
            model_state["data_dynamic_fields"][unit_field] = choices
        else:
            # Delete Unit from Model State.
            if choices is None:
                msg = "Error: It is not possible to delete Unit - Units is not exists!"
                logger.error(msg)
                raise NotPossibleDeleteUnitError(msg)
            if not is_unit_exists:
                main_lang = translations.DEFAULT_LOCALE
                msg = (
                    "Error: It is not possible to delete Unit."
                    + f"Unit `{title[main_lang]}: {target_value}` is not exists!"
                )
                logger.erro(msg)
                raise NotPossibleDeleteUnitError(msg)
            choices = [item for item in choices if item["value"] != target_value]
            model_state["data_dynamic_fields"][unit_field] = choices or None
        # Update state of current Model in super collection.
        await super_collection.replace_one(
            filter={"collection_name": model_state["collection_name"]},
            replacement=model_state,
        )
        # Update metadata of current Model.
        cls.META["data_dynamic_fields"][unit_field] = choices or None
        # Update documents in the collection of the current Model.
        if unit.is_delete:
            collection: AsyncCollection = constants.MONGO_DATABASE[cls.META["collection_name"]]
            async for mongo_doc in collection.find():
                field_value = mongo_doc[unit_field]
                if field_value is not None:
                    if isinstance(field_value, list):
                        value_list = mongo_doc[unit_field]
                        value_list.remove(target_value)
                        mongo_doc[unit_field] = value_list or None
                    else:
                        mongo_doc[unit_field] = None
                await collection.replace_one(
                    filter={"_id": mongo_doc["_id"]},
                    replacement=mongo_doc,
                )

"""Fixtures - To populate the database with pre-created data.

Runs automatically during Model migration.
"""

from __future__ import annotations

__all__ = ("apply_fixture",)

import logging
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml
from dateutil.parser import parse
from pymongo.asynchronous.collection import AsyncCollection
from termcolor import colored

from ramifice.utils.constants import UTC_TIMEZONE
from ramifice.utils.errors import PanicError

logger = logging.getLogger(__name__)


async def apply_fixture(
    fixture_name: str,
    cls_model: Any,
    collection: AsyncCollection,
) -> None:
    """Apply fixture for current Model.

    Runs automatically during Model migration.
    """
    fixture_path: str = f"config/fixtures/{fixture_name}.yml"
    data_yaml: dict[str, Any] | list[dict[str, Any]] | None = None

    with Path.open(Path(fixture_path)) as file:
        data_yaml = yaml.safe_load(file)

    if not bool(data_yaml):
        msg = (
            f"Model: `{cls_model.META['full_model_name']}` > "
            + f"META param: `fixture_name` ({fixture_name}) => "
            + "It seems that fixture is empty or it has incorrect contents!"
        )
        logger.critical(msg)
        raise PanicError(msg)

    if data_yaml is not None:
        if not isinstance(data_yaml, list):
            data_yaml = [data_yaml]

        for data in data_yaml:
            inst_model = cls_model()
            for field_name, field_data in inst_model.__dict__.items():
                if callable(field_data) or field_data.ignored:
                    continue
                group = field_data.group
                value: Any | None = data.get(field_name)
                if value == "None":
                    value = None
                if value is not None:
                    if group == "file" or group == "img":
                        await field_data.from_path(value)
                    elif group == "date":
                        field_data.value = parse(value)
                    else:
                        field_data.value = value
            # Check Model.
            result_check: dict[str, Any] = await inst_model.check(
                is_save=True,
                collection=collection,
            )
            # If the check fails.
            if not result_check["is_valid"]:
                await collection.database.drop_collection(collection.name)
                print(colored("\nFIXTURE:", "red", attrs=["bold"]))  # noqa: T201
                print(colored(fixture_path, "blue", attrs=["bold"]))  # noqa: T201
                inst_model.print_err()
                msg = f"Fixture `{fixture_name}` failed."
                logger.critical(msg)
                raise PanicError(msg)
            # Get data for document.
            checked_data: dict[str, Any] = result_check["data"]
            # Add date and time.
            today = datetime.now(UTC_TIMEZONE)
            checked_data["created_at"] = today
            checked_data["updated_at"] = today
            # Run hook.
            await inst_model.pre_create()
            # Insert doc.
            try:
                await collection.insert_one(checked_data)
            except:
                await collection.database.drop_collection(collection.name)
            # Run hook.
            await inst_model.post_create()

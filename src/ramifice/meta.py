# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
#
# Copyright 2024-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Decorator for generating metadata (parameters) of the Model.

The parameters are assigned to the Model.META variable.
"""

from __future__ import annotations

__all__ = ("meta",)

import logging
import re
from pathlib import Path
from typing import Any

from ramifice.config import Config
from ramifice.errors import DoesNotMatchRegexError, PanicError

logger = logging.getLogger(__name__)


def meta(
    service_name: str,
    fixture_name: str | None = None,
    db_query_docs_limit: int = 1000,
    is_create_doc: bool = True,
    is_update_doc: bool = True,
    is_delete_doc: bool = True,
) -> Any:
    """Decorator for generating metadata (parameters) of the Model.

    The parameters are assigned to the Model.META variable.
    """
    try:  # ruff:ignore[too-many-statements-in-try-clause]
        if not isinstance(service_name, str):
            err_msg = "Parameter `service_name` - Must be `str` type!"
            raise AssertionError(err_msg)
        if not isinstance(fixture_name, (str, type(None))):
            err_msg = "Parameter `fixture_name` - Must be `str | None` type!"
            raise AssertionError(err_msg)
        if not isinstance(db_query_docs_limit, int):
            err_msg = "Parameter `db_query_docs_limit` - Must be `int` type!"
            raise AssertionError(err_msg)
        if not isinstance(is_create_doc, bool):
            err_msg = "Parameter `is_create_doc` - Must be `bool` type!"
            raise AssertionError(err_msg)
        if not isinstance(is_update_doc, bool):
            err_msg = "Parameter `is_update_doc` - Must be `bool` type!"
            raise AssertionError(err_msg)
        if not isinstance(is_delete_doc, bool):
            err_msg = "Parameter `is_delete_doc` - Must be `bool` type!"
            raise AssertionError(err_msg)
    except AssertionError as err:
        logger.critical(str(err))
        raise err

    def decorator(cls: Any) -> Any:
        info_msg = f"Generating metadata for the `{cls.__module__}.{cls.__name__}` model."
        logger.info(info_msg)

        if Config.REGEX["service_name"].match(service_name) is None:
            regex_str: str = "^[A-Z][a-zA-Z0-9]{0,24}$"
            err_msg = f"Does not match the regular expression: {regex_str}"
            logger.critical(err_msg)
            raise DoesNotMatchRegexError(regex_str)
        if fixture_name is not None:
            fixture_path = f"config/fixtures/{fixture_name}.yml"

            if not Path(fixture_path).exists():
                err_msg = (
                    f"Model: `{cls.__module__}.{cls.__name__}` > "
                    + "META param: `fixture_name` => "
                    + f"Fixture the `{fixture_path}` not exists!"
                )
                logger.critical(err_msg)
                raise PanicError(err_msg)

        metadata = {
            "service_name": service_name,
            "fixture_name": fixture_name,
            "db_query_docs_limit": db_query_docs_limit,
            "is_create_doc": is_create_doc,
            "is_update_doc": is_update_doc,
            "is_delete_doc": is_delete_doc,
        }

        cls.META = {
            **metadata,
            **caching(cls, service_name),
        }

        logger.info("Metadata generation completed successfully.")
        return cls

    return decorator


def caching(cls: Any, service_name: str) -> dict[str, Any]:
    """Add additional metadata to `Model.META`."""
    metadata: dict[str, Any] = {}
    model_name: str = cls.__name__
    if Config.REGEX["model_name"].match(model_name) is None:
        regex_str: str = "^[A-Z][a-zA-Z0-9]{0,24}$"
        err_msg = f"Does not match the regular expression: {regex_str}"
        logger.critical(err_msg)
        raise DoesNotMatchRegexError(regex_str)
    # All descriptor fields.
    all_descriptor_fields: list[str] = ["id", "created_at", "updated_at"]
    # Dictionary of field names and type names.
    # Format: <field_name, field_type>
    field_name_and_type: dict[str, str] = {}
    # List of dynamic fields.
    data_dynamic_fields: dict[str, dict[str, str | int | float] | None] = {}
    # List of text fields that support localization.
    # Hint: Only `TextField`
    multi_lang_text_fields: list[str] = []

    for f_name, f_value in cls.__dict__.items():
        for item in ["_html_attrs", "_funcs"]:
            if item in f_name:
                err_msg = f"The field name must not contain `{item}`."
                logger.critical(err_msg)
                raise KeyError(err_msg)
        f_cls_name = f_value.__class__.__name__
        if not callable(f_value) and "Field" in f_cls_name:
            f_html_attrs: dict[str, Any] = f_value.html_attrs
            all_descriptor_fields.append(f_name)
            #
            if not f_html_attrs["ignored"]:
                # Get a dictionary of field names and types.
                field_name_and_type[f_name] = f_cls_name
                # Add dynamic field.
                if "Dyn" in f_cls_name:
                    data_dynamic_fields[f_name] = None
                if f_cls_name == "TextField" and f_html_attrs["multi_language"]:
                    multi_lang_text_fields.append(f_name)

    metadata["model_name"] = model_name
    metadata["full_model_name"] = f"{cls.__module__}.{model_name}"
    metadata["collection_name"] = f"{service_name}_{model_name}"
    metadata["all_descriptor_fields"] = all_descriptor_fields
    metadata["field_name_and_type"] = field_name_and_type
    metadata["data_dynamic_fields"] = data_dynamic_fields
    metadata["regex_mongo_filter"] = re.compile(rf'(?P<field>"(?:{"|".join(multi_lang_text_fields)})":)')

    return metadata

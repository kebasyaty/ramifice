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
"""Group for checking slug fields.

Supported fields:
    SlugField
"""

from __future__ import annotations

__all__ = ("SlugGroupMixin",)

import logging
from typing import Any

from slugify import slugify

from ramifice.errors import PanicError
from ramifice.paladins.utils import check_uniqueness

logger = logging.getLogger(__name__)


class SlugGroupMixin:
    """Group for checking slug fields.

    Supported fields:
        SlugField
    """

    async def slug_group(self, params: dict[str, Any]) -> None:
        """Checking slug fields."""
        if not params["is_save"]:
            return
        #
        f__attrs = params["field__attrs"]
        f_name = f__attrs.name
        slug_sources = f__attrs.slug_sources
        raw_str_list: list[str] = []
        #
        for f_name_ in params["descriptor_fields"]:
            if f_name_ in slug_sources:
                value = getattr(self, f_name_)
                if value is None:
                    value = f__attrs.get("default")
                if value is not None:
                    raw_str_list.append(value if f_name_ != "id" else str(value))
                else:
                    err_msg = (
                        f"Model: `{params['full_model_name']}` > "
                        + f"Field: `{f_name}` => "
                        + f"{f_name_} - "
                        + "This field is specified in slug_sources. "
                        + "This field should be mandatory or assign a default value."
                    )
                    logger.critical(err_msg)
                    raise PanicError(err_msg)
        # Insert result.
        if params["is_save"]:
            # Convert to slug.
            value = slugify("-".join(raw_str_list))
            # Validation of uniqueness of the value.
            if not await check_uniqueness(
                value,
                params,
                f_name,
            ):
                err_msg = (
                    f"Model: `{params['full_model_name']}` > "
                    + f"Field: `{f_name}` > "
                    + "Parameter: `slug_sources` => "
                    + "At least one field should be unique!"
                )
                logger.critical(err_msg)
                raise PanicError(err_msg)
            # Add value to map.
            params["result_map"][f_name] = value

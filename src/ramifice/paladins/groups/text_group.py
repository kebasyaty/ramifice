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
"""Group for checking text fields.

Supported fields:
    URLField | TextField | PhoneField
    IPField | EmailField | ColorField
"""

from __future__ import annotations

__all__ = ("TextGroupMixin",)

import asyncio
from typing import Any

from email_validator import (
    EmailNotValidError,
    validate_email,
)

from ramifice.paladins.utils import (
    accumulate_error,
    check_uniqueness,
    panic_type_error,
)
from ramifice.utils import (
    is_color,
    is_ip,
    is_phone,
    is_url,
)


class TextGroupMixin:
    """Group for checking text fields.

    Supported fields:
        URLField | TextField | PhoneField
        IPField | EmailField | ColorField
    """

    async def text_group(self, params: dict[str, Any]) -> None:
        """Checking text fields."""
        _ = params["_"]
        f_value = params["field_value"]
        f__attrs = params["field__attrs"]
        f__funcs = params["field__funcs"]
        field_name = f__attrs["name"]
        field_type: str = f__attrs["field_type"]
        is_multi_language: bool = (field_type == "TextField") and f__attrs["multi_language"]
        # Get current value.
        value = f_value or f__attrs.get("default")

        if is_multi_language:
            if not isinstance(value, (str, dict, type(None))):
                panic_type_error("str | dict | None", params)
        else:
            if not isinstance(value, (str, type(None))):
                panic_type_error("str | None", params)

        if value is None:
            if f__attrs["required"]:
                err_msg = _("Required field !")
                accumulate_error(err_msg, params)
            if params["is_save"]:
                params["result_map"][field_name] = None
            return
        # Validation the `max_length` field attribute.
        max_length: int | None = f__attrs.get("max_length")
        if max_length is not None and f__funcs["size"]() > max_length:
            err_msg = _(
                "The length of the string exceeds max_length={} !",
            ).format(max_length)
            accumulate_error(err_msg, params)
        # Validation the `unique` field attribute.
        if field.unique and not await check_uniqueness(
            value,
            params,
            field_name,
            is_multi_language,
        ):
            err_msg = _("Is not unique !")
            accumulate_error(err_msg, params)
        # Validation Email, Url, IP, Color, Phone.
        if field_type == "EmailField":
            try:
                emailinfo = await asyncio.to_thread(
                    validate_email,
                    str(value),
                    check_deliverability=True,
                )
                value = emailinfo.normalized
                params["field_value"].value = value
            except EmailNotValidError:
                err_msg = _("Invalid Email address !")
                accumulate_error(err_msg, params)
        elif field_type == "URLField" and not is_url(value):
            err_msg = _("Invalid URL address !")
            accumulate_error(err_msg, params)
        elif field_type == "IPField" and not is_ip(value):
            err_msg = _("Invalid IP address !")
            accumulate_error(err_msg, params)
        elif field_type == "ColorField" and not is_color(value):
            err_msg = _("Invalid Color code !")
            accumulate_error(err_msg, params)
        elif field_type == "PhoneField" and not is_phone(value):
            err_msg = _("Invalid Phone number !")
            accumulate_error(err_msg, params)
        # Insert result.
        if params["is_save"]:
            if is_multi_language:
                LANGUAGES = self._LANGUAGES
                mult_lang_text = (
                    params["curr_doc"][field_name]
                    if params["is_update"]
                    else (
                        dict.fromkeys(LANGUAGES)
                        if isinstance(value, str)
                        else {lang: value.get(lang, "- -") for lang in LANGUAGES}
                    )
                )
                if isinstance(value, dict):
                    for lang in LANGUAGES:
                        mult_lang_text[lang] = value.get(lang, "- -")
                else:
                    mult_lang_text[self._LANG_CODE] = value
                value = mult_lang_text
            params["result_map"][field_name] = value

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
"""Group for checking file fields.

Supported fields: FileField
"""

from __future__ import annotations

__all__ = ("FileGroupMixin",)

from typing import Any

from xloft.converters import to_human_size

from ramifice.paladins.utils import accumulate_error


class FileGroupMixin:
    """Group for checking file fields.

    Supported fields: FileField
    """

    async def file_group(self, params: dict[str, Any]) -> None:
        """Checking file fields."""
        _ = params["_"]
        f_value = params["field_value"] or None
        f__attrs = params["field__attrs"]
        f__funcs = params["field__funcs"]
        f_name = f__attrs.name

        if not params["is_update"] and f_value is None:
            default = f__attrs.default or None
            # If necessary, use the default value.
            if default is not None:
                await f__funcs.from_path(default)
                f_value = f__attrs.value
                setattr(self, f_name, f_value)
            # Validation, if the field is required and empty, accumulate the error.
            # ( the default value is used whenever possible )
            if f_value is None:
                if f__attrs.required:
                    err_msg = _("Required field !")
                    accumulate_error(err_msg, params)
                if params["is_save"]:
                    params["result_map"][f_name] = None
                return
        # Return if the current value is missing
        if f_value is None:
            return
        if not f_value["save_as_is"]:
            # If the file needs to be delete.
            if f_value["is_delete"] and len(f_value["path"]) == 0:
                default = f__attrs.default or None
                # If necessary, use the default value.
                if default is not None:
                    await f__funcs.from_path(default)
                    f_value = f__attrs.value
                    setattr(self, f_name, f_value)
                else:
                    if not f__attrs.required:
                        if params["is_save"]:
                            params["result_map"][f_name] = None
                    else:
                        err_msg = _("Required field !")
                        accumulate_error(err_msg, params)
                    return
            # Accumulate an error if the file size exceeds the maximum value.
            if f_value["size"] > f__attrs.max_size:
                human_size = to_human_size(f__attrs.max_size)
                err_msg = _(
                    "File size exceeds the maximum value {} !",
                ).format(human_size)
                accumulate_error(err_msg, params)
                return
        # Insert result.
        if params["is_save"] and (f_value["is_new_file"] or f_value["save_as_is"]):
            f_value["is_delete"] = False
            f_value["save_as_is"] = True
            params["result_map"][f_name] = f_value

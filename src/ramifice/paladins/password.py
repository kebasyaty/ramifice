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
"""Verification, replacement and recoverang of password."""

from __future__ import annotations

__all__ = ("PasswordMixin",)

import contextlib
import logging
from typing import Any

from argon2 import PasswordHasher
from pymongo.asynchronous.collection import AsyncCollection

from ramifice.config import Config
from ramifice.errors import OldPassNotMatchError, PanicError

logger = logging.getLogger(__name__)


class PasswordMixin:
    """Verification, replacement and recoverang of password."""

    async def verify_password(
        self,
        password: str,
        field_name: str = "password",
    ) -> bool:
        """For password verification."""
        cls_model = self.__class__
        # Get documet ID.
        doc_id = self._id.value
        if doc_id is None:
            err_msg = (
                f"Model: `{cls_model.META['full_model_name']}` > "
                + "Method: `verify_password` => "
                + "Cannot get document ID - ID field is empty."
            )
            logger.critical(err_msg)
            raise PanicError(err_msg)
        # Get collection for current Model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls_model.META["collection_name"]]
        # Get document.
        mongo_doc: dict[str, Any] | None = await collection.find_one({"_id": doc_id})
        if mongo_doc is None:
            err_msg = (
                f"Model: `{cls_model.META['full_model_name']}` > "
                + "Method: `verify_password` => "
                + f"There is no document with ID `{self._id.value}` in the database."
            )
            logger.critical(err_msg)
            raise PanicError(err_msg)
        # Get password hash.
        hash: str | None = mongo_doc.get(field_name)
        if hash is None:
            err_msg = (
                f"Model: `{cls_model.META['full_model_name']}` > "
                + "Method: `verify_password` => "
                + f"The model does not have a field `{field_name}`."
            )
            logger.critical(err_msg)
            raise PanicError(err_msg)
        # Password verification.
        is_valid: bool = False
        ph = PasswordHasher()
        with contextlib.suppress(BaseException):
            is_valid = ph.verify(hash, password)
        #
        if is_valid and ph.check_needs_rehash(hash):
            hash = ph.hash(password)
            await collection.update_one({"_id": doc_id}, {"$set": {field_name: hash}})
        #
        return is_valid

    async def update_password(
        self,
        old_password: str,
        new_password: str,
        field_name: str = "password",
    ) -> None:
        """For replace or recover password."""
        cls_model = self.__class__
        if not await self.verify_password(old_password, field_name):
            logger.warning("Old password does not match!")
            raise OldPassNotMatchError()
        # Get documet ID.
        doc_id = self._id.value
        # Get collection for current Model.
        collection: AsyncCollection = Config.MONGO_DATABASE[cls_model.META["collection_name"]]
        # Create hash of new passwor.
        ph = PasswordHasher()
        hash: str = ph.hash(new_password)
        await collection.update_one({"_id": doc_id}, {"$set": {field_name: hash}})

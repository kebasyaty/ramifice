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
"""HooksMixin - Contains abstract methods for creating hooks."""

from __future__ import annotations

__all__ = ("HooksMixin",)

from abc import abstractmethod


class HooksMixin:
    """A set of abstract methods for creating hooks."""

    @abstractmethod
    async def pre_create(self) -> None:
        """Called before a new document is created in the database."""

    @abstractmethod
    async def post_create(self) -> None:
        """Called after a new document has been created in the database."""

    @abstractmethod
    async def pre_update(self) -> None:
        """Called before updating an existing document in the database."""

    @abstractmethod
    async def post_update(self) -> None:
        """Called after an existing document in the database is updated."""

    @abstractmethod
    async def pre_delete(self) -> None:
        """Called before deleting an existing document in the database."""

    @abstractmethod
    async def post_delete(self) -> None:
        """Called after an existing document in the database has been deleted."""

# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""IndexMixin - Contains abstract method for indexing the model in the database."""

from __future__ import annotations

__all__ = ("IndexMixin",)

from abc import abstractmethod


class IndexMixin:
    """Contains the method for indexing the model in the database."""

    @classmethod
    @abstractmethod
    async def indexing(cls) -> None:
        """Set up and start indexing."""

# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""AddValidMixin - Contains an abstract method for additional validation of fields."""

from __future__ import annotations

__all__ = ("AddValidMixin",)

from abc import abstractmethod

from xloft import NamedTuple


class AddValidMixin:
    """Contains an abstract method for additional validation of fields."""

    @abstractmethod
    async def add_validation(self) -> NamedTuple:
        """Additional validation of fields."""
        return NamedTuple()

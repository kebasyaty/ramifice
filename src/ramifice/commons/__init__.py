# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Commons - Model class methods."""

from __future__ import annotations

__all__ = ("QCommonsMixin",)

from ramifice.commons.general import GeneralMixin
from ramifice.commons.indexes import IndexMixin
from ramifice.commons.many import ManyMixin
from ramifice.commons.one import OneMixin
from ramifice.commons.unit_manager import UnitMixin


class QCommonsMixin(  # noqa: RUF067
    GeneralMixin,
    OneMixin,
    ManyMixin,
    IndexMixin,
    UnitMixin,
):
    """Commons - Model class methods."""

    def __init__(self) -> None:  # noqa: D107
        super().__init__()

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
"""Commons - Model class methods."""

from __future__ import annotations

__all__ = ("QCommonsMixin",)

from ramifice.commons.general import GeneralMixin
from ramifice.commons.indexes import IndexMixin
from ramifice.commons.many import ManyMixin
from ramifice.commons.one import OneMixin
from ramifice.commons.unit_manager import UnitMixin


class QCommonsMixin(  # ruff:ignore[non-empty-init-module]
    GeneralMixin,
    OneMixin,
    ManyMixin,
    IndexMixin,
    UnitMixin,
):
    """Commons - Model class methods."""

    def __init__(self) -> None:  # ruff:ignore[undocumented-public-init]
        super().__init__()

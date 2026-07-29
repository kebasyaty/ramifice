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
"""Groups - Model instance methods for specific processing of fields."""

from __future__ import annotations

__all__ = (
    "BoolGroupMixin",
    "ChoiceGroupMixin",
    "DateGroupMixin",
    "FileGroupMixin",
    "IDGroupMixin",
    "ImgGroupMixin",
    "NumberGroupMixin",
    "PasswordGroupMixin",
    "SlugGroupMixin",
    "TextGroupMixin",
)

from ramifice.paladins.groups.bool_group import BoolGroupMixin
from ramifice.paladins.groups.choice_group import ChoiceGroupMixin
from ramifice.paladins.groups.date_group import DateGroupMixin
from ramifice.paladins.groups.file_group import FileGroupMixin
from ramifice.paladins.groups.id_group import IDGroupMixin
from ramifice.paladins.groups.img_group import ImgGroupMixin
from ramifice.paladins.groups.number_group import NumberGroupMixin
from ramifice.paladins.groups.password_group import PasswordGroupMixin
from ramifice.paladins.groups.slug_group import SlugGroupMixin
from ramifice.paladins.groups.text_group import TextGroupMixin

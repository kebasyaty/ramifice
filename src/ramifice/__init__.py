# Copyright 2022-present MongoDB, Inc.
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

"""Ramifice - ORM-like API MongoDB for Python language."""

__all__ = (
    "NamedTuple",
    "model",
    "translations",
    "Migration",
    "Unit",
)

import logging

from xloft import NamedTuple

from ramifice.models.decorator import model
from ramifice.utils import translations
from ramifice.utils.migration import Migration
from ramifice.utils.unit import Unit

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
)

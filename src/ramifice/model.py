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
"""Converting Python classes into Ramifice Models."""

from __future__ import annotations

__all__ = ("Model",)


from copy import deepcopy
from typing import Any, ClassVar

from xloft import NamedTuple

from ramifice.commons import QCommonsMixin
from ramifice.config import Config
from ramifice.errors import AttributeCannotBeDeleteError
from ramifice.fields import DateTimeField, IDField
from ramifice.json import JsonMixin
from ramifice.paladins import QPaladinsMixin
from ramifice.translator import Translator

_ = Translator.STUB_TRANSLATOR_FOR_ATTRIBUTES_OF_FIELDS


class Model(JsonMixin, QPaladinsMixin, QCommonsMixin):
    """Converting Python Class into Ramifice Model."""

    META: ClassVar[dict[str, Any]] = {}

    id = IDField(
        label=_("Document ID"),
        placeholder=_("It is added automatically"),
        hint=_("It is added automatically"),
        hide=True,
        disabled=True,
    )

    created_at = DateTimeField(
        label=_("Created at"),
        placeholder=_("It is added automatically"),
        hint=_("It is added automatically"),
        warning=[_("When the document was created.")],
        hide=True,
        disabled=True,
    )

    updated_at = DateTimeField(
        label=_("Updated at"),
        placeholder=_("It is added automatically"),
        hint=_("It is added automatically"),
        warning=[_("When the document was updated.")],
        hide=True,
        disabled=True,
    )

    def __init__(self, lang_code: str = Translator.DEFAULT_LOCALE) -> None:
        """Converting Python Class into Ramifice Model.

        Args:
            lang_code (str): Language code for Model localization.
        """
        metadata = self.__class__.META
        descriptor_fields = metadata["all_descriptor_fields"]
        data_dynamic_fields = metadata["data_dynamic_fields"]

        LANGUAGES = deepcopy(Translator.LANGUAGES)
        LANG_CODE = lang_code if lang_code in LANGUAGES else Translator.DEFAULT_LOCALE

        self._LANGUAGES = LANGUAGES
        self._LANG_CODE = LANG_CODE
        self._DATEPARSER_SETTINGS = deepcopy(Config.DATEPARSER_SETTINGS)
        self._UTC_TIMEZONE = deepcopy(Config.UTC_TIMEZONE)
        self.__dict__["_RAMIFICE_TRANSLATOR"] = deepcopy(Translator.ramifice_translator(LANG_CODE, True))
        self.__dict__["_CUSTOM_TRANSLATOR"] = deepcopy(Translator.custom_translator(LANG_CODE, True))

        for f_name in descriptor_fields:
            setattr(self, f_name, None)

        self.inject(lang_code, descriptor_fields, data_dynamic_fields)

    def __delattr__(self, name: str) -> None:
        """Blocked Deleter."""
        raise AttributeCannotBeDeleteError(name)

    @property
    def lang_code(self) -> str:
        """Language code."""
        return self._LANG_CODE

    def model_name(self) -> str:
        """Get Model name - Class name."""
        return self.__class__.__name__

    def full_model_name(self) -> str:
        """Get full Model name - module_name + . + ClassName."""
        cls = self.__class__
        return f"{cls.__module__}.{cls.__name__}"

    def inject(
        self,
        lang_code,
        descriptor_fields,
        data_dynamic_fields,
    ) -> None:
        """Update the state of dynamic fields from metadata of model."""
        for f_name in descriptor_fields:
            f__attrs = getattr(self, f"{f_name}__attrs")
            if "Dyn" in f__attrs.field_type:
                dyn_data = data_dynamic_fields.get(f_name)
                if dyn_data is not None:
                    f__attrs.choices = [[item["value"], item["title"][lang_code]] for item in dyn_data]
                else:
                    # This is necessary for
                    # `paladins > refrash > RefrashMixin > refrash_from_db`.
                    f__attrs.choices = None

    def get_error_map(self) -> NamedTuple:
        """Get clean data."""
        metadata = self.__class__.META
        descriptor_fields = metadata["all_descriptor_fields"]
        error_map: dict[str, Any] = {}

        for name in descriptor_fields:
            error_map[name] = None

        return NamedTuple(**error_map)

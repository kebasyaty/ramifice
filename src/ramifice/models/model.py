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


from typing import Any, ClassVar

from xloft import NamedTuple

from ramifice.errors import AttributeCannotBeDeleteError
from ramifice.fields import DateTimeField, IDField
from ramifice.translations import Translator


class Model:
    """Converting Python Class into Ramifice Model."""

    META: ClassVar[dict[str, Any]] = {}

    # Stub for translator
    _: ClassVar = lambda _: _

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

    def __init__(self) -> None:  # noqa: D107
        metadata = self.__class__.META
        descriptor_fields = metadata["all_descriptor_fields"]
        data_dynamic_fields = metadata["data_dynamic_fields"]

        for f_name in descriptor_fields:
            setattr(self, f_name, None)

        self.ramifice_translator = Translator.ramifice_translator()
        self.custom_translator = Translator.custom_translator()

        self.inject(descriptor_fields, data_dynamic_fields)

    def __delattr__(self, name: str) -> None:
        """Blocked Deleter."""
        raise AttributeCannotBeDeleteError(name)

    def model_name(self) -> str:
        """Get Model name - Class name."""
        return self.__class__.__name__

    def full_model_name(self) -> str:
        """Get full Model name - module_name + . + ClassName."""
        cls = self.__class__
        return f"{cls.__module__}.{cls.__name__}"

    def inject(
        self,
        descriptor_fields,
        data_dynamic_fields,
    ) -> None:
        """Update the state of dynamic fields from metadata of model."""
        lang = Translator.current_locale
        for f_name in descriptor_fields:
            f_html_attrs = getattr(self, f"{f_name}_html_attrs")
            if "Dyn" in f_html_attrs["field_type"]:
                dyn_data = data_dynamic_fields.get(f_name)
                if dyn_data is not None:
                    f_html_attrs["choices"] = [[item["value"], item["title"][lang]] for item in dyn_data]
                else:
                    # This is necessary for
                    # `paladins > refrash > RefrashMixin > refrash_from_db`.
                    f_html_attrs["choices"] = None

    def get_error_map(self) -> NamedTuple:
        """Get clean data."""
        metadata = self.__class__.META
        descriptor_fields = metadata["all_descriptor_fields"]
        error_map: dict[str, Any] = {}

        for name in descriptor_fields:
            error_map[name] = getattr(self, name)

        return NamedTuple(**error_map)

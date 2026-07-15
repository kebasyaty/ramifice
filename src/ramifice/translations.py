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
"""Localization of Translations.

The localization of translations class contains the following parameters:

- `DEFAULT_LOCALE` - Language code by default.
- `LANGUAGES` - List of codes supported by languages.
- `current_locale` - Code of current language.

The localization of translations class contains the following methods:

- `add_new_languages` - Add new languages.
- `change_locale` - Change current language.
- `activate` - Activate translations.

Hint - CKEditor supported languages:

af | ar | ast | az | bg | ca | cs | da | de | de_ch | el | en | en_au |
en_gb | eo | es | et | eu | fa | fi | fr | gl | gu | he | hi |
hr | hu | id | it | ja | km | kn | ko | ku | lt | lv | ms |
nb | ne | nl | no | oc | pl | pt | pt_br | ro | ru | si | sk |
sl | sq | sr | sr_latn | sv | th | tk | tr | tt | ug | uk | vi |
zh | zh_cn
"""

from __future__ import annotations

__all__ = ("Translator",)

import gettext as _gettext
import logging
from gettext import NullTranslations
from typing import ClassVar, final

logger = logging.getLogger(__name__)


@final
class Translator:
    """Manager by localization of translations."""

    # Language by default.
    DEFAULT_LOCALE: ClassVar[str] = "en"
    # List of supported languages.
    LANGUAGES: ClassVar[frozenset[str]] = frozenset(("en", "ru"))
    # Code of current language.
    current_locale: ClassVar[str] = "en"
    # Add translations for Ramifice.
    RAMIFICE_TRANSLATIONS: ClassVar[dict[str, NullTranslations]]
    # Add translations for custom project.
    CUSTOM_TRANSLATIONS: ClassVar[dict[str, NullTranslations]]
    # The object of the current translator, for Ramifice.
    ramifice_translator: ClassVar[NullTranslations]
    # The object of the current translator, for custom project.
    custom_translator: ClassVar[NullTranslations]

    @classmethod
    def add_new_languages(cls, languages: frozenset[str]) -> None:
        """Add new languages."""
        cls.LANGUAGES.union(languages)

    @classmethod
    def change_locale(cls, lang_code: str) -> None:
        """Change current language.

        Examples:
            >>> from ramifice import Translator
            >>> Translator.change_locale("ru")

        Args:
            lang_code: Language code.

        Returns:
            Object `None`.
        """
        if lang_code != cls.CURRENT_LOCALE:
            current_local = lang_code if lang_code in cls.LANGUAGES else cls.DEFAULT_LOCALE
            # Changing the current locale
            cls.CURRENT_LOCALE = current_local
            # Update translator for Ramifice
            cls.ramifice_translator = cls.RAMIFICE_TRANSLATIONS.get(
                current_local,
                cls.RAMIFICE_TRANSLATIONS[cls.DEFAULT_LOCALE],
            )
            # Update translator for custom project
            cls.custom_translator = cls.CUSTOM_TRANSLATIONS.get(
                current_local,
                cls.CUSTOM_TRANSLATIONS[cls.DEFAULT_LOCALE],
            )

    @classmethod
    def activate(cls) -> None:
        """Activate translations."""
        # Add translations for Ramifice
        cls.RAMIFICE_TRANSLATIONS = {
            lang: _gettext.translation(
                domain="messages",
                localedir="config/translations/ramifice",
                languages=[lang],
                class_=None,
                fallback=True,
            )
            for lang in cls.LANGUAGES
        }
        # Add translations for custom project
        cls.CUSTOM_TRANSLATIONS = {
            lang: _gettext.translation(
                domain="messages",
                localedir="config/translations/custom",
                languages=[lang],
                class_=None,
                fallback=True,
            )
            for lang in cls.LANGUAGES
        }
        # Initialize translators
        # ----------------------
        default_locale = cls.DEFAULT_LOCAL
        # Add translator for Ramifice
        cls.ramifice_translator = cls.RAMIFICE_TRANSLATIONS.get(
            default_locale,
            cls.RAMIFICE_TRANSLATIONS[default_locale],
        )
        # Add translator for custom project
        cls.custom_translator = cls.CUSTOM_TRANSLATIONS.get(
            default_locale,
            cls.CUSTOM_TRANSLATIONS[default_locale],
        )

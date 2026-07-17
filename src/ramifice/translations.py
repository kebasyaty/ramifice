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
- `RAMIFICE_TRANSLATIONS` - Translations for Ramifice.
- `CUSTOM_TRANSLATIONS` - Translations for custom project.
- `STUB_TRANSLATOR` - Stub for translator.
- `current_locale` - Current language.

The localization of translations class contains the following methods:

- `add_new_languages` - Add new languages.
- `change_locale` - Globally change the localization of translations.
- `ramifice_translator` - Get translator for Ramifice.
- `custom_translator` - Get translator for custom project.

Language Codes:

https://support.crowdin.com/developer/language-codes/

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
from collections.abc import Callable
from typing import ClassVar, final

logger = logging.getLogger(__name__)


@final
class Translator:
    """Manager by localization of translations."""

    # Language by default
    DEFAULT_LOCALE: ClassVar[str] = "en"
    # List of supported languages
    LANGUAGES: ClassVar[frozenset[str]] = frozenset(("en", "ru"))
    # Translations for Ramifice
    RAMIFICE_TRANSLATIONS: ClassVar[dict[str, _gettext.NullTranslations]] = {
        lang: _gettext.translation(
            domain="messages",
            localedir="config/translations/ramifice",
            languages=[lang],
            class_=None,
            fallback=True,
        )
        for lang in LANGUAGES
    }
    # Translations for custom project
    CUSTOM_TRANSLATIONS: ClassVar[dict[str, _gettext.NullTranslations]] = {
        lang: _gettext.translation(
            domain="messages",
            localedir="config/translations/custom",
            languages=[lang],
            class_=None,
            fallback=True,
        )
        for lang in LANGUAGES
    }
    # Stub for translator
    STUB_TRANSLATOR: ClassVar[Callable] = lambda message: message
    # Current language
    current_locale: ClassVar[str] = "en"

    @classmethod
    def add_new_languages(cls, languages: frozenset[str]) -> None:
        """Add new languages."""
        cls.LANGUAGES.union(languages)

    @classmethod
    def change_locale(cls, lang_code: str) -> None:
        """Globally change the localization of translations."""
        cls.current_locale = lang_code if lang_code in cls.LANGUAGES else cls.DEFAULT_LOCALE

    @classmethod
    def ramifice_translator(cls) -> _gettext.NullTranslations:
        """Get translator for Ramifice."""
        # Return of the translator for Ramifice
        return cls.RAMIFICE_TRANSLATIONS.get(
            cls.current_locale,
            cls.RAMIFICE_TRANSLATIONS[cls.DEFAULT_LOCALE],
        )

    @classmethod
    def custom_translator(cls) -> _gettext.NullTranslations:
        """Get translator for custom project."""
        # Return custom translator
        return cls.CUSTOM_TRANSLATIONS.get(
            cls.current_locale,
            cls.CUSTOM_TRANSLATIONS[cls.DEFAULT_LOCALE],
        )

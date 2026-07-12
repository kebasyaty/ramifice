# Ramifice - ORM-pseudo-like API MongoDB for Python language.
# Copyright (c) 2024 Gennady Kostyunin
# SPDX-License-Identifier: MIT
"""Localization of Translations.

The localization of translations class contains the following parameters:

- `CURRENT_LOCALE` - Code of current language.
- `DEFAULT_LOCALE` - Language code by default.
- `LANGUAGES` - List of codes supported by languages.
- `gettext` - The object of the current translator.
- `ngettext` - The object of the current translator.

The localization of translations class contains the following methods:

- `add_languages` - Add languages.
- `get_ramifice_translator` -Get an object of translation for the desired language, for Ramifice.
- `get_custom_translator` - Get an object of translation for the desired language, for custom project.
- `change_locale` - Change current language.
- `init_params` - Method for general initialization of parameters.

Hint - CKEditor supported languages:

af | ar | ast | az | bg | ca | cs | da | de | de_ch | el | en | en_au |
en_gb | eo | es | et | eu | fa | fi | fr | gl | gu | he | hi |
hr | hu | id | it | ja | km | kn | ko | ku | lt | lv | ms |
nb | ne | nl | no | oc | pl | pt | pt_br | ro | ru | si | sk |
sl | sq | sr | sr_latn | sv | th | tk | tr | tt | ug | uk | vi |
zh | zh_cn
"""

from __future__ import annotations

__all__ = ("Translations",)

import copy
import gettext as _gettext
import logging
from collections.abc import Callable
from gettext import NullTranslations
from typing import Any, ClassVar, final

from ramifice.errors import PanicError

logger = logging.getLogger(__name__)


@final
class Translations:
    """Localization of Translations."""

    # Language by default.
    DEFAULT_LOCALE: ClassVar[str] = "en"
    # Code of current language.
    CURRENT_LOCALE: ClassVar[str] = copy.deepcopy(DEFAULT_LOCALE)
    # List of supported languages.
    LANGUAGES: ClassVar[frozenset[str]] = frozenset(("en", "ru"))
    # The object of the current translation, for Ramifice.
    _: ClassVar[Callable] = lambda _: _
    # The object of the current translation, for custom project.
    gettext: ClassVar[Callable] = lambda _: _
    ngettext: ClassVar[Callable] = lambda _: _

    @classmethod
    def add_languages(
        cls,
        default_locale: str,
        languages: frozenset[str],
    ) -> None:
        """Add languages."""
        if default_locale not in languages:
            msg = "DEFAULT_LOCALE is not included in the LANGUAGES!"
            logger.critical(msg)
            raise PanicError(msg)
        cls.DEFAULT_LOCALE = default_locale
        cls.LANGUAGES = languages

    # Add translations for Ramifice.
    ramifice_translations: ClassVar[dict[str, NullTranslations]] = {
        lang: _gettext.translation(
            domain="messages",
            localedir="config/translations/ramifice",
            languages=[lang],
            class_=None,
            fallback=True,
        )
        for lang in LANGUAGES
    }

    # Add translations for custom project.
    custom_translations: ClassVar[dict[str, NullTranslations]] = {
        lang: _gettext.translation(
            domain="messages",
            localedir="config/translations/custom",
            languages=[lang],
            class_=None,
            fallback=True,
        )
        for lang in LANGUAGES
    }

    @classmethod
    def get_ramifice_translator(cls, lang_code: str) -> Any:
        """Get an object of translation for the desired language, for Ramifice.

        Examples:
            >>> from ramifice.translations import Translations
            >>> _ = Translations.get_ramifice_translator("en").gettext
            >>> msg = _("Hello World!")
            >>> print(msg)
            Hello World!

        Args:
            lang_code: Language code.

        Returns:
            Object of translation for the desired language.
        """
        return cls.ramifice_translations.get(
            lang_code,
            cls.ramifice_translations[cls.DEFAULT_LOCALE],
        )

    @classmethod
    def get_custom_translator(cls, lang_code: str) -> Any:
        """Get an object of translation for the desired language, for custom project.

        Examples:
            >>> from ramifice.translations import Translations
            >>> gettext = Translations.get_custom_translator("en").gettext
            >>> msg = gettext("Hello World!")
            >>> print(msg)
            Hello World!

        Args:
            lang_code: Language code.

        Returns:
            Object of translation for the desired language.
        """
        return cls.custom_translations.get(
            lang_code,
            cls.custom_translations[cls.DEFAULT_LOCALE],
        )

    @classmethod
    def change_locale(cls, lang_code: str) -> None:
        """Change current language.

        Examples:
            >>> from ramifice.translations import Translations
            >>> Translations.change_locale("ru")

        Args:
            lang_code: Language code.

        Returns:
            Object `None`.
        """
        if lang_code != cls.CURRENT_LOCALE:
            cls.CURRENT_LOCALE = lang_code if lang_code in cls.LANGUAGES else cls.DEFAULT_LOCALE
            cls._ = cls.get_ramifice_translator(cls.CURRENT_LOCALE).gettext
            translator: NullTranslations = cls.get_custom_translator(cls.CURRENT_LOCALE)
            cls.gettext = translator.gettext
            cls.ngettext = translator.ngettext

    @classmethod
    def init_params(cls) -> None:
        """Method for general initialization of parameters."""
        cls._ = cls.get_ramifice_translator(cls.DEFAULT_LOCALE).gettext
        cls.gettext = cls.get_custom_translator(cls.DEFAULT_LOCALE).gettext
        cls.ngettext = cls.get_custom_translator(cls.DEFAULT_LOCALE).ngettext

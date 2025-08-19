"""Localization of translations.

The module contains the following variables:

- `CURRENT_LOCALE` - Code of current language.
- `DEFAULT_LOCALE` - Language code by default.
- `LANGUAGES` - List of codes supported by languages.
- `gettext` - The object of the current translator.
- `ngettext` - The object of the current translator.

The module contains the following functions:

- `change_locale` - To change the current language and translation object.

CKEditor supported languages:

af | ar | ast | az | bg | ca | cs | da | de | de_ch | el | en | en_au |
en_gb | eo | es | et | eu | fa | fi | fr | gl | gu | he | hi |
hr | hu | id | it | ja | km | kn | ko | ku | lt | lv | ms |
nb | ne | nl | no | oc | pl | pt | pt_br | ro | ru | si | sk |
sl | sq | sr | sr_latn | sv | th | tk | tr | tt | ug | uk | vi |
zh | zh_cn
"""

from __future__ import annotations

__all__ = (
    "DEFAULT_LOCALE",
    "CURRENT_LOCALE",
    "LANGUAGES",
    "add_languages",
    "_",
    "gettext",
    "ngettext",
    "change_locale",
)

import copy
import gettext as _gettext
import logging
from gettext import NullTranslations
from typing import Any

from ramifice.utils.errors import PanicError

logger = logging.getLogger(__name__)

# Language by default.
DEFAULT_LOCALE: str = "en"
# Code of current language.
CURRENT_LOCALE: str = copy.deepcopy(DEFAULT_LOCALE)
# List of supported languages.
LANGUAGES: frozenset[str] = frozenset(("en", "ru"))


def add_languages(
    default_locale: str,
    languages: frozenset[str],
) -> None:
    """Add languages."""
    global DEFAULT_LOCALE, LANGUAGES  # noqa: PLW0603
    if default_locale not in languages:
        msg = "DEFAULT_LOCALE is not included in the LANGUAGES!"
        logger.critical(msg)
        raise PanicError(msg)
    DEFAULT_LOCALE = default_locale
    LANGUAGES = languages


# Add translations for Ramifice.
ramifice_translations: dict[str, NullTranslations] = {
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
custom_translations: dict[str, NullTranslations] = {
    lang: _gettext.translation(
        domain="messages",
        localedir="config/translations/custom",
        languages=[lang],
        class_=None,
        fallback=True,
    )
    for lang in LANGUAGES
}


def get_ramifice_translator(lang_code: str) -> Any:
    """Get an object of translation for the desired language, for Ramifice.

    Examples:
        >>> from ramifice import translations
        >>> _ = translations.get_ramifice_translator("en").gettext
        >>> msg = _("Hello World!")
        >>> print(msg)
        Hello World!

    Args:
        lang_code: Language code.

    Returns:
        Object of translation for the desired language.
    """
    return ramifice_translations.get(
        lang_code,
        ramifice_translations[DEFAULT_LOCALE],
    )


def get_custom_translator(lang_code: str) -> Any:
    """Get an object of translation for the desired language, for custom project.

    Examples:
        >>> from ramifice import translations
        >>> gettext = translations.get_custom_translator("en").gettext
        >>> msg = gettext("Hello World!")
        >>> print(msg)
        Hello World!

    Args:
        lang_code: Language code.

    Returns:
        Object of translation for the desired language.
    """
    return custom_translations.get(
        lang_code,
        custom_translations[DEFAULT_LOCALE],
    )


# The object of the current translation, for Ramifice.
_: Any = get_ramifice_translator(DEFAULT_LOCALE).gettext

# The object of the current translation, for custom project.
gettext: Any = get_custom_translator(DEFAULT_LOCALE).gettext
ngettext: Any = get_custom_translator(DEFAULT_LOCALE).ngettext


def change_locale(lang_code: str) -> None:
    """Change current language.

    Examples:
        >>> from ramifice import translations
        >>> translations.change_locale("ru")

    Args:
        lang_code: Language code.

    Returns:
        Object `None`.
    """
    global CURRENT_LOCALE, _, gettext, ngettext  # noqa: PLW0603
    if lang_code != CURRENT_LOCALE:
        CURRENT_LOCALE = lang_code if lang_code in LANGUAGES else DEFAULT_LOCALE
        _ = get_ramifice_translator(CURRENT_LOCALE).gettext
        translator: NullTranslations = get_custom_translator(CURRENT_LOCALE)
        gettext = translator.gettext
        ngettext = translator.ngettext

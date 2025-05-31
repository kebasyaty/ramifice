"""For localization of translations.

The module contains the following variables:

- `CURRENT_LOCALE` - Code of current language.
- `DEFAULT_LOCALE` - Language code by default.
- `LANGUAGES` - List of supported languages.
- `translations` - List of translations
- `gettext` - The object of the current translation.

The module contains the following functions:

- `get_translator` - Get an object of translation for the desired language.
- `change_locale` - To change the current language and translation object.
"""

import gettext

CURRENT_LOCALE: str = "en"
DEFAULT_LOCALE: str = "en"
LANGUAGES: list[str] = ["en", "ru"]

translations = {
    lang: gettext.translation(
        domain="messages",
        localedir="config/translations/ramifice",
        languages=[lang],
        class_=None,
        fallback=True,
    )
    for lang in LANGUAGES
}


def get_translator(lang_code: str):
    return translations.get(lang_code, translations[DEFAULT_LOCALE])


gettext = get_translator(DEFAULT_LOCALE).gettext


def change_locale(lang_code: str):
    """Change current locale."""
    global CURRENT_LOCALE, gettext
    if lang_code != CURRENT_LOCALE:
        CURRENT_LOCALE = lang_code if lang_code in LANGUAGES else DEFAULT_LOCALE
        gettext = get_translator(CURRENT_LOCALE).gettext

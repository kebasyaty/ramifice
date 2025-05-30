"""For localization of translations."""

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

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


def get_translator(lang: str = CURRENT_LOCALE):
    return translations.get(lang, translations[DEFAULT_LOCALE])


def add_current_locale(lang_code: str):
    """Add current locale."""
    global CURRENT_LOCALE, gettext
    CURRENT_LOCALE = lang_code if lang_code in LANGUAGES else DEFAULT_LOCALE
    gettext = get_translator().gettext


gettext = get_translator().gettext

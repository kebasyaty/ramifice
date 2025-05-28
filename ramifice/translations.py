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

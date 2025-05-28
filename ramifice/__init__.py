# Copyright 2018-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""ORM-like API MongoDB for Python language."""

import gettext

from . import store
from .decor_model import model

LANGUAGES: list[str] = ["en", "ru"]
DEFAULT_LOCALE: str = "en"


def add_current_locale(lang_code: str = "en"):
    """Add current locale."""
    store.CURRENT_LOCALE = lang_code if lang_code in LANGUAGES else "en"


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


def get_translator(lang: str):
    return translations.get(lang, translations[DEFAULT_LOCALE])

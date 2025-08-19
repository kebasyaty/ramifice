"""Testing the module  `ramifice > translations`."""

from __future__ import annotations

import unittest

from ramifice import model
from ramifice.fields import EmailField
from ramifice.utils import translations


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self):
        """Adding fields."""
        self.email = EmailField()


class TestTranslations(unittest.TestCase):
    """Testing the module  `ramifice > translations`."""

    def test_add_languages(self):
        """Testing `add_languages`."""
        translations.add_languages(
            default_locale="en",
            languages=frozenset(("en", "ru")),
        )

    def test_change_locale(self):
        """Testing `change_locale` method."""
        self.assertEqual(translations._("Document ID"), "Document ID")
        self.assertEqual(translations.gettext("Document ID"), "Document ID")
        translations.change_locale("ru")
        self.assertEqual(translations._("Document ID"), "Идентификатор документа")

        user = User()

        self.assertEqual(user.id.label, "Идентификатор документа")
        self.assertEqual(user.id.placeholder, "Он добавляется автоматически")
        self.assertEqual(user.id.hint, "Он добавляется автоматически")

        self.assertEqual(user.created_at.label, "Создан")
        self.assertEqual(user.created_at.placeholder, "Он добавляется автоматически")
        self.assertEqual(user.created_at.hint, "Он добавляется автоматически")
        self.assertEqual(user.created_at.warning, ["Когда был создан документ."])

        self.assertEqual(user.updated_at.label, "Обновлен")
        self.assertEqual(user.updated_at.placeholder, "Он добавляется автоматически")
        self.assertEqual(user.updated_at.hint, "Он добавляется автоматически")
        self.assertEqual(user.updated_at.warning, ["Когда был обновлен документ."])

        self.assertEqual(user.email.label, "")
        self.assertEqual(user.email.placeholder, "")
        self.assertEqual(user.email.hint, "")


if __name__ == "__main__":
    unittest.main()

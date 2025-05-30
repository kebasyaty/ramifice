"""Testing  ramifice > translations."""

import unittest

from ramifice import model, translations
from ramifice.fields import EmailField


@model(service_name="Accounts")
class User:
    """Model for testing."""

    def fields(self, gettext):
        self.email = EmailField()


class TestTranslations(unittest.TestCase):
    """Testing  ramifice > translations."""

    def test_change_locale(self):
        """Testing `change_locale` method."""
        translations.change_locale("ru")

        user = User()

        self.assertEqual(user._id.label, "Идентификатор документа")
        self.assertEqual(user._id.placeholder, "Он добавляется автоматически")
        self.assertEqual(user._id.hint, "Он добавляется автоматически")

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

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
        self.assertEqual(user.email.label, "Адрес электронной почты")
        self.assertEqual(user.email.placeholder, "Введите адрес электронной почты")
        self.assertEqual(user.email.hint, "Введите адрес электронной почты")


if __name__ == "__main__":
    unittest.main()

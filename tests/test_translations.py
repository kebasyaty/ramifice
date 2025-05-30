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
        self.assertEqual(user._id.placeholder, "")
        self.assertEqual(user._id.hint, "")

        self.assertEqual(user.email.label, "")
        self.assertEqual(user.email.placeholder, "")
        self.assertEqual(user.email.hint, "")


if __name__ == "__main__":
    unittest.main()

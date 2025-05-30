"""Testing  ramifice > translations."""

import unittest

from ramifice.fields import EmailField


class TestTranslations(unittest.TestCase):
    """Testing  ramifice > translations."""

    def test_add_current_locale(self):
        """Testing `add_current_locale` method."""
        f = EmailField()
        self.assertEqual(f.label, "Email address")
        self.assertEqual(f.placeholder, "Enter email address")
        self.assertEqual(f.hint, "Enter email address")


if __name__ == "__main__":
    unittest.main()

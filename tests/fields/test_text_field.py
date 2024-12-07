"""Testing TextField."""

import unittest
from ramifice.fields import text_field


class TestTextField(unittest.TestCase):
    """Testing TextField."""

    def test_attributes_by_default(self):
        """Testing atrabuts with default values."""
        f = text_field.TextField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "TextField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 1)


if __name__ == '__main__':
    unittest.main()

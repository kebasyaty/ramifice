"""Testing text fields."""

import unittest
from ramifice.fields import fields


class TestTextFields(unittest.TestCase):
    """Testing parameters with default values."""

    def test_attributes_by_default(self):
        """Testing a parameters for TextField."""
        f = fields.TextField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "TextField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "text")
        self.assertEqual(f.input_type, "text")


if __name__ == '__main__':
    unittest.main()

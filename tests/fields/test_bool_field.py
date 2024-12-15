"""Testing a parameters with default values for logical (boolean) field."""

import unittest
from ramifice.fields import BoolField


class TestBooleanFields(unittest.TestCase):
    """Testing parameters with default values."""

    def test_bool_field(self):
        """Testing a parameters by default for BoolField."""
        f = BoolField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "BoolField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'bool')
        self.assertEqual(f.input_type, 'checkbox')
        self.assertIsNone(f.value)
        self.assertFalse(f.default)


if __name__ == '__main__':
    unittest.main()

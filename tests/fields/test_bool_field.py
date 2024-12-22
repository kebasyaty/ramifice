"""Testing logical (boolean) field."""

import unittest

from ramifice.fields import BoolField


class TestBooleanField(unittest.TestCase):
    """Testing logical (boolean) field"""

    def test_bool_field(self):
        """Testing `BoolField`."""
        # Parameters by default:
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
        self.assertEqual(f.group, "bool")
        self.assertEqual(f.input_type, "checkbox")
        self.assertIsNone(f.value)
        self.assertFalse(f.default)
        # Additional check:
        with self.assertRaises(AssertionError):
            BoolField(default=0)
        with self.assertRaises(AssertionError):
            BoolField(default="False")
        BoolField(default=True)


if __name__ == "__main__":
    unittest.main()

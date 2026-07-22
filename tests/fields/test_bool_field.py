"""Testing boolean field."""

from __future__ import annotations

import unittest

from ramifice.fields import BooleanField


class TestBooleanField(unittest.TestCase):
    """Testing boolean field."""

    def test_boolean_field(self):
        """Testing `BooleanField`."""
        # Parameters by default:
        f = BooleanField()
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "BooleanField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.group, "bool")
        self.assertEqual(f.field_attrs.input_type, "checkbox")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertIsNone(f.field_attrs.value)
        self.assertFalse(f.field_attrs.default)
        # Exception checking:
        with self.assertRaises(AssertionError):
            BooleanField(default=0)
        with self.assertRaises(AssertionError):
            BooleanField(default="False")
        BooleanField(default=True)


if __name__ == "__main__":
    unittest.main()

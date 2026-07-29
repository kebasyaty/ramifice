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
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "BooleanField")
        self.assertFalse(f.field_core.is_disable)
        self.assertFalse(f.field_core.is_hide)
        self.assertFalse(f.field_core.is_ignore)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "bool")
        self.assertEqual(f.field_core.input_type, "checkbox")
        self.assertEqual(f.field_core.hint, "")
        self.assertIsNone(f.field_core.value)
        self.assertFalse(f.field_core.default)
        # Exception checking:
        with self.assertRaises(AssertionError):
            BooleanField(default=0)
        with self.assertRaises(AssertionError):
            BooleanField(default="False")
        BooleanField(default=True)


if __name__ == "__main__":
    unittest.main()

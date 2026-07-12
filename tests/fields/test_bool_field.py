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
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "BooleanField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertIsNone(f.html_attrs["warning"])
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "bool")
        self.assertEqual(f.html_attrs["input_type"], "checkbox")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertIsNone(f.html_attrs["value"])
        self.assertFalse(f.html_attrs["default"])
        # Exception checking:
        with self.assertRaises(AssertionError):
            BooleanField(default=0)
        with self.assertRaises(AssertionError):
            BooleanField(default="False")
        BooleanField(default=True)


if __name__ == "__main__":
    unittest.main()

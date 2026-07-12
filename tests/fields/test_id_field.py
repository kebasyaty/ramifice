"""Testing ID field."""

from __future__ import annotations

import unittest

from ramifice.fields import IDField


class TestHashField(unittest.TestCase):
    """Testing ID field."""

    def test_id_field(self):
        """Testing `IDField`."""
        # Parameters by default:
        f = IDField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "IDField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertIsNone(f.html_attrs["warning"])
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["alerts"], [])
        self.assertEqual(f.html_attrs["group"], "id")
        self.assertEqual(f.html_attrs["input_type"], "text")
        self.assertIsNone(f.html_attrs["value"])
        self.assertEqual(f.html_attrs["placeholder"], "")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertFalse(f.html_attrs["readonly"])
        self.assertFalse(f.html_attrs["unique"])


if __name__ == "__main__":
    unittest.main()

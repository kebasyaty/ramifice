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
        self.assertEqual(f.field_attrs.id, "")
        self.assertEqual(f.field_attrs.label, "")
        self.assertEqual(f.field_attrs.name, "")
        self.assertEqual(f.field_attrs.field_type, "IDField")
        self.assertFalse(f.field_attrs.disabled)
        self.assertFalse(f.field_attrs.hide)
        self.assertFalse(f.field_attrs.ignored)
        self.assertEqual(len(f.field_attrs.warning), 0)
        self.assertEqual(f.field_attrs.errors, [])
        self.assertEqual(f.field_attrs.alerts, [])
        self.assertEqual(f.field_attrs.group, "id")
        self.assertEqual(f.field_attrs.input_type, "text")
        self.assertIsNone(f.field_attrs.value)
        self.assertEqual(f.field_attrs.placeholder, "")
        self.assertEqual(f.field_attrs.hint, "")
        self.assertFalse(f.field_attrs.required)
        self.assertFalse(f.field_attrs.readonly)
        self.assertFalse(f.field_attrs.unique)


if __name__ == "__main__":
    unittest.main()

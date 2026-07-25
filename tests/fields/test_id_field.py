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
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "IDField")
        self.assertFalse(f.field_core.disabled)
        self.assertFalse(f.field_core.hide)
        self.assertFalse(f.field_core.ignored)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.alerts, [])
        self.assertEqual(f.field_core.group, "id")
        self.assertEqual(f.field_core.input_type, "text")
        self.assertIsNone(f.field_core.value)
        self.assertEqual(f.field_core.placeholder, "")
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.required)
        self.assertFalse(f.field_core.readonly)
        self.assertFalse(f.field_core.unique)


if __name__ == "__main__":
    unittest.main()

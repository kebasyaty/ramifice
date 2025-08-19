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
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "IDField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertEqual(f.errors, [])
        self.assertEqual(f.alerts, [])
        self.assertEqual(f.group, "id")
        self.assertEqual(f.input_type, "text")
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertEqual(f.hint, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)


if __name__ == "__main__":
    unittest.main()

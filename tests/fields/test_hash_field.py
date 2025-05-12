"""Testing hash field."""

import unittest

from ramifice.fields import HashField


class TestHashField(unittest.TestCase):
    """Testing hash field."""

    def test_hash_field(self):
        """Testing `HashField`."""
        # Parameters by default:
        f = HashField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "HashField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertEqual(f.errors, [])
        self.assertEqual(f.alerts, [])
        self.assertEqual(f.group, "hash")
        self.assertEqual(f.input_type, "text")
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)


if __name__ == "__main__":
    unittest.main()

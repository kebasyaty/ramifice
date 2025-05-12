"""Testing the module `ramifice.types`."""

import unittest

from ramifice.types import Unit


class TestTypes(unittest.TestCase):
    """Testing the module `ramifice.types`."""

    def test_unit(self):
        """Testing a class `Unit`."""
        u = Unit(field="field_name", title="Title", value="value")
        self.assertEqual(u.field, "field_name")
        self.assertEqual(u.title, "Title")
        self.assertEqual(u.value, "value")
        self.assertFalse(u.is_delete)
        u = Unit(field="field_name", title="Title", value="value", is_delete=True)
        self.assertEqual(u.field, "field_name")
        self.assertEqual(u.title, "Title")
        self.assertEqual(u.value, "value")
        self.assertTrue(u.is_delete)


if __name__ == "__main__":
    unittest.main()

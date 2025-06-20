"""Testing the module `ramifice.types`."""

import unittest

from ramifice.errors import PanicError
from ramifice.unit import Unit


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

        # Check the match of types.
        with self.assertRaises(PanicError):
            Unit(field=None, title="Title", value="value", is_delete=True)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title=None, value="value", is_delete=True)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title="Title", value=None, is_delete=True)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title="Title", value="value", is_delete=None)

        # Check empty arguments
        with self.assertRaises(PanicError):
            Unit(field="", title="Title", value="value", is_delete=True)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title="", value="value", is_delete=True)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title="Title", value="", is_delete=True)


if __name__ == "__main__":
    unittest.main()

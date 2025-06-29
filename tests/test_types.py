"""Testing the module `ramifice.types`."""

import unittest

from ramifice.utils.errors import PanicError
from ramifice.utils.unit import Unit


class TestTypes(unittest.TestCase):
    """Testing the module `ramifice.types`."""

    def test_unit(self):
        """Testing a class `Unit`."""
        u = Unit(field="field_name", title={"en": "Title"}, value="value")
        self.assertEqual(u.field, "field_name")
        self.assertEqual(u.title, {"en": "Title"})
        self.assertEqual(u.value, "value")
        self.assertFalse(u.is_delete)

        u = Unit(field="field_name", title={"en": "Title"}, is_delete=True)
        self.assertEqual(u.field, "field_name")
        self.assertEqual(u.title, {"en": "Title"})
        self.assertIsNone(u.value)
        self.assertTrue(u.is_delete)

        # Check the match of types.
        with self.assertRaises(PanicError):
            Unit(field=None, title={"en": "Title"}, value="value", is_delete=True)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title=None, value="value", is_delete=True)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title={"en": "Title"}, value=None, is_delete=False)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title={"en": "Title"}, value="value", is_delete=None)

        # Check empty arguments
        with self.assertRaises(PanicError):
            Unit(field="", title={"en": "Title"}, value="value", is_delete=True)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title="", value="value", is_delete=True)
        with self.assertRaises(PanicError):
            Unit(field="field_name", title={"en": "Title"}, value="", is_delete=True)


if __name__ == "__main__":
    unittest.main()

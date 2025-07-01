"""Testing selective integer fields."""

import unittest

from ramifice.fields import (
    ChoiceIntDynField,
    ChoiceIntField,
    ChoiceIntMultDynField,
    ChoiceIntMultField,
)


class TestChoiceIntegerFields(unittest.TestCase):
    """Testing selective integer fields."""

    def test_choice_int_field(self):
        """Testing `ChoiceIntField`."""
        # Parameters by default:
        f = ChoiceIntField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "ChoiceIntField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "choice")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertEqual(f.hint, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertFalse(f.multiple)
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceIntField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceIntField(default="2")
        with self.assertRaises(AssertionError):
            f = ChoiceIntField(default=3, choices=[(1, "Title"), (2, "Title 2")])
        # Methods:
        f = ChoiceIntField()
        self.assertTrue(f.has_value())
        f = ChoiceIntField(default=2, choices=[(1, "Title"), (2, "Title 2")])
        self.assertTrue(f.has_value())
        f = ChoiceIntField(choices=[(1, "Title"), (2, "Title 2")])
        self.assertTrue(f.has_value())
        f.value = 2
        self.assertTrue(f.has_value())
        f.value = 3
        self.assertFalse(f.has_value())

    def test_choice_int_mult_field(self):
        """Testing `ChoiceIntMultField`."""
        # Parameters by default:
        f = ChoiceIntMultField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "ChoiceIntMultField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "choice")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertEqual(f.hint, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertTrue(f.multiple)
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(choices=[])
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(default="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(default=[])
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(default=[3], choices=[(1, "Title"), (2, "Title 2")])
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(default=[2, 3], choices=[(1, "Title"), (2, "Title 2")])
        # Methods:
        f = ChoiceIntMultField()
        self.assertTrue(f.has_value())
        f = ChoiceIntMultField(default=[2], choices=[(1, "Title"), (2, "Title 2")])
        self.assertTrue(f.has_value())
        f = ChoiceIntMultField(choices=[(1, "Title"), (2, "Title 2")])
        self.assertTrue(f.has_value())
        f.value = [2]
        self.assertTrue(f.has_value())
        f.value = [3]
        self.assertFalse(f.has_value())
        f.value = [2, 3]
        self.assertFalse(f.has_value())

    def test_choice_int_dyn_field(self):
        """Testing `ChoiceIntDynField`."""
        # Parameters by default:
        f = ChoiceIntDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "ChoiceIntDynField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "choice")
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertEqual(f.hint, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertFalse(f.multiple)

    def test_choice_int_mult_dyn_field(self):
        """Testing `ChoiceIntMultDynField`."""
        # Parameters by default:
        f = ChoiceIntMultDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "ChoiceIntMultDynField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "choice")
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertEqual(f.hint, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertTrue(f.multiple)


if __name__ == "__main__":
    unittest.main()

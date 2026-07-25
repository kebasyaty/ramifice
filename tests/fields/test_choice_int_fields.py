"""Testing selective integer fields."""

from __future__ import annotations

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
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceIntField")
        self.assertFalse(f.field_core.disabled)
        self.assertFalse(f.field_core.hide)
        self.assertFalse(f.field_core.ignored)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "choice")
        self.assertIsNone(f.field_core.value)
        self.assertIsNone(f.field_core.default)
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.required)
        self.assertFalse(f.field_core.readonly)
        self.assertFalse(f.field_core.unique)
        self.assertFalse(f.field_core.multiple)
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceIntField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceIntField(default="2")
        with self.assertRaises(AssertionError):
            f = ChoiceIntField(default=3, choices=[[1, "Title"], [2, "Title 2"]])
        # Methods:
        f = ChoiceIntField()
        self.assertTrue(f.has_value())
        f = ChoiceIntField(default=2, choices=[[1, "Title"], [2, "Title 2"]])
        self.assertTrue(f.has_value())
        f = ChoiceIntField(choices=[[1, "Title"], [2, "Title 2"]])
        self.assertTrue(f.has_value())
        f.field_core.value = 2
        self.assertTrue(f.has_value())
        f.field_core.value = 3
        self.assertFalse(f.has_value())

    def test_choice_int_mult_field(self):
        """Testing `ChoiceIntMultField`."""
        # Parameters by default:
        f = ChoiceIntMultField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceIntMultField")
        self.assertFalse(f.field_core.disabled)
        self.assertFalse(f.field_core.hide)
        self.assertFalse(f.field_core.ignored)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "choice")
        self.assertIsNone(f.field_core.value)
        self.assertIsNone(f.field_core.default)
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.required)
        self.assertFalse(f.field_core.readonly)
        self.assertFalse(f.field_core.unique)
        self.assertTrue(f.field_core.multiple)
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
            f = ChoiceIntMultField(default=[3], choices=[[1, "Title"], [2, "Title 2"]])
        with self.assertRaises(AssertionError):
            f = ChoiceIntMultField(default=[2, 3], choices=[[1, "Title"], [2, "Title 2"]])
        # Methods:
        f = ChoiceIntMultField()
        self.assertTrue(f.has_value())
        f = ChoiceIntMultField(default=[2], choices=[[1, "Title"], [2, "Title 2"]])
        self.assertTrue(f.has_value())
        f = ChoiceIntMultField(choices=[[1, "Title"], [2, "Title 2"]])
        self.assertTrue(f.has_value())
        f.field_core.value = [2]
        self.assertTrue(f.has_value())
        f.field_core.value = [3]
        self.assertFalse(f.has_value())
        f.field_core.value = [2, 3]
        self.assertFalse(f.has_value())

    def test_choice_int_dyn_field(self):
        """Testing `ChoiceIntDynField`."""
        # Parameters by default:
        f = ChoiceIntDynField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceIntDynField")
        self.assertFalse(f.field_core.disabled)
        self.assertFalse(f.field_core.hide)
        self.assertFalse(f.field_core.ignored)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "choice")
        self.assertIsNone(f.field_core.value)
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.required)
        self.assertFalse(f.field_core.readonly)
        self.assertFalse(f.field_core.unique)
        self.assertFalse(f.field_core.multiple)

    def test_choice_int_mult_dyn_field(self):
        """Testing `ChoiceIntMultDynField`."""
        # Parameters by default:
        f = ChoiceIntMultDynField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceIntMultDynField")
        self.assertFalse(f.field_core.disabled)
        self.assertFalse(f.field_core.hide)
        self.assertFalse(f.field_core.ignored)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "choice")
        self.assertIsNone(f.field_core.value)
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.required)
        self.assertFalse(f.field_core.readonly)
        self.assertFalse(f.field_core.unique)
        self.assertTrue(f.field_core.multiple)


if __name__ == "__main__":
    unittest.main()

"""Testing selective float fields."""

from __future__ import annotations

import unittest

from ramifice.fields import (
    ChoiceFloatDynField,
    ChoiceFloatField,
    ChoiceFloatMultDynField,
    ChoiceFloatMultField,
)


class TestChoiceFloatFields(unittest.TestCase):
    """Testing selective float fields."""

    def test_choice_float_field(self):
        """Testing `ChoiceFloatField`."""
        # Parameters by default:
        f = ChoiceFloatField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceFloatField")
        self.assertFalse(f.field_core.is_disable)
        self.assertFalse(f.field_core.is_hide)
        self.assertFalse(f.field_core.is_ignore)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "choice")
        self.assertIsNone(f.field_core.value)
        self.assertIsNone(f.field_core.default)
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.is_require)
        self.assertFalse(f.field_core.is_readonly)
        self.assertFalse(f.field_core.is_unique)
        self.assertFalse(f.field_core.is_multiple)
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceFloatField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatField(default="2.0")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatField(default=3.0, choices=[[1.0, "Title"], [2.0, "Title 2"]])
        # Methods:
        f = ChoiceFloatField()
        self.assertTrue(f.field_core.has_value())
        f = ChoiceFloatField(default=2.0, choices=[[1.0, "Title"], [2.0, "Title 2"]])
        self.assertTrue(f.field_core.has_value())
        f = ChoiceFloatField(choices=[[1.0, "Title"], [2.0, "Title 2"]])
        self.assertTrue(f.field_core.has_value())
        f.field_core.value = 2.0
        self.assertTrue(f.field_core.has_value())
        f.field_core.value = 3.0
        self.assertFalse(f.field_core.has_value())

    def test_choice_float_mult_field(self):
        """Testing `ChoiceFloatMultField`."""
        # Parameters by default:
        f = ChoiceFloatMultField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceFloatMultField")
        self.assertFalse(f.field_core.is_disable)
        self.assertFalse(f.field_core.is_hide)
        self.assertFalse(f.field_core.is_ignore)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "choice")
        self.assertIsNone(f.field_core.value)
        self.assertIsNone(f.field_core.default)
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.is_require)
        self.assertFalse(f.field_core.is_readonly)
        self.assertFalse(f.field_core.is_unique)
        self.assertTrue(f.field_core.is_multiple)
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(choices=[])
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(default="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(default=[])
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(default=[3.0], choices=[[1.0, "Title"], [2.0, "Title 2"]])
        with self.assertRaises(AssertionError):
            f = ChoiceFloatMultField(default=[2.0, 3.0], choices=[[1.0, "Title"], [2.0, "Title 2"]])
        # Methods:
        f = ChoiceFloatMultField()
        self.assertTrue(f.field_core.has_value())
        f = ChoiceFloatMultField(default=[2.0], choices=[[1.0, "Title"], [2.0, "Title 2"]])
        self.assertTrue(f.field_core.has_value())
        f = ChoiceFloatMultField(choices=[[1.0, "Title"], [2.0, "Title 2"]])
        self.assertTrue(f.field_core.has_value())
        f.field_core.value = [2.0]
        self.assertTrue(f.field_core.has_value())
        f.field_core.value = [3.0]
        self.assertFalse(f.field_core.has_value())
        f.field_core.value = [2.0, 3.0]
        self.assertFalse(f.field_core.has_value())

    def test_choice_float_dyn_field(self):
        """Testing `ChoiceFloatDynField`."""
        # Parameters by default:
        f = ChoiceFloatDynField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceFloatDynField")
        self.assertFalse(f.field_core.is_disable)
        self.assertFalse(f.field_core.is_hide)
        self.assertFalse(f.field_core.is_ignore)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "choice")
        self.assertIsNone(f.field_core.value)
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.is_require)
        self.assertFalse(f.field_core.is_readonly)
        self.assertFalse(f.field_core.is_unique)
        self.assertFalse(f.field_core.is_multiple)

    def test_choice_float_mult_dyn_field(self):
        """Testing `ChoiceFloatMultDynField`."""
        # Parameters by default:
        f = ChoiceFloatMultDynField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceFloatMultDynField")
        self.assertFalse(f.field_core.is_disable)
        self.assertFalse(f.field_core.is_hide)
        self.assertFalse(f.field_core.is_ignore)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "choice")
        self.assertIsNone(f.field_core.value)
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.is_require)
        self.assertFalse(f.field_core.is_readonly)
        self.assertFalse(f.field_core.is_unique)
        self.assertTrue(f.field_core.is_multiple)


if __name__ == "__main__":
    unittest.main()

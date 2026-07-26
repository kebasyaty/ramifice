"""Testing selective text fields."""

from __future__ import annotations

import unittest

from ramifice.fields import (
    ChoiceTextDynField,
    ChoiceTextField,
    ChoiceTextMultDynField,
    ChoiceTextMultField,
)


class TestChoiceTextFields(unittest.TestCase):
    """Testing selective text fields."""

    def test_choice_text_field(self):
        """Testing `ChoiceTextField`."""
        # Parameters by default:
        f = ChoiceTextField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceTextField")
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
        self.assertFalse(f.field_core.multiple)
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceTextField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceTextField(default=2)
        with self.assertRaises(AssertionError):
            f = ChoiceTextField(default="")
        with self.assertRaises(AssertionError):
            f = ChoiceTextField(
                default="value 3",
                choices=[["value", "Title"], ["value 2", "Title 2"]],
            )
        # Methods:
        f = ChoiceTextField()
        self.assertTrue(f.field_core.has_value())
        f = ChoiceTextField(default="value 2", choices=[["value", "Title"], ["value 2", "Title 2"]])
        self.assertTrue(f.field_core.has_value())
        f = ChoiceTextField(choices=[["value", "Title"], ["value 2", "Title 2"]])
        self.assertTrue(f.field_core.has_value())
        f.field_core.value = "value 2"
        self.assertTrue(f.field_core.has_value())
        f.field_core.value = "value 3"
        self.assertFalse(f.field_core.has_value())

    def test_choice_text_mult_field(self):
        """Testing `ChoiceTextMultField`."""
        # Parameters by default:
        f = ChoiceTextMultField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceTextMultField")
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
        self.assertTrue(f.field_core.multiple)
        # Exception checking:
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(choices="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(choices={})
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(default="not list")
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(default=[])
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(
                default=["value 3"],
                choices=[["value", "Title"], ["value 2", "Title 2"]],
            )
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(
                default=["value 2", "value 3"],
                choices=[["value", "Title"], ["value 2", "Title 2"]],
            )
        # Methods:
        f = ChoiceTextMultField()
        self.assertTrue(f.field_core.has_value())
        f = ChoiceTextMultField(
            default=["value 2"],
            choices=[["value", "Title"], ["value 2", "Title 2"]],
        )
        self.assertTrue(f.field_core.has_value())
        f = ChoiceTextMultField(choices=[["value", "Title"], ["value 2", "Title 2"]])
        self.assertTrue(f.field_core.has_value())
        f.field_core.value = ["value 2"]
        self.assertTrue(f.field_core.has_value())
        f.field_core.value = ["value 3"]
        self.assertFalse(f.field_core.has_value())
        f.field_core.value = ["value 2", "value 3"]
        self.assertFalse(f.field_core.has_value())

    def test_choice_text_dyn_field(self):
        """Testing `ChoiceTextDynField`."""
        # Parameters by default:
        f = ChoiceTextDynField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceTextDynField")
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
        self.assertFalse(f.field_core.multiple)

    def test_choice_text_mult_dyn_field(self):
        """Testing `ChoiceTextMultDynField`."""
        # Parameters by default:
        f = ChoiceTextMultDynField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "ChoiceTextMultDynField")
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
        self.assertTrue(f.field_core.multiple)


if __name__ == "__main__":
    unittest.main()

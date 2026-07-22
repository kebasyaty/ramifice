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
        self.assertEqual(f.html_attrs.id, "")
        self.assertEqual(f.html_attrs.label, "")
        self.assertEqual(f.html_attrs.name, "")
        self.assertEqual(f.html_attrs.field_type, "ChoiceTextField")
        self.assertFalse(f.html_attrs.disabled)
        self.assertFalse(f.html_attrs.hide)
        self.assertFalse(f.html_attrs.ignored)
        self.assertEqual(len(f.html_attrs.warning), 0)
        self.assertEqual(f.html_attrs.errors, [])
        self.assertEqual(f.html_attrs.group, "choice")
        self.assertIsNone(f.html_attrs.value)
        self.assertIsNone(f.html_attrs.default)
        self.assertEqual(f.html_attrs.hint, "")
        self.assertFalse(f.html_attrs.required)
        self.assertFalse(f.html_attrs.readonly)
        self.assertFalse(f.html_attrs.unique)
        self.assertFalse(f.html_attrs.multiple)
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
        self.assertTrue(f.has_value())
        f = ChoiceTextField(default="value 2", choices=[["value", "Title"], ["value 2", "Title 2"]])
        self.assertTrue(f.has_value())
        f = ChoiceTextField(choices=[["value", "Title"], ["value 2", "Title 2"]])
        self.assertTrue(f.has_value())
        f.html_attrs.value = "value 2"
        self.assertTrue(f.has_value())
        f.html_attrs.value = "value 3"
        self.assertFalse(f.has_value())

    def test_choice_text_mult_field(self):
        """Testing `ChoiceTextMultField`."""
        # Parameters by default:
        f = ChoiceTextMultField()
        self.assertEqual(f.html_attrs.id, "")
        self.assertEqual(f.html_attrs.label, "")
        self.assertEqual(f.html_attrs.name, "")
        self.assertEqual(f.html_attrs.field_type, "ChoiceTextMultField")
        self.assertFalse(f.html_attrs.disabled)
        self.assertFalse(f.html_attrs.hide)
        self.assertFalse(f.html_attrs.ignored)
        self.assertEqual(len(f.html_attrs.warning), 0)
        self.assertEqual(f.html_attrs.errors, [])
        self.assertEqual(f.html_attrs.group, "choice")
        self.assertIsNone(f.html_attrs.value)
        self.assertIsNone(f.html_attrs.default)
        self.assertEqual(f.html_attrs.hint, "")
        self.assertFalse(f.html_attrs.required)
        self.assertFalse(f.html_attrs.readonly)
        self.assertFalse(f.html_attrs.unique)
        self.assertTrue(f.html_attrs.multiple)
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
        self.assertTrue(f.has_value())
        f = ChoiceTextMultField(
            default=["value 2"],
            choices=[["value", "Title"], ["value 2", "Title 2"]],
        )
        self.assertTrue(f.has_value())
        f = ChoiceTextMultField(choices=[["value", "Title"], ["value 2", "Title 2"]])
        self.assertTrue(f.has_value())
        f.html_attrs.value = ["value 2"]
        self.assertTrue(f.has_value())
        f.html_attrs.value = ["value 3"]
        self.assertFalse(f.has_value())
        f.html_attrs.value = ["value 2", "value 3"]
        self.assertFalse(f.has_value())

    def test_choice_text_dyn_field(self):
        """Testing `ChoiceTextDynField`."""
        # Parameters by default:
        f = ChoiceTextDynField()
        self.assertEqual(f.html_attrs.id, "")
        self.assertEqual(f.html_attrs.label, "")
        self.assertEqual(f.html_attrs.name, "")
        self.assertEqual(f.html_attrs.field_type, "ChoiceTextDynField")
        self.assertFalse(f.html_attrs.disabled)
        self.assertFalse(f.html_attrs.hide)
        self.assertFalse(f.html_attrs.ignored)
        self.assertEqual(len(f.html_attrs.warning), 0)
        self.assertEqual(f.html_attrs.errors, [])
        self.assertEqual(f.html_attrs.group, "choice")
        self.assertIsNone(f.html_attrs.value)
        self.assertEqual(f.html_attrs.hint, "")
        self.assertFalse(f.html_attrs.required)
        self.assertFalse(f.html_attrs.readonly)
        self.assertFalse(f.html_attrs.unique)
        self.assertFalse(f.html_attrs.multiple)

    def test_choice_text_mult_dyn_field(self):
        """Testing `ChoiceTextMultDynField`."""
        # Parameters by default:
        f = ChoiceTextMultDynField()
        self.assertEqual(f.html_attrs.id, "")
        self.assertEqual(f.html_attrs.label, "")
        self.assertEqual(f.html_attrs.name, "")
        self.assertEqual(f.html_attrs.field_type, "ChoiceTextMultDynField")
        self.assertFalse(f.html_attrs.disabled)
        self.assertFalse(f.html_attrs.hide)
        self.assertFalse(f.html_attrs.ignored)
        self.assertEqual(len(f.html_attrs.warning), 0)
        self.assertEqual(f.html_attrs.errors, [])
        self.assertEqual(f.html_attrs.group, "choice")
        self.assertIsNone(f.html_attrs.value)
        self.assertEqual(f.html_attrs.hint, "")
        self.assertFalse(f.html_attrs.required)
        self.assertFalse(f.html_attrs.readonly)
        self.assertFalse(f.html_attrs.unique)
        self.assertTrue(f.html_attrs.multiple)


if __name__ == "__main__":
    unittest.main()

"""Testing selective text fields."""

import unittest
from ramifice.fields import (
    ChoiceTextField, ChoiceTextMultField,
    ChoiceTextDynField, ChoiceTextMultDynField)


class TestChoiceTextFields(unittest.TestCase):
    """Testing selective text fields."""

    def test_choice_text_field(self):
        """Testing `ChoiceTextField`."""
        # Parameters by default:
        f = ChoiceTextField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceTextField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'choice')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertFalse(f.multiple)
        # Additional check:
        with self.assertRaises(AssertionError):
            f = ChoiceTextField(choices='not list')
        with self.assertRaises(AssertionError):
            f = ChoiceTextField(default=2)
        with self.assertRaises(AssertionError):
            f = ChoiceTextField(default="")
        with self.assertRaises(AssertionError):
            f = ChoiceTextField(
                default='value 3',
                choices=[('value', 'Title'), ('value 2', 'Title 2')])
        # Methods:
        self.assertTrue(f.has_value())
        f = ChoiceTextField(
            default='value 2',
            choices=[('value', 'Title'), ('value 2', 'Title 2')])
        self.assertTrue(f.has_value())
        f = ChoiceTextField(
            choices=[('value', 'Title'), ('value 2', 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = 'value 2'
        self.assertTrue(f.has_value())
        f.value = 'value 3'
        self.assertFalse(f.has_value())

    def test_choice_text_mult_field(self):
        """Testing `ChoiceTextMultField`."""
        # Parameters by default:
        f = ChoiceTextMultField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceTextMultField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'choice')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertTrue(f.multiple)
        # Additional check:
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(choices='not list')
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(default='not list')
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(default=[])
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(
                default=['value 3'],
                choices=[('value', 'Title'), ('value 2', 'Title 2')])
        with self.assertRaises(AssertionError):
            f = ChoiceTextMultField(
                default=['value 2', 'value 3'],
                choices=[('value', 'Title'), ('value 2', 'Title 2')])
        # Methods:
        self.assertTrue(f.has_value())
        f = ChoiceTextMultField(
            default=['value 2'],
            choices=[('value', 'Title'), ('value 2', 'Title 2')])
        self.assertTrue(f.has_value())
        f = ChoiceTextMultField(
            choices=[('value', 'Title'), ('value 2', 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = ['value 2']
        self.assertTrue(f.has_value())
        f.value = ['value 3']
        self.assertFalse(f.has_value())
        f.value = ['value 2', 'value 3']
        self.assertFalse(f.has_value())

    def test_choice_text_dyn_field(self):
        """Testing `ChoiceTextDynField`."""
        # Parameters by default:
        f = ChoiceTextDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceTextDynField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'choice')
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertFalse(f.multiple)

    def test_choice_text_mult_dyn_field(self):
        """Testing `ChoiceTextMultDynField`."""
        # Parameters by default:
        f = ChoiceTextMultDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceTextMultDynField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'choice')
        self.assertIsNone(f.value)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertTrue(f.multiple)


if __name__ == '__main__':
    unittest.main()

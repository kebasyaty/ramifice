"""Testing a parameters with default values for selective float fields."""

import unittest
from ramifice.fields import (
    ChoiceFloatField, ChoiceFloatMultField,
    ChoiceFloatDynField, ChoiceFloatMultDynField)


class TestChoiceFloategerFields(unittest.TestCase):
    """Testing parameters with default values."""

    def test_choice_float_field(self):
        """Testing a parameters by default for ChoiceFloatField."""
        f = ChoiceFloatField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceFloatField')
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
        #
        self.assertTrue(f.has_value())
        f = ChoiceFloatField(
            default=2.0,
            choices=[(1.0, 'Title'), (2.0, 'Title 2')])
        self.assertTrue(f.has_value())
        f = ChoiceFloatField(
            default=3.0,
            choices=[(1.0, 'Title'), (2.0, 'Title 2')])
        self.assertFalse(f.has_value())
        f = ChoiceFloatField(
            choices=[(1.0, 'Title'), (2.0, 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = 2.0
        self.assertTrue(f.has_value())
        f.value = 3.0
        self.assertFalse(f.has_value())

    def test_choice_float_mult_field(self):
        """Testing a parameters by default for ChoiceFloatMultField."""
        f = ChoiceFloatMultField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceFloatMultField')
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
        #
        self.assertTrue(f.has_value())
        f = ChoiceFloatMultField(
            default=[2.0],
            choices=[(1.0, 'Title'), (2.0, 'Title 2')])
        self.assertTrue(f.has_value())
        f = ChoiceFloatMultField(
            default=[3.0],
            choices=[(1.0, 'Title'), (2.0, 'Title 2')])
        self.assertFalse(f.has_value())
        f = ChoiceFloatMultField(
            choices=[(1.0, 'Title'), (2.0, 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = [2.0]
        self.assertTrue(f.has_value())
        f.value = [3.0]
        self.assertFalse(f.has_value())
        f.value = [2.0, 3.0]
        self.assertFalse(f.has_value())

    def test_choice_float_dyn_field(self):
        """Testing a parameters by default for ChoiceFloatDynField."""
        f = ChoiceFloatDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceFloatDynField')
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
        #
        self.assertTrue(f.has_value())
        f = ChoiceFloatDynField(
            choices=[(1.0, 'Title'), (2.0, 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = 2.0
        self.assertTrue(f.has_value())
        f.value = 3.0
        self.assertFalse(f.has_value())

    def test_choice_float_mult_dyn_field(self):
        """Testing a parameters by default for ChoiceFloatMultDynField."""
        f = ChoiceFloatMultDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceFloatMultDynField')
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
        #
        self.assertTrue(f.has_value())
        f = ChoiceFloatMultDynField(
            choices=[(1.0, 'Title'), (2.0, 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = [2.0]
        self.assertTrue(f.has_value())
        f.value = [3.0]
        self.assertFalse(f.has_value())
        f.value = [2.0, 3.0]
        self.assertFalse(f.has_value())


if __name__ == '__main__':
    unittest.main()

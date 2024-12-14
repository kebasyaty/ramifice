"""Testing a parameters with default values for selective integer fields."""

import unittest
from ramifice.fields import (
    ChoiceIntField, ChoiceIntMultField, ChoiceIntDynField, ChoiceIntMultDynField)


class TestChoiceIntegerFields(unittest.TestCase):
    """Testing parameters with default values."""

    def test_choice_int_field(self):
        """Testing a parameters by default for ChoiceIntField."""
        f = ChoiceIntField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceIntField')
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
        f = ChoiceIntField(
            default=2,
            choices=[(1, 'Title'), (2, 'Title 2')])
        self.assertTrue(f.has_value())
        f = ChoiceIntField(
            default=3,
            choices=[(1, 'Title'), (2, 'Title 2')])
        self.assertFalse(f.has_value())
        f = ChoiceIntField(
            choices=[(1, 'Title'), (2, 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = 2
        self.assertTrue(f.has_value())
        f.value = 3
        self.assertFalse(f.has_value())

    def test_choice_int_mult_field(self):
        """Testing a parameters by default for ChoiceIntMultField."""
        f = ChoiceIntMultField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceIntMultField')
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
        f = ChoiceIntMultField(
            default=[2],
            choices=[(1, 'Title'), (2, 'Title 2')])
        self.assertTrue(f.has_value())
        f = ChoiceIntMultField(
            default=[3],
            choices=[(1, 'Title'), (2, 'Title 2')])
        self.assertFalse(f.has_value())
        f = ChoiceIntMultField(
            choices=[(1, 'Title'), (2, 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = [2]
        self.assertTrue(f.has_value())
        f.value = [3]
        self.assertFalse(f.has_value())
        f.value = [2, 3]
        self.assertFalse(f.has_value())

    def test_choice_int_dyn_field(self):
        """Testing a parameters by default for ChoiceIntDynField."""
        f = ChoiceIntDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceIntDynField')
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
        f = ChoiceIntDynField(
            choices=[(1, 'Title'), (2, 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = 2
        self.assertTrue(f.has_value())
        f.value = 3
        self.assertFalse(f.has_value())

    def test_choice_int_mult_dyn_field(self):
        """Testing a parameters by default for ChoiceIntMultDynField."""
        f = ChoiceIntMultDynField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'ChoiceIntMultDynField')
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
        f = ChoiceIntMultDynField(
            choices=[(1, 'Title'), (2, 'Title 2')])
        self.assertTrue(f.has_value())
        f.value = [2]
        self.assertTrue(f.has_value())
        f.value = [3]
        self.assertFalse(f.has_value())
        f.value = [2, 3]
        self.assertFalse(f.has_value())


if __name__ == '__main__':
    unittest.main()

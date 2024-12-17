"""Testing number fields."""

import unittest
from ramifice.fields import (IntegerField, FloatField)


class TestNumberFields(unittest.TestCase):
    """Testing number fields."""

    def test_integer_field(self):
        """Testing `IntegerField`."""
        # Parameters by default:
        f = IntegerField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'IntegerField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'integer')
        self.assertEqual(f.input_type, 'number')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertIsNone(f.max_number)
        self.assertIsNone(f.min_number)
        self.assertEqual(f.step, int(1))
        # Additional check:
        with self.assertRaises(AssertionError):
            IntegerField(input_type='numbe')
        with self.assertRaises(AssertionError):
            IntegerField(input_type='rang')

    def test_float_field(self):
        """Testing `FloatField`."""
        # Parameters by default:
        f = FloatField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'FloatField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'float')
        self.assertEqual(f.input_type, 'number')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertFalse(f.readonly)
        self.assertFalse(f.unique)
        self.assertIsNone(f.max_number)
        self.assertIsNone(f.min_number)
        self.assertEqual(f.step, float(1))


if __name__ == '__main__':
    unittest.main()

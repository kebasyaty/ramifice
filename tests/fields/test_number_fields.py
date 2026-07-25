"""Testing number fields."""

from __future__ import annotations

import unittest

from ramifice.fields import FloatField, IntegerField


class TestNumberFields(unittest.TestCase):
    """Testing number fields."""

    def test_integer_field(self):
        """Testing `IntegerField`."""
        # Parameters by default:
        f = IntegerField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "IntegerField")
        self.assertFalse(f.field_core.disabled)
        self.assertFalse(f.field_core.hide)
        self.assertFalse(f.field_core.ignored)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "number")
        self.assertEqual(f.field_core.input_type, "number")
        self.assertIsNone(f.field_core.value)
        self.assertIsNone(f.field_core.default)
        self.assertEqual(f.field_core.placeholder, "")
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.required)
        self.assertFalse(f.field_core.readonly)
        self.assertFalse(f.field_core.unique)
        self.assertIsNone(f.field_core.max_number)
        self.assertIsNone(f.field_core.min_number)
        self.assertEqual(f.field_core.step, 1)
        # Exception checking:
        with self.assertRaises(AssertionError):
            IntegerField(input_type="")
        with self.assertRaises(AssertionError):
            IntegerField(input_type="numbe")
        with self.assertRaises(AssertionError):
            IntegerField(input_type="rang")
        IntegerField(input_type="number")
        IntegerField(input_type="range")
        with self.assertRaises(AssertionError):
            IntegerField(default="")
        with self.assertRaises(AssertionError):
            IntegerField(default=float(12))
        with self.assertRaises(AssertionError):
            IntegerField(default=12.0)
        with self.assertRaises(AssertionError):
            IntegerField(max_number=12.0)
        with self.assertRaises(AssertionError):
            IntegerField(min_number=12.0)
        with self.assertRaises(AssertionError):
            IntegerField(step=2.0)
        with self.assertRaises(AssertionError):
            IntegerField(max_number=12, min_number=12)
        with self.assertRaises(AssertionError):
            IntegerField(max_number=12, min_number=13)
        with self.assertRaises(AssertionError):
            IntegerField(default=11, max_number=13, min_number=12)
        with self.assertRaises(AssertionError):
            IntegerField(default=14, max_number=13, min_number=12)
        IntegerField(default=12)
        IntegerField(max_number=12)
        IntegerField(min_number=12)
        IntegerField(step=2)
        IntegerField(default=12, max_number=13, min_number=12)
        IntegerField(default=13, max_number=13, min_number=12)

    def test_float_field(self):
        """Testing `FloatField`."""
        # Parameters by default:
        f = FloatField()
        self.assertEqual(f.field_core.id, "")
        self.assertEqual(f.field_core.label, "")
        self.assertEqual(f.field_core.name, "")
        self.assertEqual(f.field_core.field_type, "FloatField")
        self.assertFalse(f.field_core.disabled)
        self.assertFalse(f.field_core.hide)
        self.assertFalse(f.field_core.ignored)
        self.assertEqual(len(f.field_core.warning), 0)
        self.assertEqual(f.field_core.errors, [])
        self.assertEqual(f.field_core.group, "number")
        self.assertEqual(f.field_core.input_type, "number")
        self.assertIsNone(f.field_core.value)
        self.assertIsNone(f.field_core.default)
        self.assertEqual(f.field_core.placeholder, "")
        self.assertEqual(f.field_core.hint, "")
        self.assertFalse(f.field_core.required)
        self.assertFalse(f.field_core.readonly)
        self.assertFalse(f.field_core.unique)
        self.assertIsNone(f.field_core.max_number)
        self.assertIsNone(f.field_core.min_number)
        self.assertEqual(f.field_core.step, float(1))
        # Exception checking:
        with self.assertRaises(AssertionError):
            FloatField(input_type="")
        with self.assertRaises(AssertionError):
            FloatField(input_type="numbe")
        with self.assertRaises(AssertionError):
            FloatField(input_type="rang")
        FloatField(input_type="number")
        FloatField(input_type="range")
        with self.assertRaises(AssertionError):
            FloatField(default="")
        with self.assertRaises(AssertionError):
            FloatField(default=12)
        with self.assertRaises(AssertionError):
            FloatField(default=12)
        with self.assertRaises(AssertionError):
            FloatField(max_number=12)
        with self.assertRaises(AssertionError):
            FloatField(min_number=12)
        with self.assertRaises(AssertionError):
            FloatField(step=2)
        with self.assertRaises(AssertionError):
            FloatField(max_number=12.0, min_number=12.0)
        with self.assertRaises(AssertionError):
            FloatField(max_number=12.0, min_number=13.0)
        with self.assertRaises(AssertionError):
            FloatField(default=14.0, max_number=13.0, min_number=12.0)
        with self.assertRaises(AssertionError):
            FloatField(default=11.0, max_number=13.0, min_number=12.0)
        FloatField(default=12.0)
        FloatField(max_number=12.0)
        FloatField(min_number=12.0)
        FloatField(step=2.0)
        FloatField(max_number=13.0, min_number=12.0)
        FloatField(default=12.0, max_number=13.0, min_number=12.0)
        FloatField(default=13.0, max_number=13.0, min_number=12.0)


if __name__ == "__main__":
    unittest.main()

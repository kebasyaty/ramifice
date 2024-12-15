"""Testing a parameters with default values for file fields."""

import unittest
from ramifice.fields import (FileField)


class TestFileFields(unittest.TestCase):
    """Testing parameters with default values."""

    def test_file_field(self):
        """Testing a parameters by default for FileField."""
        f = FileField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, 'FileField')
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, 'file')
        self.assertEqual(f.input_type, 'file')
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertFalse(f.required)
        self.assertEqual(f.target_dir, "")
        self.assertEqual(f.accept, "")
        self.assertEqual(f.media_root, 'public/media/uploads')
        self.assertEqual(f.media_url, '/media/uploads')


if __name__ == '__main__':
    unittest.main()

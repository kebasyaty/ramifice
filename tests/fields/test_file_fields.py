"""Testing file fields."""

import unittest

from ramifice.fields import FileField, ImageField


class TestFileFields(unittest.TestCase):
    """Testing file fields."""

    def test_file_field(self):
        """Testing `FileField`."""
        # Parameters by default:
        f = FileField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "FileField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "file")
        self.assertEqual(f.input_type, "file")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertEqual(f.target_dir, "files")
        self.assertEqual(f.accept, "")
        self.assertEqual(f.media_root, "public/media/uploads")
        self.assertEqual(f.media_url, "/media/uploads")
        # Methods:
        # self.assertIsNone(f.from_base64("SGVsbG8gV29ybGQhCg==", "file_name.txt"))
        # self.assertEqual(f.value.name, "file_name.txt")
        # self.assertEqual(f.value.size, 13)
        # self.assertTrue(f.value.is_new_file)
        # self.assertEqual(f.value.extension, ".txt")
        # self.assertFalse(f.value.delete)
        # self.assertFalse(f.value.save_as_is)

    def test_image_field(self):
        """Testing `ImageField`."""
        # Parameters by default:
        f = ImageField()
        self.assertEqual(f.id, "")
        self.assertEqual(f.label, "")
        self.assertEqual(f.name, "")
        self.assertEqual(f.field_type, "ImageField")
        self.assertFalse(f.disabled)
        self.assertFalse(f.hide)
        self.assertFalse(f.ignored)
        self.assertIsNone(f.warning)
        self.assertIsNone(f.errors)
        self.assertEqual(f.group, "image")
        self.assertEqual(f.input_type, "file")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertFalse(f.required)
        self.assertEqual(f.target_dir, "images")
        self.assertEqual(f.accept, "")
        self.assertEqual(f.media_root, "public/media/uploads")
        self.assertEqual(f.media_url, "/media/uploads")


if __name__ == "__main__":
    unittest.main()

"""Testing file fields."""

from __future__ import annotations

import unittest

from ramifice.fields import FileField, ImageField
from ramifice.utils.errors import FileHasNoExtensionError


class TestFileFields(unittest.IsolatedAsyncioTestCase):
    """Testing file fields."""

    def setUp(self):
        """Set data for testing."""
        self.file_base64_str = "SGVsbG8gV29ybGQhCg=="
        self.img_base64_str = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAANSURBVBhXY9BJbvgPAAPdAg9WzUCeAAAAAElFTkSuQmCC"  # noqa: E501
        return super().setUp()

    async def test_file_field(self):
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
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "file")
        self.assertEqual(f.input_type, "file")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertEqual(f.hint, "")
        self.assertFalse(f.required)
        self.assertEqual(f.target_dir, "files")
        self.assertEqual(f.accept, "")
        # Exception checking:
        with self.assertRaises(AssertionError):
            FileField(default=12)
        with self.assertRaises(AssertionError):
            FileField(default="")
        #
        with self.assertRaises(FileHasNoExtensionError):
            await f.from_base64(self.file_base64_str, "file_name")
        with self.assertRaises(FileHasNoExtensionError):
            await f.from_path("public/media/default/no_doc")
        # from_base64
        self.assertIsNone(await f.from_base64(self.file_base64_str, "file_name.txt"))
        self.assertEqual(f.value["name"], "file_name.txt")
        self.assertEqual(f.value["size"], 13)
        self.assertEqual(f.value["human_size"], "13 bytes")
        self.assertTrue(f.value["is_new_file"])
        self.assertEqual(f.value["extension"], ".txt")
        self.assertFalse(f.value["is_delete"])
        self.assertFalse(f.value["save_as_is"])
        # from_path
        self.assertIsNone(await f.from_path("public/media/default/no_doc.odt"))
        self.assertEqual(f.value["name"], "no_doc.odt")
        self.assertEqual(f.value["size"], 9843)
        self.assertEqual(f.value["human_size"], "9.612 KB")
        self.assertTrue(f.value["is_new_file"])
        self.assertEqual(f.value["extension"], ".odt")
        self.assertFalse(f.value["is_delete"])
        self.assertFalse(f.value["save_as_is"])

    async def test_image_field(self):
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
        self.assertEqual(f.errors, [])
        self.assertEqual(f.group, "img")
        self.assertEqual(f.input_type, "file")
        self.assertIsNone(f.value)
        self.assertIsNone(f.default)
        self.assertEqual(f.placeholder, "")
        self.assertEqual(f.hint, "")
        self.assertFalse(f.required)
        self.assertEqual(f.target_dir, "images")
        self.assertEqual(f.accept, "image/png,image/jpeg,image/webp")
        # Exception checking:
        with self.assertRaises(AssertionError):
            ImageField(default=12)
        with self.assertRaises(AssertionError):
            ImageField(default="")
        with self.assertRaises(AssertionError):
            ImageField(thumbnails=[])
        with self.assertRaises(AssertionError):
            ImageField(thumbnails={})
        with self.assertRaises(AssertionError):
            ImageField(thumbnails={"bad_key": 120})
        with self.assertRaises(AssertionError):
            ImageField(thumbnails={"lg": 1200, "md": 600, "sm": 300, "xs": 300})
        with self.assertRaises(AssertionError):
            ImageField(thumbnails={"lg": 1200, "md": 600, "sm": 300, "xs": 301})
        #
        with self.assertRaises(FileHasNoExtensionError):
            await f.from_base64(self.img_base64_str, "file_name")
        with self.assertRaises(FileHasNoExtensionError):
            await f.from_path("public/media/default/no_doc")
        # from_base64
        self.assertIsNone(
            await f.from_base64(
                base64_str=self.img_base64_str,
                filename="image_name.png",
            ),
        )
        self.assertEqual(f.value["name"], "image_name.png")
        self.assertEqual(f.value["size"], 120)
        self.assertEqual(f.value["human_size"], "120 bytes")
        self.assertTrue(f.value["is_new_img"])
        self.assertEqual(f.value["extension"], ".png")
        self.assertEqual(f.value["ext_upper"], "PNG")
        self.assertFalse(f.value["is_delete"])
        self.assertFalse(f.value["save_as_is"])
        # from_path
        self.assertIsNone(
            await f.from_path(
                src_path="public/media/default/no-photo.png",
            ),
        )
        self.assertEqual(f.value["name"], "no-photo.png")
        self.assertEqual(f.value["size"], 41554)
        self.assertEqual(f.value["human_size"], "40.58 KB")
        self.assertTrue(f.value["is_new_img"])
        self.assertEqual(f.value["extension"], ".png")
        self.assertEqual(f.value["ext_upper"], "PNG")
        self.assertFalse(f.value["is_delete"])
        self.assertFalse(f.value["save_as_is"])


if __name__ == "__main__":
    unittest.main()

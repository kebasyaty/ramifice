"""Testing file fields."""

from __future__ import annotations

import unittest

from ramifice.errors import FileHasNoExtensionError
from ramifice.fields import FileField, ImageField


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
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "FileField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertIsNone(f.html_attrs["warning"])
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "file")
        self.assertEqual(f.html_attrs["input_type"], "file")
        self.assertIsNone(f.html_attrs["value"])
        self.assertIsNone(f.html_attrs["default"])
        self.assertEqual(f.html_attrs["placeholder"], "")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertEqual(f.html_attrs["target_dir"], "files")
        self.assertEqual(f.html_attrs["accept"], "")
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
        self.assertEqual(f.html_attrs["value"]["name"], "file_name.txt")
        self.assertEqual(f.html_attrs["value"]["size"], 13)
        self.assertEqual(f.html_attrs["value"]["human_size"], "13 bytes")
        self.assertTrue(f.html_attrs["value"]["is_new_file"])
        self.assertEqual(f.html_attrs["value"]["extension"], ".txt")
        self.assertFalse(f.html_attrs["value"]["is_delete"])
        self.assertFalse(f.html_attrs["value"]["save_as_is"])
        # from_path
        self.assertIsNone(await f.from_path("public/media/default/no_doc.odt"))
        self.assertEqual(f.html_attrs["value"]["name"], "no_doc.odt")
        self.assertEqual(f.html_attrs["value"]["size"], 9843)
        self.assertEqual(f.html_attrs["value"]["human_size"], "9.612 KB")
        self.assertTrue(f.html_attrs["value"]["is_new_file"])
        self.assertEqual(f.html_attrs["value"]["extension"], ".odt")
        self.assertFalse(f.html_attrs["value"]["is_delete"])
        self.assertFalse(f.html_attrs["value"]["save_as_is"])

    async def test_image_field(self):
        """Testing `ImageField`."""
        # Parameters by default:
        f = ImageField()
        self.assertEqual(f.html_attrs["id"], "")
        self.assertEqual(f.html_attrs["label"], "")
        self.assertEqual(f.html_attrs["name"], "")
        self.assertEqual(f.html_attrs["field_type"], "ImageField")
        self.assertFalse(f.html_attrs["disabled"])
        self.assertFalse(f.html_attrs["hide"])
        self.assertFalse(f.html_attrs["ignored"])
        self.assertIsNone(f.html_attrs["warning"])
        self.assertEqual(f.html_attrs["errors"], [])
        self.assertEqual(f.html_attrs["group"], "img")
        self.assertEqual(f.html_attrs["input_type"], "file")
        self.assertIsNone(f.html_attrs["value"])
        self.assertIsNone(f.html_attrs["default"])
        self.assertEqual(f.html_attrs["placeholder"], "")
        self.assertEqual(f.html_attrs["hint"], "")
        self.assertFalse(f.html_attrs["required"])
        self.assertEqual(f.html_attrs["target_dir"], "images")
        self.assertEqual(f.html_attrs["accept"], "image/png,image/jpeg,image/webp")
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
        self.assertEqual(f.html_attrs["value"]["name"], "image_name.png")
        self.assertEqual(f.html_attrs["value"]["size"], 120)
        self.assertEqual(f.html_attrs["value"]["human_size"], "120 bytes")
        self.assertTrue(f.html_attrs["value"]["is_new_img"])
        self.assertEqual(f.html_attrs["value"]["extension"], ".png")
        self.assertEqual(f.html_attrs["value"]["ext_upper"], "PNG")
        self.assertFalse(f.html_attrs["value"]["is_delete"])
        self.assertFalse(f.html_attrs["value"]["save_as_is"])
        # from_path
        self.assertIsNone(
            await f.from_path(
                src_path="public/media/default/no-photo.png",
            ),
        )
        self.assertEqual(f.html_attrs["value"]["name"], "no-photo.png")
        self.assertEqual(f.html_attrs["value"]["size"], 41554)
        self.assertEqual(f.html_attrs["value"]["human_size"], "40.58 KB")
        self.assertTrue(f.html_attrs["value"]["is_new_img"])
        self.assertEqual(f.html_attrs["value"]["extension"], ".png")
        self.assertEqual(f.html_attrs["value"]["ext_upper"], "PNG")
        self.assertFalse(f.html_attrs["value"]["is_delete"])
        self.assertFalse(f.html_attrs["value"]["save_as_is"])


if __name__ == "__main__":
    unittest.main()

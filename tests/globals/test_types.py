"""Testing the global module `types`."""

import unittest

from ramifice.types import FileData, ImageData, OutputData, Unit


class TestGlobalTypes(unittest.TestCase):
    """Testing the global module `types`."""

    def test_output_data(self):
        """Testing a class `OutputData`."""
        d = OutputData(data={"field_name": "value"}, valid=True, update=False)
        self.assertEqual(d.data, {"field_name": "value"})
        self.assertTrue(d.valid)
        self.assertFalse(d.update)
        d.valid = False
        self.assertFalse(d.valid)

    def test_unit(self):
        """Testing a class `Unit`."""
        u = Unit(field="field_name", title="Title", value="value")
        self.assertEqual(u.field, "field_name")
        self.assertEqual(u.title, "Title")
        self.assertEqual(u.value, "value")
        self.assertFalse(u.delete)
        u = Unit(field="field_name", title="Title", value="value", delete=True)
        self.assertEqual(u.field, "field_name")
        self.assertEqual(u.title, "Title")
        self.assertEqual(u.value, "value")
        self.assertTrue(u.delete)

    def test_file_data(self):
        """Testing a class `FileData`."""
        d = FileData()
        self.assertEqual(d.path, "")
        self.assertEqual(d.url, "")
        self.assertEqual(d.name, "")
        self.assertEqual(d.size, 0)
        self.assertFalse(d.is_new_file)
        self.assertFalse(d.delete)
        self.assertEqual(d.extension, "")
        self.assertFalse(d.save_as_is)
        d.path = "path/file.txt"
        d.url = "/path/file.txt"
        d.name = "file.txt"
        d.size = 512
        d.is_new_file = True
        d.delete = True
        d.extension = ".txt"
        d.save_as_is = True
        self.assertEqual(d.path, "path/file.txt")
        self.assertEqual(d.url, "/path/file.txt")
        self.assertEqual(d.name, "file.txt")
        self.assertEqual(d.size, 512)
        self.assertTrue(d.is_new_file)
        self.assertTrue(d.delete)
        self.assertEqual(d.extension, ".txt")
        self.assertTrue(d.save_as_is)

    def test_image_data(self):
        """Testing a class `ImageData`."""
        d = ImageData()
        self.assertEqual(d.path, "")
        self.assertEqual(d.path_xs, "")
        self.assertEqual(d.path_sm, "")
        self.assertEqual(d.path_md, "")
        self.assertEqual(d.path_lg, "")
        self.assertEqual(d.url, "")
        self.assertEqual(d.url_xs, "")
        self.assertEqual(d.url_sm, "")
        self.assertEqual(d.url_md, "")
        self.assertEqual(d.url_lg, "")
        self.assertEqual(d.name, "")
        self.assertEqual(d.width, 0)
        self.assertEqual(d.height, 0)
        self.assertEqual(d.size, 0)
        self.assertFalse(d.is_new_img)
        self.assertFalse(d.delete)
        self.assertEqual(d.extension, "")
        self.assertEqual(d.imgs_dir_path, "")
        self.assertEqual(d.imgs_dir_url, "")
        self.assertFalse(d.save_as_is)
        d.path = "path/img.png"
        d.path_xs = "path/xs.png"
        d.path_sm = "path/sm.png"
        d.path_md = "path/md.png"
        d.path_lg = "path/lg.png"
        d.url = "/path/img.png"
        d.url_xs = "/path/xs.png"
        d.url_sm = "/path/sm.png"
        d.url_md = "/path/md.png"
        d.url_lg = "/path/lg.png"
        d.name = "img.png"
        d.width = 512
        d.height = 512
        d.size = 512
        d.is_new_img = True
        d.delete = True
        d.extension = ".png"
        d.imgs_dir_path = "path/0123456789abcdef"
        d.imgs_dir_url = "/path/0123456789abcdef"
        d.save_as_is = True
        self.assertEqual(d.path, "path/img.png")
        self.assertEqual(d.path_xs, "path/xs.png")
        self.assertEqual(d.path_sm, "path/sm.png")
        self.assertEqual(d.path_md, "path/md.png")
        self.assertEqual(d.path_lg, "path/lg.png")
        self.assertEqual(d.url, "/path/img.png")
        self.assertEqual(d.url_xs, "/path/xs.png")
        self.assertEqual(d.url_sm, "/path/sm.png")
        self.assertEqual(d.url_md, "/path/md.png")
        self.assertEqual(d.url_lg, "/path/lg.png")
        self.assertEqual(d.name, "img.png")
        self.assertEqual(d.width, 512)
        self.assertEqual(d.height, 512)
        self.assertEqual(d.size, 512)
        self.assertTrue(d.is_new_img)
        self.assertTrue(d.delete)
        self.assertEqual(d.extension, ".png")
        self.assertEqual(d.imgs_dir_path, "path/0123456789abcdef")
        self.assertEqual(d.imgs_dir_url, "/path/0123456789abcdef")
        self.assertTrue(d.save_as_is)

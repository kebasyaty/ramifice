"""Testing the global module `types`."""

import unittest

from ramifice.types import FileData, ImageData, OutputData, Unit


class TestGlobalTypes(unittest.TestCase):
    """Testing the global module `types`."""

    def test_output_data(self):
        """Testing a class `OutputData`."""
        d = OutputData(data={'field_name': 'value'}, valid=True, update=False)
        self.assertEqual(d.data, {'field_name': 'value'})
        self.assertTrue(d.valid)
        self.assertFalse(d.update)
        d.valid = False
        self.assertFalse(d.valid)

    def test_unit(self):
        """Testing a class `Unit`."""
        u = Unit(field='field_name', title='Title', value='value')
        self.assertEqual(u.field, 'field_name')
        self.assertEqual(u.title, 'Title')
        self.assertEqual(u.value, 'value')
        self.assertFalse(u.delete)
        u = Unit(field='field_name', title='Title', value='value', delete=True)
        self.assertEqual(u.field, 'field_name')
        self.assertEqual(u.title, 'Title')
        self.assertEqual(u.value, 'value')
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
        d.path = 'path/file.txt'
        d.url = '/path/file.txt'
        d.name = 'file.txt'
        d.size = 512
        d.is_new_file = True
        d.delete = True
        d.extension = '.txt'
        d.save_as_is = True
        self.assertEqual(d.path, 'path/file.txt')
        self.assertEqual(d.url, '/path/file.txt')
        self.assertEqual(d.name, 'file.txt')
        self.assertEqual(d.size, 512)
        self.assertTrue(d.is_new_file)
        self.assertTrue(d.delete)
        self.assertEqual(d.extension, '.txt')
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
        self.assertEqual(d.size, 0)
        self.assertFalse(d.is_new_img)
        self.assertFalse(d.delete)
        self.assertEqual(d.extension, "")
        self.assertFalse(d.save_as_is)
        d.path = 'path/img.png'
        d.url = '/path/img.png'
        d.name = 'img.png'
        d.size = 512
        d.is_new_img = True
        d.delete = True
        d.extension = '.png'
        d.save_as_is = True
        self.assertEqual(d.path, 'path/img.png')
        self.assertEqual(d.url, '/path/img.png')
        self.assertEqual(d.name, 'img.png')
        self.assertEqual(d.size, 512)
        self.assertTrue(d.is_new_img)
        self.assertTrue(d.delete)
        self.assertEqual(d.extension, '.png')
        self.assertTrue(d.save_as_is)

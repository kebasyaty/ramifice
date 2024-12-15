"""Testing variables in global store."""

import unittest
from ramifice.globals.store import (
    MONGO_CLIENT)


class TestGlobalStore(unittest.TestCase):
    """Testing variables in global store."""

    def test_bool_field(self):
        """Testing a values by default."""
        self.assertIsNone(MONGO_CLIENT)


if __name__ == '__main__':
    unittest.main()

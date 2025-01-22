"""Testing the module `ramifice.store`."""

import unittest

from pymongo import AsyncMongoClient


class TestAsyncMongoClient(unittest.TestCase):
    """Testing the `AsyncMongoClient`."""

    def test_connection_mongo_client(self):
        """Connection with AsyncMongoClient."""
        client = AsyncMongoClient("localhost", 27017)

"""Testing the `AsyncMongoClient`."""

import unittest

from pymongo import AsyncMongoClient


class TestAsyncMongoClient(unittest.IsolatedAsyncioTestCase):
    """Testing the `AsyncMongoClient`."""

    async def test_connection_mongo_client(self):
        """Connection with AsyncMongoClient."""
        # Making a Connection with MongoClient:
        client = AsyncMongoClient(host="localhost", port=27017)
        # Getting a Database:
        db = client["test-database"]
        self.assertEqual(db.name, "test-database")
        # Getting a Collection:
        collection = db["test-collection"]
        # Inserting a Document:
        await collection.insert_one({"x": 1})
        self.assertEqual(await db.list_collection_names(), ["test-collection"])
        #
        await client.close()

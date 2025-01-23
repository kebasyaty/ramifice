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
        await collection.insert_one({"x": 1, "y": [1, 2, 3]})
        self.assertEqual(await db.list_collection_names(), ["test-collection"])
        doc = await collection.find_one({"x": 1})
        self.assertTrue(isinstance(doc.get("x"), int))
        self.assertTrue(isinstance(doc.get("y"), list))
        self.assertTrue(isinstance(doc, dict))
        doc_count = await collection.count_documents({})
        self.assertEqual(doc_count, 1)
        await collection.delete_one({"x": 1})
        doc_count = await collection.count_documents({})
        self.assertEqual(doc_count, 0)
        _ = await client.drop_database(db.name)
        #
        await client.close()

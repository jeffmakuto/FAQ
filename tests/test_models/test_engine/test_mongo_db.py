import unittest
from pymongo import MongoClient
from back_end.models.engine.mongo_db import MongoDBHandler

class TestMongoDBHandler(unittest.TestCase):
    def setUp(self):
        """Set up a test MongoDB connection for the tests."""
        self.test_db_name = 'test_database'
        self.test_collection_name = 'test_collection'
        self.mongo_client = MongoClient('localhost', 27017)
        self.mongo_db = self.mongo_client[self.test_db_name]
        self.mongo_collection = self.mongo_db[self.test_collection_name]

    def tearDown(self):
        """Clean up the test database after the tests."""
        self.mongo_client.drop_database(self.test_db_name)

    def test_successful_connection(self):
        """Test successful MongoDB connection."""

        handler = MongoDBHandler(self.test_db_name, self.test_collection_name)

        self.assertIsNotNone(handler.collection)

    def test_failed_connection(self):
        """Test failed MongoDB connection."""

        handler = MongoDBHandler('nonexistent_db', self.test_collection_name)

        self.assertIsNone(handler.collection)

    def test_add_to_db_without_connection(self):
        """Test adding to the database without a valid connection."""

        handler = MongoDBHandler(self.test_db_name, self.test_collection_name)
        handler.collection = None

        handler.add_to_db("Question", "Answer")

        # Check if there are no documents in the collection
        document = self.mongo_collection.find_one()
        self.assertIsNone(document)

    def test_get_from_db_without_connection(self):
        """Test retrieving from the database without a valid connection."""

        handler = MongoDBHandler(self.test_db_name, self.test_collection_name)
        handler.collection = None

        retrieved_answer = handler.get_from_db("Question")


        self.assertIsNone(retrieved_answer)

    def test_add_to_db_and_get_from_db_multiple_documents(self):
        """Test adding and retrieving multiple documents from the database."""

        handler = MongoDBHandler(self.test_db_name, self.test_collection_name)


        handler.add_to_db("Question1", "Answer1")
        handler.add_to_db("Question2", "Answer2")


        retrieved_answer_1 = handler.get_from_db("Question1")
        retrieved_answer_2 = handler.get_from_db("Question2")

        self.assertEqual(retrieved_answer_1, "Answer1")
        self.assertEqual(retrieved_answer_2, "Answer2")

    def test_add_to_db_error_handling(self):
        """Test error handling during document insertion."""

        handler = MongoDBHandler(self.test_db_name, self.test_collection_name)
        handler.collection.insert_one = None  # Simulate an error during insertion

        with self.assertRaises(Exception):
            handler.add_to_db("Question", "Answer")

    def test_get_from_db_error_handling(self):
        """Test error handling during document retrieval."""

        handler = MongoDBHandler(self.test_db_name, self.test_collection_name)
        handler.collection.find_one = None  # Simulate an error during retrieval

        with self.assertRaises(Exception):
            handler.get_from_db("Question")

if __name__ == '__main__':
    unittest.main()

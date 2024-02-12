#!/usr/bin/env python3
import unittest
from unittest.mock import MagicMock, patch
from mongo_db import MongoDBHandler

class TestMongoDBHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a test MongoDB database and collection for the class
        cls.test_db_name = 'test_db'
        cls.test_collection_name = 'test_collection'
        cls.mongo_handler = MongoDBHandler(db_name=cls.test_db_name, collection_name=cls.test_collection_name)

    def test_connection_successful(self):
        """
        Test that the MongoDBHandler initializes successfully and establishes a connection to the MongoDB collection.
        """
        self.assertIsNotNone(self.mongo_handler.collection)
        self.assertIsInstance(self.mongo_handler.collection, MagicMock)
        # Assuming that the MagicMock class is used for the MongoDB collection for testing purposes

    def test_add_to_db_successful(self):
        """
        Test the successful addition of a question and answer pair to the MongoDB collection.
        """
        question = 'Test question'
        answer = 'Test answer'

        with patch.object(self.mongo_handler.collection, 'insert_one', return_value=None) as mock_insert:
            self.mongo_handler.add_to_db(question, answer)
            mock_insert.assert_called_once_with({"question": question, "answer": answer})

    def test_add_to_db_connection_not_established(self):
        """
        Test that attempting to add a question and answer pair to the MongoDB collection fails when the connection
        to the database is not established.
        """
        mongo_handler = MongoDBHandler(db_name='invalid_db', collection_name='invalid_collection')
        with patch.object(mongo_handler.collection, 'insert_one') as mock_insert:
            mongo_handler.add_to_db('Invalid question', 'Invalid answer')
            mock_insert.assert_not_called()

    def test_get_from_db_successful(self):
        """
        Test the successful retrieval of an answer for a given question from the MongoDB collection.
        """
        question = 'Test question'
        answer = 'Test answer'
        mock_find_one = MagicMock(return_value={"question": question, "answer": answer})
        with patch.object(self.mongo_handler.collection, 'find_one', mock_find_one):
            result = self.mongo_handler.get_from_db(question)
            mock_find_one.assert_called_once_with({"question": question})
            self.assertEqual(result, answer)

    def test_get_from_db_connection_not_established(self):
        """
        Test that attempting to retrieve an answer from the MongoDB collection fails when the connection
        to the database is not established.
        """
        mongo_handler = MongoDBHandler(db_name='invalid_db', collection_name='invalid_collection')
        with patch.object(mongo_handler.collection, 'find_one') as mock_find_one:
            result = mongo_handler.get_from_db('Invalid question')
            mock_find_one.assert_not_called()
            self.assertIsNone(result)

    def test_get_from_db_question_not_found(self):
        """
        Test that attempting to retrieve an answer for a non-existent question from the MongoDB collection
        results in a None response.
        """
        with patch.object(self.mongo_handler.collection, 'find_one', return_value=None) as mock_find_one:
            result = self.mongo_handler.get_from_db('Non-existent question')
            mock_find_one.assert_called_once_with({"question": 'Non-existent question'})
            self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

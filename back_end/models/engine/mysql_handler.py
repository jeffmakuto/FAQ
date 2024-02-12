#!/usr/bin/env python3
""" Database engine with sqlalchemy for MySQL """
import logging
from pymongo import MongoClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MongoDBHandler:
    def __init__(self, db_name, collection_name, host='localhost', port=27017, username=None, password=None):
        """
        Initializes a new instance of MongoDBHandler.

        Connects to the MongoDB database using the provided configuration.

        Args:
            db_name (str): The name of the MongoDB database.
            collection_name (str): The name of the collection within the database.
            host (str): MongoDB server host (default is 'localhost').
            port (int): MongoDB server port (default is 27017).
            username (str): MongoDB username (default is None).
            password (str): MongoDB password (default is None).
        """
        try:
            connection_uri = f"mongodb://{username}:{password}@{host}:{port}/"
            self.collection = MongoClient(connection_uri)[db_name][collection_name]
            logger.info("Connected to MongoDB")
        except Exception as e:
            logger.error(f"Error connecting to MongoDB: {e}")
            self.collection = None  # Set to None to indicate a failed connection
            # You can choose to raise the exception if you want to stop the program
            # raise

    def add_to_db(self, question, answer):
        """
        Adds a new query to the 'queries' collection in the MongoDB database.

        Args:
            question (str): The question to be added.
            answer (str): The corresponding answer to be added.
        """
        if self.collection is None:
            logger.error("Cannot add to the database. MongoDB connection not established.")
            return

        document = {"question": question, "answer": answer}
        try:
            self.collection.insert_one(document)
            logger.info(f"Added query: '{question}'")
        except Exception as e:
            logger.error(f"Error adding query to MongoDB: {e}")
            # Consider raising the exception if you want to stop the program
            # raise

    def get_from_db(self, question):
        """
        Retrieves the answer for a given question from the 'queries' collection in the MongoDB database.

        Args:
            question (str): The question for which the answer is to be retrieved.

        Returns:
            str or None: The answer if found, or None if the question is not in the database.
        """
        if self.collection is None:
            logger.error("Cannot retrieve from the database. MongoDB connection not established.")
            return None

        document = self.collection.find_one({"question": question})
        if document:
            logger.info(f"Retrieved answer for query: '{question}'")
            return document["answer"]
        else:
            logger.warning(f"Query not found: '{question}'")
            return None


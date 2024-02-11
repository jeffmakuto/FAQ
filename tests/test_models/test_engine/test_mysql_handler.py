import unittest
from unittest.mock import patch, Mock
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from back_end.models.engine.mysql_handler import MySQLHandler
from back_end.models.engine.db_config import my_db_config
from sqlalchemy.ext.declarative import Base

class TestMySQLHandler(unittest.TestCase):
    """
    This module contains unit tests for the MySQLHandler class in your_module.
    It focuses on testing the functionality of adding and retrieving queries from the MySQL database.

    Test Cases:
    - test_add_to_db: Tests the addition of a new query to the database.
    - test_get_from_db_existing_question: Tests retrieving an answer for an existing question.
    - test_get_from_db_nonexistent_question: Tests retrieving an answer for a nonexistent question.
    - test_init_with_db_config: Tests the initialization of MySQLHandler with a provided db_config.
    - test_init_with_default_config: Tests the initialization of MySQLHandler with the default db_config.
    """

    def setUp(self):
        """
        Set up the testing environment by creating an in-memory SQLite database and initializing MySQLHandler.
        """
        engine = create_engine('sqlite:///:memory:')
        Session = sessionmaker(bind=engine)
        Base.metadata.create_all(bind=engine)
        self.mysql_handler = MySQLHandler(db_config=my_db_config)
        self.mysql_handler.Session = Session

    def tearDown(self):
        """
        Clean up the testing environment by closing any open sessions.
        """
        self.mysql_handler.Session.close()

    def test_add_to_db(self):
        """
        Test adding a new query to the database.
        """
        question = "What is the answer?"
        answer = "The answer is 42."
        self.mysql_handler.add_to_db(question, answer)

        # Check if the query is in the database
        result = self.mysql_handler.get_from_db(question)
        self.assertEqual(result, answer)

    def test_get_from_db_existing_question(self):
        """
        Test retrieving an answer for an existing question.
        """
        question = "Existing question"
        answer = "Existing answer"
        self.mysql_handler.add_to_db(question, answer)

        result = self.mysql_handler.get_from_db(question)
        self.assertEqual(result, answer)

    def test_get_from_db_nonexistent_question(self):
        """
        Test retrieving an answer for a nonexistent question.
        """
        question = "Nonexistent question"
        result = self.mysql_handler.get_from_db(question)
        self.assertIsNone(result)

    @patch('your_module.create_engine')
    @patch('your_module.Base.metadata.create_all')
    def test_init_with_db_config(self, mock_create_all, mock_create_engine):
        """
        Test initialization with a provided db_config.
        """
        db_config = Mock()
        self.mysql_handler = MySQLHandler(db_config=db_config)

        # Ensure create_engine is called with the correct arguments
        mock_create_engine.assert_called_once_with(
            f"mysql+pymysql://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}",
            echo=True,
        )

        # Ensure Base.metadata.create_all is called
        mock_create_all.assert_called_once()

    @patch('your_module.create_engine')
    @patch('your_module.Base.metadata.create_all')
    def test_init_with_default_config(self, mock_create_all, mock_create_engine):
        """
        Test initialization with the default db_config.
        """
        self.mysql_handler = MySQLHandler()

        # Ensure create_engine is called with the correct arguments
        mock_create_engine.assert_called_once_with(
            f"mysql+pymysql://{my_db_config.user}:{my_db_config.password}@{my_db_config.host}:{my_db_config.port}/{my_db_config.database}",
            echo=True,
        )

        # Ensure Base.metadata.create_all is called
        mock_create_all.assert_called_once()

if __name__ == '__main__':
    unittest.main()

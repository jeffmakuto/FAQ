#!/usr/bin/env python3
""" Database engine with sqlalchemy for MySQL """
import logging
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db_config import my_db_config

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a base class for declarative class definitions
Base = declarative_base()

class Query(Base):
    """
    SQLAlchemy model representing the 'queries' table.

    Attributes:
        id (int): Primary key, auto-incremented.
        question (str): Question text (non-nullable and unique).
        answer (str): Answer text (non-nullable).
    """
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String, nullable=False, unique=True)
    answer = Column(String, nullable=False)

class MySQLHandler:
    """
    Handles MySQL database operations using SQLAlchemy.

    Methods:
        __init__(db_config): Initializes the MySQLHandler with a connection to the database.
        add_to_db(question, answer): Adds a new query to the 'queries' table.
        get_from_db(question): Retrieves the answer for a given question from the database.

    Attributes:
        Session: A sessionmaker for creating database sessions.
    """
    def __init__(self, db_config=my_db_config):
        """
        Initializes a new instance of MySQLHandler.

        Connects to the MySQL database using the provided configuration.

        Args:
            db_config (DBConfig): An instance of the DBConfig class containing database connection details.
        """
        engine = create_engine(
            f"mysql+pymysql://{db_config.user}:{db_config.password}@{db_config.host}:{db_config.port}/{db_config.database}",
            echo=True,
        )
        # Create the 'queries' table if it does not exist
        Base.metadata.create_all(bind=engine)
        self.Session = sessionmaker(bind=engine)

    def add_to_db(self, question, answer):
        """
        Adds a new query to the 'queries' table in the database.

        Args:
            question (str): The question to be added.
            answer (str): The corresponding answer to be added.
        """
        with self.Session() as session:
            new_query = Query(question=question, answer=answer)
            session.add(new_query)
            session.commit()
            logger.info(f"Added query: '{question}'")

    def get_from_db(self, question):
        """
        Retrieves the answer for a given question from the 'queries' table in the database.

        Args:
            question (str): The question for which the answer is to be retrieved.

        Returns:
            str or None: The answer if found, or None if the question is not in the database.
        """
        with self.Session() as session:
            query = session.query(Query).get(question)
            if query:
                logger.info(f"Retrieved answer for query: '{question}'")
                return query.answer
            else:
                logger.warning(f"Query not found: '{question}'")
                return None

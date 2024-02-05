#!/usr/bin/env python3
""" Module that handles the bot's logic features """


class RuleBasedBot:
    """
    Takes input processes it and answers back. if it doesn't understand,
    it answers 'I don't have an answer for that, sorry'
    """
    def __init__(self):
        """ Initialize the database to store the data """
        self.db = {}

    def add_to_db(self, q, a):
        """ Adds the new query to the database """
        self.db[q] = a

    def respond(self, user_input):
        """
        Checks if an aswer is provided in the db and responds
        If the response isn't found it writes a custom message
        to inform the user response isn't available
        """
        if user_input in self.db:
            return self.db[user_input]
        else:
            self.add_to_db(user_input, "Hello admin, please reply to the query. Thank you")
            return "I don't have an answer for that, sorry."


class Admin:
    """
    Admin class responsible for managing unanswered queries and providing answers.

    Attributes:
    - bot (object): An instance of the RuleBasedBot class for communication.
    - unanswered_queries (dict): A dictionary to store unanswered queries and their corresponding answers.

    Methods:
    - has_unanswered_queries(): Check if there are any unanswered queries.
    - get_unanswered_queries(): Get a list of unanswered queries.
    - mark_resolved(query): Mark a query as resolved.
    - provide_answer(query, answer): Provide an answer to an unanswered query.
    """

    def __init__(self, bot):
        """
        Initialize the Admin instance.

        Parameters:
        - bot (object): An instance of the RuleBasedBot class for communication.
        """
        self.bot = bot
        self.unanswered_queries = {}

    def has_unanswered_queries(self):
        """
        Check if there are any unanswered queries.

        Returns:
        - bool: True if there are unanswered queries, False otherwise.
        """
        return bool(self.unanswered_queries)

    def get_unanswered_queries(self):
        """
        Get a list of unanswered queries.

        Returns:
        - list: A list of unanswered queries.
        """
        return list(self.unanswered_queries.keys())

    def mark_resolved(self, query):
        """
        Mark a query as resolved.

        Parameters:
        - query (str): The query to mark as resolved.
        """
        if query in self.unanswered_queries:
            del self.unanswered_queries[query]

    def provide_answer(self, query, answer):
        """
        Provide an answer to an unanswered query.

        Parameters:
        - query (str): The unanswered query.
        - answer (str): The answer to the query.

        Returns:
        - str: A message confirming that the answer has been provided.
        """
        self.unanswered_queries[query] = answer
        return f"Admin: {answer}"

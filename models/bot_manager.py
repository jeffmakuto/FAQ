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
    Represents an administrator for the RuleBasedBot.
    The admin can provide answers, manage unanswered queries, and mark queries as resolved.
    """

    def __init__(self, bot):
        """
        Initialize the Admin instance.

        Parameters:
        - bot (RuleBasedBot): The RuleBasedBot instance to work with.
        """
        self.bot = bot
        self.unanswered_queries = {}

    def provide_answer(self, q, a):
        """
        Provide an answer to a question, add it to the bot's database, and track it as an unanswered query.

        Parameters:
        - q (str): The question for which the admin provides an answer.
        - a (str): The admin's response to the question.
        """
        self.bot.add_to_db(q, a)
        self.unanswered_queries[q] = a

    def has_unanswered_queries(self):
        """
        Check if there are unanswered queries.

        Returns:
        - bool: True if there are unanswered queries, False otherwise.
        """
        return bool(self.unanswered_queries)

    def get_response(self, q):
        """
        Get the admin's response to a specific question.

        Parameters:
        - q (str): The question for which the admin's response is requested.

        Returns:
        - str: The admin's response or a default message if the question is not in the unanswered queries.
        """
        return self.unanswered_queries.get(q, "I don't have an answer for that, sorry.")

    def get_unanswered_queries(self):
        """
        Get the list of unanswered queries.

        Returns:
        - list: A list of unanswered queries (questions without responses).
        """
        return list(self.unanswered_queries.keys())

    def mark_resolved(self, q):
        """
        Mark a specific question as resolved, removing it from the list of unanswered queries.

        Parameters:
        - q (str): The question to mark as resolved.
        """
        if q in self.unanswered_queries:
            del self.unanswered_queries[q]

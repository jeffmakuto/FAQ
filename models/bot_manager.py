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

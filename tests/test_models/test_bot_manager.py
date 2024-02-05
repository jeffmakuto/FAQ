#!/usr/bin/env python3
""" Test for the bot manager.py file """
import unittest
from models.bot_manager import RuleBasedBot, Admin

class TestRuleBasedBot(unittest.TestCase):
    """ Test for the functionality of the RuleBasedBot class """

    @classmethod
    def setUpClass(cls):
        """ Initialize the RuleBasedBot instance with a known question """
        cls.bot = RuleBasedBot()
        cls.known_question = "What is the KQ acronym in full?"
        cls.known_answer = "Kenya Airways"
        cls.bot.add_to_db(cls.known_question, cls.known_answer)

    def test_known_query(self):
        """ Test response for a known question in the database """
        response = self.bot.respond(self.known_question)
        self.assertEqual(response, self.known_answer)

    def test_unknown_query(self):
        """ Test response for an unknown question not in the database """
        unknown_query = "Is there a legal department at Kenya Airways?"
        response = self.bot.respond(unknown_query)
        self.assertEqual(response, "I don't have an answer for that, sorry.")
        self.assertIn(unknown_query, self.bot.db)


class TestAdmin(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by creating a RuleBasedBot instance and an Admin instance.
        """
        self.bot = RuleBasedBot()
        self.admin = Admin(self.bot)

    def test_provide_answer(self):
        """
        Test the provide_answer method of the Admin class.
        """
        question = "What is the capital of France?"
        answer = "The capital of France is Paris."

        self.admin.provide_answer(question, answer)

        self.assertIn(question, self.bot.database)
        self.assertEqual(self.bot.database[question], answer)

        self.assertIn(question, self.admin.unanswered_queries)
        self.assertEqual(self.admin.unanswered_queries[question], answer)

    def test_has_unanswered_queries(self):
        """
        Test the has_unanswered_queries method of the Admin class.
        """
        self.assertFalse(self.admin.has_unanswered_queries())

        self.admin.provide_answer("Question 1", "Answer 1")
        self.assertTrue(self.admin.has_unanswered_queries())

    def test_get_response(self):
        """
        Test the get_response method of the Admin class.
        """
        question = "What is the meaning of life?"

        default_response = self.admin.get_response(question)
        self.assertEqual(default_response, "No response available")

        self.admin.provide_answer(question, "The meaning of life is 42.")
        response = self.admin.get_response(question)
        self.assertEqual(response, "The meaning of life is 42.")

    def test_get_unanswered_queries(self):
        """
        Test the get_unanswered_queries method of the Admin class.
        """
        self.assertEqual(self.admin.get_unanswered_queries(), [])

        self.admin.provide_answer("Question 1", "Answer 1")
        self.admin.provide_answer("Question 2", "Answer 2")
        unanswered_queries = self.admin.get_unanswered_queries()
        self.assertEqual(unanswered_queries, ["Question 1", "Question 2"])

    def test_mark_resolved(self):
        """
        Test the mark_resolved method of the Admin class.
        """
        question = "To be resolved"

        self.admin.provide_answer(question, "Resolved answer")
        self.assertIn(question, self.admin.unanswered_queries)

        self.admin.mark_resolved(question)
        self.assertNotIn(question, self.admin.unanswered_queries)


if __name__ == '__main__':
    unittest.main()

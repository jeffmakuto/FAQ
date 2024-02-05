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
    """
    Test that the admin receives a notification for queries users didn't find an answer to.
    Test that the admin can view the list of queries users didn't find an answer to.
    Test that the admin can mark queries as resolved
    """

    @classmethod
    def setUpClass(cls):
        """ Initialize RuleBasedBot instance and Admin instance """
        cls.bot = RuleBasedBot()
        cls.admin = Admin(cls.bot)
        cls.user_input = "How do I reset my password?"
        cls.admin_response = "You can reset your password by..."
        cls.admin.provide_answer(cls.user_input, f"Admin: {cls.admin_response}")

    def test_notification(self):
        """ Test method for if admin received a notification """
        self.assertTrue(self.admin.has_unanswered_queries())
        self.assertEqual(self.admin_response, self.admin.get_response(self.user_input))

    def test_view_unanswered_queries(self):
        """ Test method for if the admin can view the list of queries """
        self.assertIn(self.user_input, self.admin.get_unanswered_queries())

    def test_mark_resolved(self):
        """ Test method for if the admin has resolved the queries """
        self.admin.mark_resolved(self.user_input)
        self.assertFalse(self.admin.has_unanswered_queries())

if __name__ == "__main__":
    unittest.main()

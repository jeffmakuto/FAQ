""" Test for the bot manager.py file """
import unittest
from models.bot_manager import RuleBasedBot

class TestRuleBasedBot(unittest.TestCase):
    """ Test for the functionality of the RuleBasedBot class """
    def test_known_query(self):
        """
        Instance of RuleBasedBot with a known question
        in the databse
        """
        bot = RuleBasedBot()
        bot.add_to_db("What is the KQ acronym in full?", "Kenya Airways")
        response = bot.respond("What is the KQ acronym in full?")
        self.assertEqual(response, "Kenya Airways")

    def test_unknown_query(self):
        """ Test for an uknown question not in the database """
        bot = RuleBasedBot()
        response = bot.respond("Is there a legal department at Kenya Airways?")
        self.assertEqual(response, "I don't have an answer for that, sorry.")
        self.assertIn("Is there a legal department at Kenya Airways?", bot.db)

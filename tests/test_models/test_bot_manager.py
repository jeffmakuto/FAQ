""" Test for the bot manager.py file """
import unittest
from models.bot_manager import RuleBasedBot

class TestRuleBasedBot(unittest.Testcase):
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

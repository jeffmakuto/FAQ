#!/usr/bin/env python3
""" Test for nlp_manager.py file """
import unittest
from unittest.mock import patch
from back_end.models.nlp_manager import NLPManager


class TestNLPManager(unittest.TestCase):
    """ Test for the functionality of the NLPManager class """

    @classmethod
    def setUpClass(cls):
        """ Initialize the NLPManager instance """
        cls.nlp_manager = NLPManager()

    def test_process_input(self):
        """ Test processing user input using the spaCy language model """
        user_input = "Tell me about KQ's mission."
        doc = self.nlp_manager.process_input(user_input)
        self.assertIsNotNone(doc)

    def test_extract_entities(self):
        """ Test extracting entities from a spaCy processed document """
        user_input = "KQ's mission is to connect people, cultures, and markets."
        doc = self.nlp_manager.process_input(user_input)
        entities = self.nlp_manager.extract_entities(doc)
        self.assertEqual(entities, ["KQ"])

    def test_analyze_greeting(self):
        """ Test analyzing the input document for common greetings """
        greetings = ["hi", "hello", "hey"]
        for greeting in greetings:
            user_input = greeting
            doc = self.nlp_manager.process_input(user_input)
            response = self.nlp_manager.analyze_greeting(doc)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, str)

        # Test case with no greeting
        user_input = "What is KQ's mission?"
        doc = self.nlp_manager.process_input(user_input)
        response = self.nlp_manager.analyze_greeting(doc)
        self.assertIsNone(response)

    def test_analyze_mission_vision(self):
        """ Test analyzing the input document for keywords related to mission or vision """
        user_input_mission = "Tell me about KQ's mission."
        doc_mission = self.nlp_manager.process_input(user_input_mission)
        response_mission = self.nlp_manager.analyze_mission_vision(doc_mission)
        self.assertIsNotNone(response_mission)
        self.assertIsInstance(response_mission, str)

        user_input_vision = "What is KQ's vision?"
        doc_vision = self.nlp_manager.process_input(user_input_vision)
        response_vision = self.nlp_manager.analyze_mission_vision(doc_vision)
        self.assertIsNotNone(response_vision)
        self.assertIsInstance(response_vision, str)

        # Test case with no mission or vision keywords
        user_input = "What is KQ's goal?"
        doc = self.nlp_manager.process_input(user_input)
        response = self.nlp_manager.analyze_mission_vision(doc)
        self.assertIsNone(response)

    def test_analyze_scia_values(self):
        """ Test analyzing the input document for keywords related to SCIA values """
        for value in ["safety", "customer obsession", "integrity", "accountability"]:
            user_input = f"Tell me about KQ's {value}."
            doc = self.nlp_manager.process_input(user_input)
            response = self.nlp_manager.analyze_scia_values(doc)
            self.assertIsNotNone(response)
            self.assertIsInstance(response, str)

        # Test case with no SCIA value keywords
        user_input = "What are KQ's values?"
        doc = self.nlp_manager.process_input(user_input)
        response = self.nlp_manager.analyze_scia_values(doc)
        self.assertIsNone(response)

    def test_get_scenario_for_value(self):
        """ Test retrieving a scenario description for a given SCIA value """
        for value in ["safety", "customer obsession", "integrity", "accountability"]:
            scenario = self.nlp_manager.get_scenario_for_value(value)
            self.assertIsNotNone(scenario)
            self.assertIsInstance(scenario, str)

        # Test case with an unrecognized value
        unknown_value = "innovation"
        scenario = self.nlp_manager.get_scenario_for_value(unknown_value)
        self.assertEqual(scenario, "No specific scenario available.")


if __name__ == '__main__':
    unittest.main()


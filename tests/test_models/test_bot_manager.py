#!/usr/bin/env python3
""" Test for the bot manager.py file """
import unittest
from unittest.mock import patch, MagicMock
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

        # Mock the admin instance
        admin_instance = MagicMock()

        # Call the respond method
        response = self.bot.respond(
            unknown_query,
            admin_instance,
            "smtp_server",
            587,
            "sender_email",
            "sender_password",
            "recipient_email"
        )

        # Assert the response
        self.assertEqual(response, "I don't have an answer for that, sorry.")

        # Assert that the user input is added to the database
        self.assertIn(unknown_query, self.bot.db)

        # Assert that the forward_query_to_admin method is called
        admin_instance.forward_query_to_admin.assert_called_once_with(
            unknown_query,
            "smtp_server",
            587,
            "sender_email",
            "sender_password",
            "recipient_email"
        )


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
        q = "What is the capital of France?"
        a = "The capital of France is Paris."

        self.admin.provide_answer(q, a)

        self.assertIn(q, self.bot.db)
        self.assertEqual(self.bot.db[q], a)

        self.assertIn(q, self.admin.unanswered_queries)
        self.assertEqual(self.admin.unanswered_queries[q], a)

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
        q = "What is the capital city of Kenya?"

        default_response = self.admin.get_response(q)
        self.assertEqual(default_response, "I don't have an answer for that, sorry.")

        self.admin.provide_answer(q, "The capital city of Kenya is Nairobi.")
        response = self.admin.get_response(q)
        self.assertEqual(response, "The capital city of Kenya is Nairobi.")

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
        q = "To be resolved"

        self.admin.provide_answer(q, "Resolved answer")
        self.assertIn(q, self.admin.unanswered_queries)

        self.admin.mark_resolved(q)
        self.assertNotIn(q, self.admin.unanswered_queries)

    def test_forward_query_to_admin_success(self):
        """ Mock the smtplib.SMTP class and its methods """
        with patch("smtplib.SMTP") as mock_smtp:
            mock_smtp.return_value.__enter__.return_value.sendmail.return_value = None

            bot_mock = MagicMock()

            admin = Admin(bot_mock)

            smtp_server = "example.com"
            smtp_port = 587
            sender_email = "bot@example.com"
            sender_password = "bot_password"
            recipient_email = "admin@example.com"

            query = "How does this work?"

            admin.forward_query_to_admin(query, smtp_server, smtp_port, sender_email, sender_password, recipient_email)

            self.assertIn(query, admin.unanswered_queries)
            self.assertEqual(admin.unanswered_queries[query], "Forwarded to admin's email. Waiting for response.")

            mock_smtp.assert_called_once_with(smtp_server, smtp_port)
            mock_smtp.return_value.__enter__.assert_called_once()
            mock_smtp.return_value.__enter__.return_value.login.assert_called_once_with(sender_email, sender_password)
            mock_smtp.return_value.__enter__.return_value.sendmail.assert_called_once_with(
                sender_email, [recipient_email], unittest.mock.ANY
            )

    def test_forward_query_to_admin_failure(self):
        # Mock the smtplib.SMTP class and its methods to simulate an exception during email sending
        with patch("smtplib.SMTP") as mock_smtp:
            mock_smtp_instance = mock_smtp.return_value.__enter__.return_value
            mock_smtp_instance.sendmail.side_effect = Exception("Email sending failed")

            # Create an instance of RuleBasedBot (you can mock it if needed)
            bot_mock = MagicMock()

            # Create an instance of Admin
            admin = Admin(bot_mock)

            # Define SMTP server details
            smtp_server = "example.com"
            smtp_port = 587
            sender_email = "bot@example.com"
            sender_password = "bot_password"
            recipient_email = "admin@example.com"

            # Define a sample query
            query = "How does this work?"

            # Call the forward_query_to_admin method
            admin.forward_query_to_admin(query, smtp_server, smtp_port, sender_email, sender_password, recipient_email)

            # Assert that the query has been marked as unresolved with an error message
            self.assertIn(query, admin.unanswered_queries)
            self.assertEqual(admin.unanswered_queries[query], "Error forwarding to admin. Please try again.")

            # Assert that the smtplib.SMTP class and its methods were called correctly
            mock_smtp.assert_called_once_with(smtp_server, smtp_port)
            mock_smtp_instance.login.assert_called_once_with(sender_email, sender_password)
            mock_smtp_instance.sendmail.assert_called_once_with(
                sender_email, [recipient_email], unittest.mock.ANY
            )


if __name__ == '__main__':
    unittest.main()

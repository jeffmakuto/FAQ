#!/usr/bin/env python3
""" Module that handles the bot's logic features """
import smtplib
from email.mime.text import MIMEText
import logging
from .nlp_manager import NLPManager

# Configure the logger
logging.basicConfig(level=logging.INFO)


class RuleBasedBot:
    """
    Takes input processes it and answers back. If it doesn't understand,
    it answers 'I don't have an answer for that, sorry.'
    """
    def __init__(self):
        """ Initialize the database to store the data """
        self.db = {}
        self.nlp_manager = NLPManager()

    def add_to_db(self, q, a):
        """ Adds the new query to the database """
        self.db[q] = a

    def respond(self, user_input, admin_instance, smtp_server, smtp_port, sender_email, sender_password, recipient_email):
        """
        Checks if an answer is provided in the db and responds.
        If the response isn't found, it tries to answer using NLPManager.
        If not successful, it adds the query to the database,
        then forwards it to the admin and marks it as unresolved.

        Parameters:
        - user_input (str): The user's input.
        - admin_instance (Admin): An instance of the Admin class.
        - smtp_server (str): SMTP server address.
        - smtp_port (int): SMTP server port.
        - sender_email (str): Bot's email address.
        - sender_password (str): Bot's email password.
        - recipient_email (str): Admin's email address.

        Returns:
        - str: The bot's response.
        """
        # Check if the user input is in the database
        if user_input in self.db:
            return self.db[user_input]
        else:
            # Try to answer using NLPManager
            nlp_doc = self.nlp_manager.process_input(user_input)
            greeting_response = self.nlp_manager.analyze_greeting(nlp_doc)
            mission_vision_response = self.nlp_manager.analyze_mission_vision(nlp_doc)
            scia_values_response = self.nlp_manager.analyze_scia_values(nlp_doc)

            if greeting_response:
                return greeting_response
            elif mission_vision_response:
                return mission_vision_response
            elif scia_values_response:
                return scia_values_response
            else:
                # If not successful, add the query to the database and forward to admin
                self.add_to_db(user_input, "Forwarded to admin's email. Waiting for response.")
                admin_instance.forward_query_to_admin(user_input, smtp_server, smtp_port, sender_email, sender_password, recipient_email)
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
        - log : Initialize logger
        """
        self.bot = bot
        self.unanswered_queries = {}
        self.log = logging.getLogger(__name__)

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

    def forward_query_to_admin(self, q, smtp_server, smtp_port, sender_email, sender_password, recipient_email):
        """
        Forward a query to the admin's email from the bot's email and mark it as unresolved.

        Parameters:
        - q (str): The question to forward to the admin.
        - smtp_server (str): SMTP server address.
        - smtp_port (int): SMTP server port.
        - sender_email (str): Bot's email address.
        - sender_password (str): Bot's email password.
        - recipient_email (str): Admin's email address.
        """
        try:
            if q not in self.unanswered_queries:
                # Create MIMEText object
                msg = MIMEText(f"The bot received a new query:\n\n{q}\n\nPlease respond to the user.")
                msg["Subject"] = "New Query: " + q
                msg["From"] = sender_email
                msg["To"] = recipient_email

                # Establish a connection to the SMTP server
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    # Start TLS for security
                    server.starttls()

                    # Log in to the email server
                    server.login(sender_email, sender_password)

                    # Send the email
                    server.sendmail(sender_email, [recipient_email], msg.as_string())

                    # Log successful email forwarding
                    self.log.info(f"Query forwarded successfully: {q}")

                    # Add the query to unanswered_queries only if forwarding is successful
                    self.unanswered_queries[q] = "Forwarded to admin's email. Waiting for response."

        except Exception as e:
            # Log the exception and mark the query as unresolved
            self.log.error(f"Error forwarding query '{q}': {e}")
            self.unanswered_queries[q] = "Error forwarding to admin. Please try again."

class SMTPConfig:
    """
    SMTP Configuration Class

    This class encapsulates the SMTP configuration settings for the FAQ Bot.

    Attributes:
    - smtp_server (str): The SMTP server address.
    - smtp_port (int): The SMTP server port.
    - sender_email (str): The email address used for sending messages.
    - sender_password (str): The password associated with the sender's email.
    - recipient_email (str): The email address where bot responses will be sent.
    """

    def __init__(self, smtp_server, smtp_port, sender_email, sender_password, recipient_email):
        """
        Initialize SMTPConfig with specified parameters.

        Parameters:
        - smtp_server (str): The SMTP server address.
        - smtp_port (int): The SMTP server port.
        - sender_email (str): The email address used for sending messages.
        - sender_password (str): The password associated with the sender's email.
        - recipient_email (str): The email address where bot responses will be sent.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email


# Create an instance with the configuration
smtp_config_instance = SMTPConfig(
    smtp_server='mailhog',
    smtp_port=587,
    sender_email='hjeffmakuto@gmail.com',
    sender_password='',
    recipient_email='mwangombedanson@gmail.com'
)

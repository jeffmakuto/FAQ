class DBConfig:
    """
    A class representing the configuration for a database connection.

    Attributes:
        user (str): The MySQL user.
        password (str): The MySQL password.
        host (str): The MySQL host.
        port (str): The MySQL port.
        database (str): The name of the database.

    Methods:
        __init__(self, user: str, password: str, host: str, port: str, database: str): Initializes a new DBConfig instance.
        __str__(self): Returns a string representation of the DBConfig instance.
    """
    def __init__(self, user: str, password: str, host: str, port: str, database: str):
        """
        Initializes a new DBConfig instance.

        Parameters:
            user (str): The MySQL user.
            password (str): The MySQL password.
            host (str): The MySQL host.
            port (str): The MySQL port.
            database (str): The name of the database.
        """
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database

    def __str__(self) -> str:
        """
        Returns a string representation of the DBConfig instance.
        """
        return f"DBConfig(user={self.user}, password={self.password}, host={self.host}, port={self.port}, database={self.database})"

# Creating an instance of DBConfig using the provided configuration
my_db_config = DBConfig(
    user='your_mysql_user',
    password='your_mysql_password',
    host='your_mysql_host',
    port='your_mysql_port',
    database='your_database_name'
)

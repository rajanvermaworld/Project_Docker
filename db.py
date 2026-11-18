import psycopg
import os
from dotenv import load_dotenv

load_dotenv()
def get_connection():
    """
    Establishes a connection to the PostgreSQL database using psycopg.
    The connection parameters are retrieved from environment variables.

    Returns:
        psycopg.Connection: A connection object to the PostgreSQL database.
    """
    # Retrieve database connection parameters from environment variables
    connection_result = psycopg.connect(
        host = "localhost",
        port = 5432,
        dbname = "docker_testapp",
        user = "postgres",
        password = os.getenv("db_password")
    )

    return connection_result
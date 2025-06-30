# db_connection.py



import mysql.connector
from configparser import ConfigParser
from exception.catalogue_custom_exceptions import CatalogueException

def get_db_connection():
    try:
        config = ConfigParser()
        config.read('config/dbconnection.ini')

        host = config.get('mysql', 'host')
        user = config.get('mysql', 'user')
        password = config.get('mysql', 'password')
        database = config.get('mysql', 'database')

        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    except Exception as e:
        raise CatalogueException(f"Database connection failed: {str(e)}")


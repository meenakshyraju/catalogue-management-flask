# user_service.py

import mysql.connector
from util.db_connection_util import get_db_connection

class UserService:
    def validate_user(self, username, password):
        connection = None
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM Users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()
            return result is not None
        except Exception as e:
            raise Exception(f"Login failed: {str(e)}")
        finally:
            if connection and connection.is_connected():
                connection.close()

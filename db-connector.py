import os
import mysql-connector-python
from mysql-connector import Error

host = os.environ.get('DB_HOST')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
database = os.environ.get('DATABASE')

print(f"[Info]: Checking DB Connection")
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("[Success]: Connected to database!")
    except Error as err:
        print(f"[Error]: '{err}'")

        return connection

connection = create_server_connection(db_host, db_username, db_password)

import mysql-connector
from mysql-connector import Error

db_host = "172.17.0.2"
db_username = "root"
db_password =  "root"
db_name = "test"

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

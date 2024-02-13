import mysql.connector
from mysql.connector import Error


# CONNECTION A LA DB SANS SON NOM
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        # print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# CONNECTION A LA DB AVEC SON NOM
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            autocommit = True
        )
        # print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection
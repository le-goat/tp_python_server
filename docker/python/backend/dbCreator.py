import mysql.connector
from mysql.connector import Error
from dbConnector import create_server_connection
   
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")  
        
     
connection = create_server_connection("localhost", "root", "")       
query = "CREATE DATABASE pythonAnsible"   
create_database(connection, query)
connection.close()









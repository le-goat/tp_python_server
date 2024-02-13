import mysql.connector
from mysql.connector import Error
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from dbConnector import create_server_connection
import os
   
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")  
        
load_dotenv(find_dotenv())
     
connection = create_server_connection("localhost", "root", os.getenv("PASSWORD"))       
query = "CREATE DATABASE pythonAnsible"   
create_database(connection, query)
connection.close()









from dotenv import load_dotenv, find_dotenv
from mysql.connector import Error
from dbConnector import create_db_connection
from dbExecutor import execute_query
import os

load_dotenv(find_dotenv())

create_eurodollarsecond_table = """CREATE TABLE interator (state INT NOT NULL) ;"""
connection = create_db_connection("localhost", "root", "", "pythonAnsible") # Connect to the Database
execute_query(connection, create_eurodollarsecond_table) # Execute our defined query
connection.close()
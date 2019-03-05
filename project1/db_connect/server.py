import psycopg2 
from config import app_configuration
from psycopg2.extras import RealDictCursor
from .relation_commands import sqlcommands
import os

class DatabaseConnect:

    def __init__(self):
        self.credentials = dict(
                dbname ='books_db',
                user = 'postgres',
                host='localhost',
                port = 5432
            )

        
        self.conn =  psycopg2.connect(**self.credentials, cursor_factory=RealDictCursor)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()


        for command in sqlcommands:
            self.cursor.execute(command)
            print(f"connection successful on {self.credentials}")


      

    def drop_table(self,tablename):
        command = f"""
        DROP TABLE IF EXISTS {tablename} CASCADE
        """
        return self.cursor.execute(command)
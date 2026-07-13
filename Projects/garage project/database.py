import mysql.connector

class Database:
    def connect(self):

        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="0000",
            database="garage_db2"
        )
        return con
    
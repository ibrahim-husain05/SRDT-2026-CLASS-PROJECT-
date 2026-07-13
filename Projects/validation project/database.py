import mysql.connector
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="login_system"
        )
        self.cursor = self.connection.cursor(buffered=True)

    def execute(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

        if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
            self.connection.commit()
            
    def fetchone(self):
        return self.cursor.fetchone()
        
    def fetchall(self):
        return self.cursor.fetchall()
        
    def close(self):
        self.cursor.close()
        self.connection.close()
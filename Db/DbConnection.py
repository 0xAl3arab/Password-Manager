import sqlite3


class DbConnection:
    def __init__(self):
        self.connection = sqlite3.connect('../Db/fastpass.db')
        self.cursor = self.connection.cursor()
        self.commit = self.connection.commit()

    def close_connection(self):
        self.connection.close()
        self.cursor.close()


def start_db():
    dbconn = DbConnection()
    dbconn.cursor.execute("CREATE TABLE IF NOT EXISTS Users (id int AUTO_INCREMENT PRIMARY KEY ,username VARCHAR(50) NOT NULL ,password VARCHAR(100) NOT NULL);")
    dbconn.commit
    res = dbconn.cursor.fetchall()
    print(res)
    print("DATABASE RUNNING SUCCEFULLY")
import sqlite3


class DbConnection:
    def __init__(self):
        self.connection = sqlite3.connect('./fastpass.db')
        self.cursor = self.connection.cursor()
        self.commit = self.connection.commit()

    def close_connection(self):
        self.connection.close()
        self.cursor.close()


def start_db():
    dbconn = DbConnection()
    dbconn.cursor.execute(
        "CREATE TABLE IF NOT EXISTS Users (id INTEGER   PRIMARY KEY ,username VARCHAR(50) NOT NULL ,password VARCHAR(100) NOT NULL);")
    # in sql lite standards auto increment is added directly by mention its integer and pk
    dbconn.commit
    user = ("a", "d")
    dbconn.cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", user)

    dbconn.cursor.execute("Select * FROM Users")
    res = dbconn.cursor.fetchone()
    print(len(res))
    dbconn.commit
    print("DATABASE RUNNING SUCCEFULLY")


start_db()
import bcrypt
import Db.DbConnection as Db

dbconn = Db.DbConnection()

class SignUp:

    def sign_up(self, username, password):
        bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        psw = bcrypt.hashpw(bytes, salt)
        user = (username, psw)

        check = dbconn.cursor.execute("select * from USERS where username = ?", (username,))
        res = check.fetchone()

        if (res is None):
            dbconn.cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)", user)
            dbconn.commit()
            dbconn.cursor.execute("SELECT * FROM Users")
            res = dbconn.cursor.fetchall()
            print(res)
            return True, "Account created successfully"
        else:
            return False, "Username already exists"
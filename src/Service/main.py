from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from Ui.LoginPage import LoginPage
from Ui.SignUpPage import SignUpPage
import sqlite3
import bcrypt


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.loginPage = LoginPage()
        self.signUpPage = SignUpPage()
        self.loginPage.show()  # Show login first
        self.connect_signals()

    def connect_signals(self):
        #get the signal (when the create account btn is clicked) from LoginPage and call showSignUpPage
        self.loginPage.create_account_signal.connect(self.showSignUpPage)
        #get signal when Login button is clicked
        self.loginPage.login_button_signal.connect(self.login)

    def login(self):
        username = self.loginPage.username_input.text()
        password = self.loginPage.password_input.text()
        encoded_password = password.encode('utf-8')

        #open db 
        conn = sqlite3.connect('../Db/fastpass.db')

        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username= ? " , (username,))
        result = cursor.fetchone()

        conn.close()

        if result is None :
            self.loginPage.message_label.setText("Username does not exist")
            return False
            #print username doesnt exist
        
        hashed_password = result[0]

        if bcrypt.checkpw( encoded_password , hashed_password ) :
            self.loginPage.message_label.setText("Login successful")
            return True
            #redirect to home page
        

        self.loginPage.message_label.setText("Username or password incorrect")
        return False
        #handle password incorrect

    def showSignUpPage(self):
        self.loginPage.hide()
        self.signUpPage.show()
    
    





app = QApplication([])
window = MainPage()
app.exec()
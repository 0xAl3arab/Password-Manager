from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QFormLayout, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel , QStackedWidget
from PyQt5.QtCore import QSize, Qt 
import sys
from pages.LoginPage import LoginPage
from pages.SignUpPage import SignUpPage
import sqlite3
import bcrypt


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_stacked_widget = QStackedWidget()
        self.setCentralWidget(self.central_stacked_widget)

        self.loginPage = LoginPage()
        self.signUpPage = SignUpPage()

        #add the two pages to the central widget which is the container
        self.central_stacked_widget.addWidget(self.loginPage)
        self.central_stacked_widget.addWidget(self.signUpPage)

        #show the login page on startup always
        self.central_stacked_widget.setCurrentWidget(self.loginPage)



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
        self.central_stacked_widget.setCurrentWidget(self.signUpPage)
    
    





app = QApplication([])
window = MainPage()
window.show()
app.exec()
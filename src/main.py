from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QFormLayout, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel , QStackedWidget
from PyQt5.QtCore import QSize, Qt 
import sys
from pages.LoginPage import LoginPage
from pages.SignUpPage import SignUpPage


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

        #get the signal (when the create account btn is clicked) from LoginPage and call showSignUpPage
        self.loginPage.create_account_signal.connect(self.showSignUpPage)

    def showSignUpPage(self):
        self.central_stacked_widget.setCurrentWidget(self.signUpPage)





app = QApplication([])
window = MainPage()
window.show()
app.exec()
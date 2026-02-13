from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QFormLayout, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel , QStackedWidget
from PyQt5.QtCore import QSize, Qt 
import sys
from pages.LoginPage import LoginPage

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()

        central_stacked_widget = QStackedWidget()
        self.setCentralWidget(central_stacked_widget)

        loginPage = LoginPage()

        central_stacked_widget.addWidget(loginPage)
        central_stacked_widget.setCurrentWidget(loginPage)





app = QApplication([])
window = MainPage()
window.show()
app.exec()
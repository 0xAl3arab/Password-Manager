from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QFormLayout, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QSize, Qt 
import sys

WINDOW_WIDTH = 550
WINDOW_HEIGHT = 600
INPUT_WIDTH = 230
INPUT_HEIGHT = 30
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 30

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Form container and layout
        form_widget = QWidget()
        form_layout = QFormLayout()
        form_widget.setLayout(form_layout)

        # Username row
        username_input = QLineEdit()
        username_input.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        username_widget = QWidget()
        username_layout = QHBoxLayout()
        username_layout.addWidget(username_input, alignment=Qt.AlignLeft)
        username_widget.setLayout(username_layout)
        form_layout.addRow("Username:", username_widget)
        username_layout.setContentsMargins(0,0,0,0)

        # Password row
        password_input = QLineEdit()
        password_input.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        show_password_button = QPushButton("show")
        show_password_button.setFixedSize(40, BUTTON_HEIGHT)
        password_widget = QWidget()
        password_layout = QHBoxLayout()
        password_layout.addWidget(password_input)
        password_layout.addWidget(show_password_button)
        password_widget.setLayout(password_layout)
        form_layout.addRow("Master password:", password_widget)
        password_layout.setContentsMargins(0,0,0,0)


        # Login button row
        login_button = QPushButton("Login")
        login_button.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        login_widget = QWidget()
        login_layout = QHBoxLayout()
        login_layout.addWidget(login_button, alignment=Qt.AlignHCenter)
        login_widget.setLayout(login_layout)
        form_layout.addRow(login_widget)

        # Add form to main layout and center
        main_layout.addStretch()
        main_layout.addWidget(form_widget, alignment=Qt.AlignHCenter)
        main_layout.addStretch()


app = QApplication(sys.argv)
window = LoginPage()
window.show()
app.exec()

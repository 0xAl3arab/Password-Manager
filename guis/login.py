from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow , QFormLayout ,QLineEdit ,QVBoxLayout
from PyQt5.QtCore import QSize , Qt 
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
        self.setFixedSize(WINDOW_WIDTH,WINDOW_HEIGHT)

        central_widget= QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        #form container
        formWidget = QWidget()
        form_layout = QFormLayout()

        #form elements
        username_input = QLineEdit();username_input.setFixedSize(INPUT_WIDTH,INPUT_HEIGHT)
        password_input = QLineEdit();password_input.setFixedSize(INPUT_WIDTH,INPUT_HEIGHT)
        login_button = QPushButton("Login");login_button.setFixedSize(BUTTON_WIDTH,BUTTON_HEIGHT)

        form_layout.addRow("Username:", username_input)
        form_layout.addRow("Master password:", password_input)
        form_layout.addRow(login_button)
        formWidget.setLayout(form_layout)


        main_layout.addStretch()
        main_layout.addWidget(formWidget , alignment = Qt.AlignHCenter)
        main_layout.addStretch()


        

app = QApplication(sys.argv)
window = LoginPage()
window.show()
app.exec()






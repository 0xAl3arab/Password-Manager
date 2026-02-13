from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QFormLayout, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel
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
        self.password_input = QLineEdit()
        self.password_input.setFixedSize(INPUT_WIDTH, INPUT_HEIGHT)
        self.show_password_button = QPushButton(self)
        self.show_password_button.setText("show")
        self.show_password_button.setCheckable(True)

        self.show_password_button.toggled.connect(self.show_password_button_toggled)
        
        self.show_password_button.setFixedSize(40, BUTTON_HEIGHT)
        password_widget = QWidget()
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.show_password_button)
        password_widget.setLayout(password_layout)
        form_layout.addRow("Master password:", password_widget)
        password_layout.setContentsMargins(0,0,0,0)

        #option to create new account
        button_text = "create new one"
        self.create_account_button = QPushButton(button_text)
        self.create_account_button.setFlat(True)
        self.create_account_button.setFixedSize(BUTTON_WIDTH-30,BUTTON_HEIGHT)
        create_account_text = QLabel()
        create_account_text.setText("don't have an account ?")
        create_account_text.setFixedSize(BUTTON_WIDTH+15,BUTTON_HEIGHT)


        create_account_widget = QWidget()
        create_account_layout = QHBoxLayout()
        create_account_layout.addStretch(1)
        create_account_layout.addWidget(create_account_text)
        create_account_layout.addWidget(self.create_account_button)
        create_account_layout.addStretch(1)

        create_account_layout.setContentsMargins(25,0,0,0)

        create_account_widget.setLayout(create_account_layout)

        form_layout.addRow(create_account_widget)
        

        # Login button row
        login_button = QPushButton("Login")
        login_button.setFixedSize(BUTTON_WIDTH, BUTTON_HEIGHT)
        login_widget = QWidget()
        login_layout = QHBoxLayout()
        login_layout.addWidget(login_button, alignment=Qt.AlignHCenter)
        login_layout.setContentsMargins(0,0,0,0)
        login_widget.setLayout(login_layout)
        form_layout.addRow(login_widget)

        # Add form to main layout and center
        main_layout.addStretch()
        main_layout.addWidget(form_widget, alignment=Qt.AlignHCenter)
        main_layout.addStretch()
    

    def show_password_button_toggled(self):
        btn = self.show_password_button
        state = btn.isChecked()
        if state==True:
            btn.setText("hide")
            self.password_input.setEchoMode(QLineEdit.Password)
        else:
            btn.setText("show")
            self.password_input.setEchoMode(QLineEdit.Normal)



def main():
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    app.exec()



if __name__=="__main__":
    main()
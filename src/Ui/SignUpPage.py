import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QCheckBox, QPushButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
import Db.DbConnection as Db
from Ui.LoginPage import LoginPage
from Service.SignUp import SignUp

dbconn = Db.DbConnection()


class SignUpPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.sign_up_service = SignUp()
        self.setWindowTitle("FastPass - SignUp")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon('../../Assets/FastPassLogo.svg'))
        self.setFixedSize(500, 500)
        label = QLabel("Sign Up", self)
        label.setGeometry(0, 90, 500, 500)
        label.setAlignment(Qt.AlignHCenter)
        label.setStyleSheet("color:blue;"
                            "font-size:35px;"
                            "font-family:Arial;"
                            "font-weight:bold;"
                            "font-style:italic;")
        logolabel = QLabel(self)
        logolabel.setGeometry(100, 0, 90, 90)
        logo = QPixmap("../../Assets/FastPassLogo.svg")
        logolabel.setPixmap(logo)
        logolabel.setScaledContents(True)

        nameLabel = QLabel("FastPass", self)
        nameLabel.setGeometry(180, 5, 500, 90)
        nameLabel.setStyleSheet("font-size:50px;")

        Username = QLabel("Username", self)
        Username.setGeometry(50, 170, 50, 50)

        self.inputUser = QLineEdit(self)
        self.inputUser.setGeometry(150, 180, 220, 30)

        password = QLabel("Password", self)
        password.setGeometry(50, 220, 220, 50)

        self.inputPass = QLineEdit(self)
        self.inputPass.setGeometry(150, 230, 220, 30)

        ConfirmPassword = QLabel("Confirm Password", self)
        ConfirmPassword.setGeometry(50, 280, 300, 50)

        self.setStyleSheet("""
            QLineEdit {
                border-radius: 10px;
                border : 1px solid black;
                font-family: MV Boli;
                font-weight:bold;
                font-size : 20px
            }
            QPushButton:hover {
                background-color:black;
                color:white;
                cursor:pointer;
            }
            QLineEdit{
                padding: 0px ;
                padding-left : 5px;
                padding-right: 5px;
            }
        """)

        self.inputCrPass = QLineEdit(self)
        self.inputCrPass.setGeometry(150, 290, 220, 30)

        self.inputPass.setEchoMode(QLineEdit.Password)
        self.inputCrPass.setEchoMode(QLineEdit.Password)

        self.show_hidePass = QLabel(self)
        self.show_hidePass.setGeometry(400, 235, 20, 20)
        eye = QPixmap("../../Assets/eye-password-show.svg")
        self.show_hidePass.setPixmap(eye)
        self.show_hidePass.setScaledContents(True)
        self.show_hidePass.setCursor(Qt.PointingHandCursor)

        self.show_hidePassCr = QLabel(self)
        self.show_hidePassCr.setGeometry(400, 295, 20, 20)
        self.show_hidePassCr.setPixmap(eye)
        self.show_hidePassCr.setScaledContents(True)
        self.show_hidePassCr.setCursor(Qt.PointingHandCursor)
        self.show_hidePass.mousePressEvent = self.toggle_password
        self.show_hidePassCr.mousePressEvent = self.toggle_password_confirm

        self.checkregulation = QCheckBox("Notice !", self)
        self.checkregulation.setGeometry(130, 350, 220, 30)

        self.login_page = QLabel("I already have an account", self)
        self.login_page.mousePressEvent = self.open_login_page
        self.login_page.setGeometry(0, 420, 500, 100)
        self.login_page.setAlignment(Qt.AlignCenter)
        self.login_page.setStyleSheet("""
            QLabel:hover{
                color: blue;
            }
        """)
        self.login_page.setCursor(Qt.PointingHandCursor)

        self.checkregulation.setStyleSheet("color : red ;")
        label2 = QLabel(": If you forget the password you are COOKED  \n you cannot recover it save it somewhere buddy",
                        self)
        label2.setGeometry(190, 353, 250, 35)
        self.submitbutton = QPushButton("Sign Up", self)
        self.submitbutton.setGeometry(215, 400, 70, 40)
        self.submitbutton.setStyleSheet("border-radius:10px;"
                                        "border : 1px solid black;"
                                        )
        self.submitbutton.setDisabled(True)
        self.submitbutton.clicked.connect(self.sign_up)
        self.problabel = QLabel(self)
        self.problabel.setGeometry(0, 320, 500, 30)
        self.problabel.setAlignment(Qt.AlignCenter)
        self.checkregulation.stateChanged.connect(self.checked)

    def checked(self, state):
        if state == Qt.Checked:
            self.submitbutton.setDisabled(False)
            self.submitbutton.setCursor(Qt.PointingHandCursor)
        else:
            self.submitbutton.setDisabled(True)

    def toggle_password(self, event):
        if self.inputPass.echoMode() == QLineEdit.Password:
            self.inputPass.setEchoMode(QLineEdit.Normal)
            self.show_hidePass.setPixmap(QPixmap("../../Assets/eye-password-see-view.svg"))
        else:
            self.inputPass.setEchoMode(QLineEdit.Password)
            self.show_hidePass.setPixmap(QPixmap("../../Assets/eye-password-show.svg"))

    def toggle_password_confirm(self, event):
        if self.inputCrPass.echoMode() == QLineEdit.Password:
            self.inputCrPass.setEchoMode(QLineEdit.Normal)
            self.show_hidePassCr.setPixmap(QPixmap("../../Assets/eye-password-see-view.svg"))
        else:
            self.inputCrPass.setEchoMode(QLineEdit.Password)
            self.show_hidePassCr.setPixmap(QPixmap("../../Assets/eye-password-show.svg"))

    def sign_up(self):
        username = self.inputUser.text()
        password = self.inputPass.text()
        confimPass = self.inputCrPass.text()

        """print(username)
        print(password)
        print(confimPass)"""

        if (password != confimPass):
            self.problabel.setText("Passwords do not match")
            return

        success, message = self.sign_up_service.sign_up(username, password)
        self.problabel.setText(message)
        if success:
            QTimer.singleShot(2000, self.loginpage)

    # going automatically after sign up
    def loginpage(self):
        self.close()
        self.login_window = LoginPage()
        self.login_window.show()

    # for the button already have an account
    def open_login_page(self, event):
        self.close()
        self.login_window = LoginPage()
        self.login_window.show()


def main():
    Db.start_db()
    app = QApplication(sys.argv)
    window = SignUpPage()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
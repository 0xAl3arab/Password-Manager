import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication , QMainWindow ,QLabel , QLineEdit , QCheckBox ,QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap , QFont
import Db.DbConnection as Db

class SignUpPage(QMainWindow):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("FastPass - SignUp")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon('Assets/1849-logo-1713617130.076color-00a3e4.svg'))
        self.setFixedSize(500,500)
        label = QLabel("Sign Up",self)
        label.setGeometry(0,90,500,500)
        label.setAlignment(Qt.AlignHCenter)
        label.setStyleSheet("color:blue;"
                            "font-size:35px;"
                            "font-family:Arial;"
                            "font-weight:bold;"
                            "font-style:italic;")
        logolabel = QLabel(self)
        logolabel.setGeometry(100,0,90,90)
        logo = QPixmap("../Assets/1849-logo-1713617130.076color-00a3e4.svg")
        logolabel.setPixmap(logo)
        logolabel.setScaledContents(True)

        nameLabel = QLabel("FastPass",self)
        nameLabel.setGeometry(180,5,500,90)
        nameLabel.setStyleSheet("font-size:50px;")

        Username = QLabel("Username",self)
        Username.setGeometry(50,170,50,50)


        self.inputUser = QLineEdit(self)
        self.inputUser.setGeometry(150,180,220,30)

        password = QLabel("Password", self)
        password.setGeometry(50, 220, 220, 50)

        self.inputPass = QLineEdit(self)
        self.inputPass.setGeometry(150 , 230, 220, 30)

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
        """)


        self.inputCrPass = QLineEdit(self)
        self.inputCrPass.setGeometry(150, 290, 220, 30)

        self.checkregulation = QCheckBox("Notice !",self)
        self.checkregulation.setGeometry(130, 350, 220, 30)

        self.checkregulation.setStyleSheet("color : red ;")
        label2 = QLabel(": If you forget the password you are COOKED  \n you cannot recover it save it somewhere buddy",self)
        label2.setGeometry(190,353,250,35)
        self.submitbutton = QPushButton("Sign Up",self)
        self.submitbutton.setGeometry(225,400,70,40)
        self.submitbutton.setStyleSheet("border-radius:10px;"
                                   "border : 1px solid black;"
                                   )
        self.submitbutton.setDisabled(True)

        self.checkregulation.stateChanged.connect(self.checked)


    def checked(self,state):
        if state == Qt.Checked:
            self.submitbutton.setDisabled(False)
        else :
            self.submitbutton.setDisabled(True)

    def sign_up(self):
        username = self.inputUser.text()
        password = self.inputPass.text()
        confimPass = self.inputCrPass.text()




def main():
    Db.start_db()
    app = QApplication(sys.argv)
    window = SignUpPage()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()
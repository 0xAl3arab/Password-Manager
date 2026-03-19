import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QCheckBox, QPushButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
import Db.DbConnection as Db
from Ui.LoginPage import LoginPage
from Service.SignUp import SignUp

dbconn = Db.DbConnection()


class MainPage(QMainWindow):

    def __init__(self):
        super().__init__()

def main():
    Db.start_db()
    app = QApplication(sys.argv)
    window = SignUpPage()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
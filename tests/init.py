from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtCore import QSize


import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface")
        self.setFixedSize(QSize(400,300))
        


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FastPass - MainPage")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon(QIcon('../../Assets/FastPassLogo.svg'))
        self.setFixedSize(500, 500)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Platform", "Email", "Password"])
        self.table.setRowCount(10)
        layout.addWidget(self.table)


def main():
    app = QApplication(sys.argv)
    window = MainPage()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

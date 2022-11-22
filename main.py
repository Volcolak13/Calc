from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calc")
        button = QPushButton("Test")
        self.setCentralWidget(button)
        self.setFixedSize(QSize(400, 300))


window = MainWindow()
window.show()


app.exec()

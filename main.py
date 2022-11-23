from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QLCDNumber
import sys


class Buttn(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("test")
        print("Buttn init")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("MaiinWindow initialization")

        self.setFixedSize(QSize(270, 300))
        self.setWindowTitle("Calc")

        btns1 = ["C", "DEL", ".", "*"]
        btns2 = ["1", "2", "3", "/"]
        btns3 = ["4", "5", "6", "+"]
        btns4 = ["7", "8", "9", "-"]
        btns5 = ["+/-", "0", ".", "="]

        # self.label = QLabel()
        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)

        # self.button = QPushButton("Test")
        # self.button = Buttn()
        self.LCD = QLCDNumber()
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()
        layout6 = QHBoxLayout()
        layout7 = QHBoxLayout()
        layout8 = QHBoxLayout()

        layout2.addWidget(self.LCD)

        for bt in btns1:
            button = QPushButton(bt)
            button.setFixedSize(QSize(60, 30))
            # button.clicked.connect(self.the_button_was_clicked)
            button.clicked.connect(lambda: self.set_digit(bt))
            layout3.addWidget(button)

        for bt in btns2:
            button = QPushButton(bt)
            button.setFixedSize(QSize(60, 30))
            button.clicked.connect(lambda: self.set_digit(bt))
            layout4.addWidget(button)

        for bt in btns3:
            button = QPushButton(bt)
            button.setFixedSize(QSize(60, 30))
            button.clicked.connect(lambda: self.set_digit(bt))
            layout5.addWidget(button)

        for bt in btns4:
            button = QPushButton(bt)
            button.setFixedSize(QSize(60, 30))
            button.clicked.connect(lambda: self.set_digit(bt))
            layout6.addWidget(button)

        for bt in btns5:
            button = QPushButton(bt)
            button.setFixedSize(QSize(60, 30))
            button.clicked.connect(lambda: self.set_digit(bt))
            layout7.addWidget(button)

        btt = "111"
        layout8.addWidget(QPushButton(btt))
        button.setFixedSize(QSize(60, 30))
        button.clicked.connect(lambda: self.set_digit(btt))

        # layout = QVBoxLayout()
        # layout.addWidget(self.input)
        # layout.addWidget(self.label)

        # layout.addWidget(self.button)
        # self.button.clicked.connect(self.the_button_was_clicked)

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)
        layout1.addLayout(layout4)
        layout1.addLayout(layout5)
        layout1.addLayout(layout6)
        layout1.addLayout(layout7)
        layout1.addLayout(layout8)
        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)

    def set_digit(self, value):
        print(value)
        self.LCD.display(value)

    def the_button_was_clicked(self):
        # self.button.setText("Done")
        print("clicked")


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()

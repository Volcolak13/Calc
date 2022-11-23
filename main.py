from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QLCDNumber
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
        
        # self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("Calc")

        btns1 = ["C", "DEL", "=", "*"]
        btns2 = ["1", "2", "3", "/"]
        btns3 = ["4", "5", "6", "+"]
        btns4 = ["7", "8", "9", "-"]
        btns5 = ["(", "0", ")", "X^2"]

        # self.label = QLabel()
        # self.input = QLineEdit()
        # self.input.textChanged.connect(self.label.setText)

        # self.button = QPushButton("Test")
        # self.button = Buttn()
        LCD = QLCDNumber()
        layout1 = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout3 = QHBoxLayout()
        layout4 = QHBoxLayout()
        layout5 = QHBoxLayout()
        layout6 = QHBoxLayout()
        layout7 = QHBoxLayout()

        layout2.addWidget(LCD)

        for bt in btns1:
            button = QPushButton(bt)
            button.com = bt
            print(button.com)
            layout3.addWidget(button)

        for bt in btns2:
            button = QPushButton(bt)
            layout4.addWidget(button)

        for bt in btns3:
            button = QPushButton(bt)
            layout5.addWidget(button)

        for bt in btns4:
            button = QPushButton(bt)
            layout6.addWidget(button)
        
        for bt in btns5:
            button = QPushButton(bt)
            layout7.addWidget(button)
        

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
        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)
    
    def the_button_was_clicked(self):
        # self.button.setText("Done")
        print("clicked")


app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()

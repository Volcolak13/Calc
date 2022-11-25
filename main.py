from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QGridLayout
import sys


class Buttn(QPushButton):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.setText(name)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.setFixedSize(QSize(265, 370))

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ["C", "DEL", "", "*",
                 "1", "2", "3", "/",
                 "4", "5", "6", "+",
                 "7", "8", "9", "-",
                 "+/-", "0", ".", "="]

        positions = [(i, j) for i in range(2, 7) for j in range(4)]

        self.LCD = QLCDNumber()
        self.formula = "0"
        self.LCD.display(self.formula)
        self.LCD.setFixedHeight(40)
        self.LCD.setDigitCount(12)
        self.LCD.setDecMode()
        grid.addWidget(self.LCD, 0, 0, 1, 4)

        self.buttons = []

        for position, name in zip(positions, names):
            if name == '':
                continue
            button = Buttn(name)
            button.setFixedSize(QSize(60, 60))
            button.clicked.connect(lambda ch, name=name:
                                   self.the_button_was_clicked(name))
            self.buttons.append(button)
            grid.addWidget(button, *position)

        self.move(1200, 550)
        self.setWindowTitle('Calculator')
        self.show()

    def the_button_was_clicked(self, value):
        if value == "+/-":
            value = "-"
        self.logica(value)

    def logica(self, value):

        if self.formula == "0":
            self.formula = value
        # elif len(self.formula) >= 11:
        #     self.formula = "ERROR"
        #    self.formula = "0"
        elif value == "C":
            self.formula = "0"
        elif value == "DEL":
            self.formula = str(self.formula[:-1])
        elif value == "*" or value == "/" or value == "+" or value == "-":
            self.formula += value
        elif value == "=":
            self.formula = str(round(eval(self.formula), 3))
            if len(self.formula) >= 11:
                self.formula = "ERROR"
        else:
            self.formula += value
        self.LCD.display(self.formula)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QGridLayout
from math import sqrt
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

        self.setFixedSize(265, 435)

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ["C", "DEL", "", "*",
                 "%", "SQRT", "X^2", "1/X",
                 "1", "2", "3", "/",
                 "4", "5", "6", "+",
                 "7", "8", "9", "-",
                 "+/-", "0", ".", "="]

        positions = [(i, j) for i in range(2, 8) for j in range(4)]

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
        elif value == "%" or value == "SQRT" or value == "X^2" or value == "1/X":
            value = self.prcs(value)
            self.formula = "0"

        self.logica(value)

    def prcs(self, x):
        if float(self.formula) > 0:
            if x == "SQRT":
                x = str(round(sqrt(float(self.formula)), 5))
            elif x == "X^2":
                x = str(round((float(self.formula)**2), 5))
            elif x == "1/X":
                x = str(round((1/float(self.formula)), 5))
        elif float(self.formula) == 0:
            if x == "SQRT":
                x = "0"
            elif x == "X^2":
                x = "0"
            elif x == "1/X":
                x = "ERROR"
        else:
            if x == "SQRT":
                x = "ERROR"
            elif x == "X^2":
                x = str(round((float(self.formula)**2), 5))
            elif x == "1/X":
                x = str(round((1/float(self.formula)), 5))
        
        return x
        # if self.formula > "0":
        #     
        # elif self.formula == "0":
        #     x = "0"
        # else:
        #     x = "ERROR"
        # return x

    def logica(self, value):

        if self.formula == "0":
            self.formula = value
        elif value == "C":
            self.formula = "0"
        elif value == "DEL":
            self.formula = str(self.formula[:-1])
        elif value == "*" or value == "/" or value == "+" or value == "-":
            self.formula += value
        elif value == "=":
            self.formula = str(round(eval(self.formula), 5))
            if len(self.formula) >= 11:
                self.formula = "ERROR"
                self.formula = "0"
        else:
            self.formula += value
        self.LCD.display(self.formula)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QGridLayout
from PyQt6 import QtGui
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
        """User Interface initialization."""
        grid = QGridLayout()
        self.setLayout(grid)

        names = ["C", "DEL", "MR+", "MR",
                 "%", "SQRT", "X^2", "1/X",
                 "1", "2", "3", "/",
                 "4", "5", "6", "+",
                 "7", "8", "9", "-",
                 "+/-", "0", ".", "="]

        self.func = ["SQRT", "X^2", "1/X", "+/-"]

        positions = [(i, j) for i in range(2, 8) for j in range(4)]

        self.LCD = QLCDNumber()
        self.formula = "0"
        self.mr = "0"
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
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.show()

    def the_button_was_clicked(self, value):
        """Button action processor."""
        if value in self.func:
            value = self.prcs(value, self.formula)
            self.formula = "0"
        if value == "C":
            self.formula = "0"
            value = "0"
        elif value == "DEL":
            if self.formula == "0" or self.formula == "DEL":
                value = ""
            self.formula = str(self.formula[:-1])
            value = ""
            if self.formula == "":
                value = "0"
        elif value == "MR+":
            value = ""
            self.mr = self.formula
        elif value == "MR":
            value = self.mr

        self.logica(value)

    def prcs(self, x, y):
        """Function processor."""
        if float(y) > 0:
            if x == "SQRT":
                x = str(round(sqrt(float(y)), 5))
            elif x == "X^2":
                x = str(round((float(y)**2), 5))
            elif x == "1/X":
                x = str(round((1/float(y)), 5))
            elif x == "+/-":
                x = str(float(y)*(-1))
        elif float(y) == 0 or (y) == "":
            self.formula = "0"
            if x == "SQRT":
                x = "0"
            elif x == "X^2":
                x = "0"
            elif x == "1/X":
                x = "0"
            elif x == "+/-":
                x = "0"
        else:
            if x == "SQRT":
                x = "0"
            elif x == "X^2":
                x = str(round((float(y)**2), 5))
            elif x == "1/X":
                x = str(round((1/float(y)), 5))
            elif x == "+/-":
                x = str(float(y)*(-1))
        return x

    def perc(self, formula):
        """Persenc function processor."""
        x = formula.split("%")
        if x[0] == "0" or x[0] == "" or x[1] == "0" or x[1] == "":
            x = "0"
        else:
            x = str(float(x[0])*(float(x[1])/100))
        return x

    def logica(self, value):
        """Main logic."""

        if self.formula == "0":
            self.formula = value
        elif value == "*" or value == "/" or value == "+" or value == "-":
            if self.formula == "":
                self.formula = "0"
            else:
                self.formula += value
        elif value == "=":
            if "%" in self.formula:
                self.formula = self.perc(self.formula)
            elif "=" in self.formula:
                self.formula = "0"
            self.formula = str(round(eval(self.formula), 5))
            if len(self.formula) >= 11:
                self.formula = "0"
        else:
            self.formula += value
        self.LCD.display(self.formula)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from linear import LinearWindow
from multivariable import MultiVariableWindow
from ga import GAWindow
from constrained import ConstrainedWindow
from multiobjective import MultiObjectiveWindow
from wing import WingWindow
from manufacturing import ManufacturingWindow

from ui_menu import Ui_wMenu

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wMenu()
        self.ui.setupUi(self)
        self.ui.btnLinear.clicked.connect(self.btnLinear_clicked)
        self.ui.btnMultiVariable.clicked.connect(self.btnMultiVariable_clicked)
        self.ui.btnGA.clicked.connect(self.btnGA_clicked)
        self.ui.btnConstrained.clicked.connect(self.btnConstrained_clicked)
        self.ui.btnMultiObjective.clicked.connect(self.btnMultiObjective_clicked)
        self.ui.btnWing.clicked.connect(self.btnWing_clicked)
        self.ui.btnManufacturing.clicked.connect(self.btnManufacturing_clicked)

    def btnLinear_clicked(self):
        print("Show Linear")
        self.hide()
        self.linear = LinearWindow()
        self.linear.show()

    def btnMultiVariable_clicked(self):
        print("Show Multi-Variable")
        self.hide()
        self.multivariable = MultiVariableWindow()
        self.multivariable.show()

    def btnGA_clicked(self):
        print("Show GA")
        self.hide()
        self.ga = GAWindow()
        self.ga.show()

    def btnConstrained_clicked(self):
        print("Show Constrained")
        self.hide()
        self.constrained = ConstrainedWindow()
        self.constrained.show()

    def btnMultiObjective_clicked(self):
        print("Show Multi-Objective")
        self.hide()
        self.multiobjective = MultiObjectiveWindow()
        self.multiobjective.show()

    def btnWing_clicked(self):
        print("Show Wing")
        self.hide()
        self.wing = WingWindow()
        self.wing.show()

    def btnManufacturing_clicked(self):
        print("Show Manufacturing")
        self.hide()
        self.manufacturing = ManufacturingWindow()
        self.manufacturing.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

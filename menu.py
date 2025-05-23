# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from linear import LinearWindow

from ui_menu import Ui_wMenu

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wMenu()
        self.ui.setupUi(self)
        self.ui.btnLinear.clicked.connect(self.btnLinear_clicked)
        self.ui.btnMultivariable.clicked.connect(self.btnMultivariable_clicked)
        self.ui.btnGA.clicked.connect(self.btnGA_clicked)
        self.ui.btnConstrained.clicked.connect(self.btnConstrained_clicked)
        self.ui.btnMultiobjective.clicked.connect(self.btnMultiobjective_clicked)

    def btnLinear_clicked(self):
        print("Show Linear")
        self.hide()
        self.linear = LinearWindow()
        self.linear.show()

    def btnbtnMultivariable_clicked(self):
        print("Show Linear")
        self.hide()
        self.linear = LinearWindow()
        self.linear.show()

    def btnGA_clicked(self):
        print("Show Linear")
        self.hide()
        self.linear = LinearWindow()
        self.linear.show()

    def btnConstrained_clicked(self):
        print("Show Linear")
        self.hide()
        self.linear = LinearWindow()
        self.linear.show()

    def btnMultiobjective_clicked(self):
        print("Show Linear")
        self.hide()
        self.linear = LinearWindow()
        self.linear.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

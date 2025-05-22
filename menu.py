# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_menu import Ui_wMenu
from linear import Ui_wLinear

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wMenu()
        self.linear = Ui_wLinear()
        self.ui.setupUi(self)
        self.ui.btnShowLinear.clicked.connect(self.btnShowLinear)

    def btnShowLinear(self):
        self.linear.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())

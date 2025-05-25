# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from Optimisers.WingQuestion import WingQuestion

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_wing import Ui_wWing


class WingWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wWing()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.btnCalculate_clicked)
        self.ui.btnBack.clicked.connect(self.btnBack_clicked)
        print("Initialised")

    def btnCalculate_clicked(self):
        print("Clicked")
        ShowPlot = False
        if self.ui.cbPlot.isChecked():
            ShowPlot = True

        cl_coeff = self.ui.txtCLCoeff.text()
        cl_offset = self.ui.txtCLOff.text()
        cd_const = self.ui.txtCDConst.text()
        cd_quad = self.ui.txtCDQuad.text()
        initial_guess_alpha = self.ui.txtAlphaGuess.text()
        stall_limit = self.ui.txtStallLimit.text()
        V_cruise = self.ui.txtCruise.text()
        V_landing = self.ui.txtLanding.text()

        self.ui.txtOutput.setText(str(WingQuestion.optimise_wing(cl_coeff, cl_offset, cd_const, cd_quad, initial_guess_alpha, stall_limit, V_cruise, V_landing, ShowPlot)))

    def btnBack_clicked(self):
        from menu import MainWindow
        print("Back")
        self.hide()
        self.ui_menu = MainWindow()
        self.ui_menu.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = WingWindow()
    widget.show()
    sys.exit(app.exec())

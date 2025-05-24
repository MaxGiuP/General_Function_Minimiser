# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from Optimisers.MultiVariable import SteepestDescent
from Optimisers.MultiVariable import ConjugateGradient
from Optimisers.MultiVariable import NewtonsMethodMulti
from Optimisers.MultiVariable import BFGS
from Optimisers.MultiVariable import HookeandJeeves

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_multivariable import Ui_wMultiVariable


class MultiVariableWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wMultiVariable()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.btnCalculate_clicked)
        self.ui.btnBack.clicked.connect(self.btnBack_clicked)
        print("Initialised")

    def btnCalculate_clicked(self):
        print("Clicked")
        ShowPlot = False
        if self.ui.cbPlot.isChecked():
            ShowPlot = True

        Function = str(self.ui.txtFunction.text())
        Iterations = int(self.ui.txtIterations.text())
        x_coord = float(self.ui.txtx.text())
        y_coord = float(self.ui.txty.text())
        start = [x_coord, y_coord]
        h = float(self.ui.txth.text())

        if self.ui.rbSteepest.isChecked():
            print("Starting Steepest")
            results = SteepestDescent.steepest_descent(Function, start, Iterations, ShowPlot)
            print("Finished Steepest")
        elif self.ui.rbConjugate.isChecked():
            print("Starting Conjugate")
            results = ConjugateGradient.conjugate_gradient(Function, start, Iterations, ShowPlot)
            print("Finished Conjugate")
        elif self.ui.rbNewton.isChecked():
            print("Starting Newton's Method")
            results = NewtonsMethodMulti.newton_multivariate(Function, start, Iterations, ShowPlot)
            print("Finished Newton's Method")
        elif self.ui.rbBFGS.isChecked():
            print("Starting BFGS")
            results = BFGS.bfgs(Function, start, Iterations, ShowPlot)
            print("Finished BFGS")
        elif self.ui.rbHJ.isChecked():
            print("Starting Hooke and Jeeves")
            results = HookeandJeeves.hooke_jeeves(Function, start, h, Iterations, ShowPlot)
            print("Finished Hooke and Jeeves")

        for i in range(1, len(results)):
            self.ui.txtOutput.setText(str(self.ui.txtOutput) + str(results[i]))

    def btnBack_clicked(self):
        from menu import MainWindow
        print("Back")
        self.hide()
        self.ui_menu = MainWindow()
        self.ui_menu.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MultiVariableWindow()
    widget.show()
    sys.exit(app.exec())

# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from Optimisers.Constrained import ConstrainedLagrange
from Optimisers.Constrained import ConstrainedPenaltyFixed
from Optimisers.Constrained import ConstrainedPenaltyVaryingSL
from Optimisers.Constrained import ConstrainedPenaltyVaryingDoC
from Optimisers.Constrained import ConstrainedAugmented

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_constrained import Ui_wConstrained

class ConstrainedWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wConstrained()
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
        Equalities = str(self.ui.txtEq.text())
        Inequalities = str(self.ui.txtIneq.text())

        start = None
        R = 0.001
        method = 'BFGS'

        scale = 10
        max_round = 6
        tol = 0.000001


        if self.ui.rbLagrange.isChecked():
            print("Starting Lagrange")
            results = ConstrainedLagrange.lagrange(Function, Equalities, Inequalities, ShowPlot)
            print("End Lagrange")
        elif self.ui.rbFixedPenalty.isChecked():
            print("Starting fixed penalty")
            results = ConstrainedPenaltyFixed.fixed_penalty(Function, Equalities, Inequalities, R, start, method, ShowPlot)
            print("Finished fixed penalty")
        elif self.ui.rbVaryingSL.isChecked():
            print("Starting Varying SL")
            results = ConstrainedPenaltyVaryingSL.varying_sl(Function, Equalities, Inequalities, R, scale, max_round, tol, start, method, ShowPlot)
            print("Finished Varying SL")
        elif self.ui.rbVaryingDoC.isChecked():
            print("Starting Varying DoC")
            results = ConstrainedPenaltyVaryingDoC.varying_doc(Function, Equalities, Inequalities, R, start, method, ShowPlot)
            print("Finished Varying DoC")
        elif self.ui.rbAugmented.isChecked():
            print("Starting Augmented")
            results = ConstrainedAugmented.augmented(Function, Equalities, Inequalities, ShowPlot)
            print("Finished Augmented")

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
    widget = ConstrainedWindow()
    widget.show()
    sys.exit(app.exec())

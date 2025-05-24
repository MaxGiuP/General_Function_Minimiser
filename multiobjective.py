# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from Optimisers.MultiObjective import EigenvectorMethod
from Optimisers.MultiObjective import FuzzyLogic
from Optimisers.MultiObjective import ParetoDominance
from Optimisers.MultiObjective import ParetoDominanceTable

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_multiobjective import Ui_wMultiObjective


class MultiObjectiveWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wMultiObjective()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.btnCalculate_clicked)
        self.ui.btnBack.clicked.connect(self.btnBack_clicked)
        print("Initialised")

    def btnCalculate_clicked(self):
        print("Clicked")
        ShowPlot = False
        if self.ui.cbPlot.isChecked():
            ShowPlot = True

        Functions = str(self.ui.txtFunction.text())
        Iterations = int(self.ui.txtIterations.text())
        x_coord = float(self.ui.txtx1.text())
        y_coord = float(self.ui.txtx2.text())
        start = [x_coord, y_coord]

        thresholds = [0, 1]
        weights = 100
        samples = []
        x_values = []

        if self.ui.rbEigenvectors.isChecked():
            print("Starting eigenvectors")
            results = EigenvectorMethod.eigenvector_weights(Functions)
            print("Finished eigenvectors")
        elif self.ui.rbFuzzyLogic.isChecked():
            print("Starting fuzzy logic")
            results = FuzzyLogic.fuzzy(Functions, thresholds)
            print("Finished fuzzy logic")
        elif self.ui.rbPareto.isChecked():
            print("Starting Pareto")
            results = ParetoDominance(Functions, weights, ShowPlot)
            print("Finished Pareto")
        elif self.ui.rbParetoTable.isChecked():
            print("Starting Pareto Table")
            results = ParetoDominanceTable(samples. x_values, Functions, ShowPlot)
            print("Finished Pareto Table")

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
    widget = MultiObjectiveWindow()
    widget.show()
    sys.exit(app.exec())

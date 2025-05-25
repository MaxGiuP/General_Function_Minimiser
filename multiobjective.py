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

        Functions = str(self.ui.txtFunctions.toPlainText()).split("\n")
        print(Functions)

        x_values = []
        thresholds = []
        Left, Right = [], []

        if self.ui.txtLeft.toPlainText().strip():
            Left = self.ui.txtLeft.toPlainText().split("\n")

        if self.ui.txtRight.toPlainText().strip():
            Right = self.ui.txtRight.toPlainText().split("\n")

        if Right and Left:
            for i in range(len(Left)):
                thresholds.append((float(Left[i]), float(Right[i])))
        elif Left:
            for val in Left:
                val = val.strip()
                if val:
                    x_values.append(float(val))

        print(thresholds)

        samples = []
        for i in range (1, len(x_values) + 1):
            samples.append(i)



        if self.ui.rbEigenvectors.isChecked():
            print("Starting eigenvectors")
            result = EigenvectorMethod.eigenvector_weights(Functions)
            print("Finished eigenvectors")
        elif self.ui.rbFuzzyLogic.isChecked():
            print("Starting fuzzy logic")
            result = FuzzyLogic.fuzzy(Functions, thresholds)
            print("Finished fuzzy logic")
        elif self.ui.rbPareto.isChecked():
            print("Starting Pareto")
            result = ParetoDominance.pareto_front(Functions, ShowPlot)
            print("Finished Pareto")
        elif self.ui.rbParetoTable.isChecked():
            print("Starting Pareto Table")
            result = ParetoDominanceTable.pareto_analysis(Functions, x_values, samples, ShowPlot)
            print("Finished Pareto Table")

        self.ui.txtOutput.setText(str(result))

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

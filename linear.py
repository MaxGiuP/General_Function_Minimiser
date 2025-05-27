# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from Optimisers.LinearSearch import GoldenSection
from Optimisers.LinearSearch import InverseParabolicInterpolation
from Optimisers.LinearSearch import NewtonsMethodLinear

from Optimsers.LinearSearch import PlotLinear

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_linear import Ui_wLinear

class LinearWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wLinear()
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
        x1 = float(self.ui.txtx1.text())
        x2 = float(self.ui.txtx2.text())
        x3 = float(self.ui.txtx3.text())

        if self.ui.rbGolden.isChecked():
            print("Starting Golden Section")
            result = GoldenSection.golden_section_search(Function, x1, x2, x3, Iterations, ShowPlot)
            print("Finished Golden Section")
        elif self.ui.rbInverse.isChecked():
            print("Starting Inverse Parabolic")
            result = InverseParabolicInterpolation.inverse_parabolic_interpolation(Function, x1, x2, x3, Iterations, ShowPlot)
            print("Finished Inverse Parabolic")
        elif self.ui.rbNewton.isChecked():
            print("Starting Newton's Method")
            result = NewtonsMethodLinear.newtons_method(Function, x1, Iterations, ShowPlot)
            print("Finished Newton's Method")

        self.ui.txtOutput.setText(result)


    def btnBack_clicked(self):
        from menu import MainWindow
        print("Back")
        self.hide()
        self.ui_menu = MainWindow()
        self.ui_menu.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LinearWindow()
    widget.show()
    sys.exit(app.exec())

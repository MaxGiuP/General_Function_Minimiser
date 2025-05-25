# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from Optimisers.GeneticAlgorithms import GA_Combined

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_ga import Ui_wGA

class GAWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_wGA()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.btnCalculate_clicked)
        self.ui.btnSelection.clicked.connect(self.btnSelection_clicked)
        self.ui.btnReproduction.clicked.connect(self.btnReproduction_clicked)

        self.ui.btnBack.clicked.connect(self.btnBack_clicked)
        print("Initialised")

    def btnCalculate_clicked(self):
        print("Clicked")

        form = self.ui

        fitness_fn = form.txtFunction.text()
        lower = float(form.txtLow.text())
        upper = float(form.txtUp.text())
        bits = int(form.txtBits.text())
        pop_size = int(form.txtPop.text())
        generations = int(form.txtGens.text())
        crossover_rate = float(form.txtCross.text())
        mutation_rate = float(form.txtMut.text())
        order = form.cmbOrder.currentText()
        method = form.cmbMethod.currentText()
        rank_power = float(form.txtRank.text())

        ga = GA_Combined.GeneticAlgorithm(
            fitness_fn    = fitness_fn,
            lower         = lower,
            upper         = upper,
            bits          = bits,
            pop_size      = pop_size,
            generations   = generations,
            select_params = {"method": method,"order": order,"rank_power": rank_power},
            crossover_rate= crossover_rate,
            mutation_rate = mutation_rate,
            rng           = None #np.random.default_rng()
        )

        x, f = ga.run()
        results = "Best x value is : " + str(x) + "\nBest f value is: " + str(f)
        form.txtOutput.setText(results)


    def btnSelection_clicked(self):
        form = self.ui

        values = [float(x) for x in form.txtValues.text().strip().split(",")]
        fitness = [float(x) for x in form.txtFitness.text().strip().split(",")]
        rands = [float(x) for x in form.txtRands.text().strip().split(",")]
        order = form.cmbSelOrder.currentText()
        method = form.cmbMethod.currentText()
        rank_power = float(form.txtSelRank.text())
        if form.cmbSelRep.currentText() == "Yes":
            replacement = True
        else: replacement = False

        idxs = GA_Combined.roulette_selection_indices(
            fitness    = fitness,
            num_select = len(values),
            method     = method,
            order      = order,
            rank_power = rank_power,
            replacement= replacement,
            rands      = rands
        )
        pool = [values[i] for i in idxs]
        form.txtSelection.setText("Roulette Pool: " + str(pool))

    def btnReproduction_clicked(self):
        form = self.ui

        lower = float(form.txtRepLow.text())
        upper = float(form.txtRepUp.text())
        bits = int(form.txtBits.text())
        crossover_point = int(float(form.txtRepCross.text()) * (bits - 1)) + 1

        if form.txtRepMut1.text() != "" and form.txtRepMut2.text() != "":
            mutation_positions = [int(float(form.txtRepMut1.text())*bits), int(float(form.txtRepMut2.text())*bits)]
        else: mutation_positions = []

        parents = [float(form.txtParent1.text()), float(form.txtParent2.text())]

        c1, c2 = GA_Combined.reproduce_parametric(
            parents            = parents,
            lower              = lower,
            upper              = upper,
            bits               = bits,
            crossover_point    = crossover_point,
            mutation_positions = mutation_positions
        )
        form.txtReproduction.setText("Children: \nLeft + Right:" + str(round(c1,5)) + " \nRight + Left" + str(round(c2,5)))

    def btnBack_clicked(self):
        from menu import MainWindow
        print("Back")
        self.hide()
        self.ui_menu = MainWindow()
        self.ui_menu.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = GAWindow()
    widget.show()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ga.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_wGA(object):
    def setupUi(self, wGA):
        if not wGA.objectName():
            wGA.setObjectName(u"wGA")
        wGA.resize(938, 552)
        self.centralwidget = QWidget(wGA)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txtOutput = QTextEdit(self.centralwidget)
        self.txtOutput.setObjectName(u"txtOutput")
        self.txtOutput.setGeometry(QRect(10, 410, 301, 81))
        self.btnCalculate = QPushButton(self.centralwidget)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(150, 360, 151, 41))
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(20, 370, 97, 26))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(580, 0, 291, 188))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 1, 0, 1, 1)

        self.txtRepMut2 = QLineEdit(self.gridLayoutWidget)
        self.txtRepMut2.setObjectName(u"txtRepMut2")

        self.gridLayout.addWidget(self.txtRepMut2, 5, 2, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)

        self.txtParent2 = QLineEdit(self.gridLayoutWidget)
        self.txtParent2.setObjectName(u"txtParent2")

        self.gridLayout.addWidget(self.txtParent2, 3, 2, 1, 1)

        self.txtParent1 = QLineEdit(self.gridLayoutWidget)
        self.txtParent1.setObjectName(u"txtParent1")

        self.gridLayout.addWidget(self.txtParent1, 3, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 2, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.txtRepMut1 = QLineEdit(self.gridLayoutWidget)
        self.txtRepMut1.setObjectName(u"txtRepMut1")

        self.gridLayout.addWidget(self.txtRepMut1, 5, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 0, 0, 1, 1)

        self.txtRepLow = QLineEdit(self.gridLayoutWidget)
        self.txtRepLow.setObjectName(u"txtRepLow")

        self.gridLayout.addWidget(self.txtRepLow, 0, 1, 1, 2)

        self.txtRepUp = QLineEdit(self.gridLayoutWidget)
        self.txtRepUp.setObjectName(u"txtRepUp")

        self.gridLayout.addWidget(self.txtRepUp, 1, 1, 1, 2)

        self.txtRepBits = QLineEdit(self.gridLayoutWidget)
        self.txtRepBits.setObjectName(u"txtRepBits")

        self.gridLayout.addWidget(self.txtRepBits, 2, 1, 1, 2)

        self.txtRepCross = QLineEdit(self.gridLayoutWidget)
        self.txtRepCross.setObjectName(u"txtRepCross")

        self.gridLayout.addWidget(self.txtRepCross, 4, 1, 1, 2)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 0, 301, 351))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.txtUp = QLineEdit(self.gridLayoutWidget_2)
        self.txtUp.setObjectName(u"txtUp")

        self.gridLayout_2.addWidget(self.txtUp, 2, 1, 1, 1)

        self.txtFunction = QLineEdit(self.gridLayoutWidget_2)
        self.txtFunction.setObjectName(u"txtFunction")

        self.gridLayout_2.addWidget(self.txtFunction, 0, 1, 1, 1)

        self.cmbOrder = QComboBox(self.gridLayoutWidget_2)
        self.cmbOrder.addItem("")
        self.cmbOrder.addItem("")
        self.cmbOrder.setObjectName(u"cmbOrder")

        self.gridLayout_2.addWidget(self.cmbOrder, 8, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 6, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.txtRank = QLineEdit(self.gridLayoutWidget_2)
        self.txtRank.setObjectName(u"txtRank")

        self.gridLayout_2.addWidget(self.txtRank, 10, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 8, 0, 1, 1)

        self.txtMut = QLineEdit(self.gridLayoutWidget_2)
        self.txtMut.setObjectName(u"txtMut")

        self.gridLayout_2.addWidget(self.txtMut, 7, 1, 1, 1)

        self.txtBits = QLineEdit(self.gridLayoutWidget_2)
        self.txtBits.setObjectName(u"txtBits")

        self.gridLayout_2.addWidget(self.txtBits, 3, 1, 1, 1)

        self.txtGens = QLineEdit(self.gridLayoutWidget_2)
        self.txtGens.setObjectName(u"txtGens")

        self.gridLayout_2.addWidget(self.txtGens, 5, 1, 1, 1)

        self.txtPop = QLineEdit(self.gridLayoutWidget_2)
        self.txtPop.setObjectName(u"txtPop")

        self.gridLayout_2.addWidget(self.txtPop, 4, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 7, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.txtCross = QLineEdit(self.gridLayoutWidget_2)
        self.txtCross.setObjectName(u"txtCross")

        self.gridLayout_2.addWidget(self.txtCross, 6, 1, 1, 1)

        self.txtLow = QLineEdit(self.gridLayoutWidget_2)
        self.txtLow.setObjectName(u"txtLow")

        self.gridLayout_2.addWidget(self.txtLow, 1, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_2.addWidget(self.label_12, 9, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 10, 0, 1, 1)

        self.cmbMethod = QComboBox(self.gridLayoutWidget_2)
        self.cmbMethod.addItem("")
        self.cmbMethod.addItem("")
        self.cmbMethod.setObjectName(u"cmbMethod")

        self.gridLayout_2.addWidget(self.cmbMethod, 9, 1, 1, 1)

        self.btnSelection = QPushButton(self.centralwidget)
        self.btnSelection.setObjectName(u"btnSelection")
        self.btnSelection.setGeometry(QRect(370, 240, 151, 41))
        self.txtSelection = QTextEdit(self.centralwidget)
        self.txtSelection.setObjectName(u"txtSelection")
        self.txtSelection.setGeometry(QRect(350, 290, 201, 81))
        self.gridLayoutWidget_4 = QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(340, 0, 233, 220))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.gridLayoutWidget_4)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_4.addWidget(self.label_21, 2, 0, 1, 1)

        self.txtValues = QLineEdit(self.gridLayoutWidget_4)
        self.txtValues.setObjectName(u"txtValues")

        self.gridLayout_4.addWidget(self.txtValues, 0, 1, 1, 1)

        self.cmbSelOrder = QComboBox(self.gridLayoutWidget_4)
        self.cmbSelOrder.addItem("")
        self.cmbSelOrder.addItem("")
        self.cmbSelOrder.setObjectName(u"cmbSelOrder")

        self.gridLayout_4.addWidget(self.cmbSelOrder, 3, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_4)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_4)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_4.addWidget(self.label_27, 5, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_4)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 4, 0, 1, 1)

        self.txtFitness = QLineEdit(self.gridLayoutWidget_4)
        self.txtFitness.setObjectName(u"txtFitness")

        self.gridLayout_4.addWidget(self.txtFitness, 1, 1, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_4)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_4.addWidget(self.label_26, 3, 0, 1, 1)

        self.txtSelRank = QLineEdit(self.gridLayoutWidget_4)
        self.txtSelRank.setObjectName(u"txtSelRank")

        self.gridLayout_4.addWidget(self.txtSelRank, 5, 1, 1, 1)

        self.cmbSelMethod = QComboBox(self.gridLayoutWidget_4)
        self.cmbSelMethod.addItem("")
        self.cmbSelMethod.addItem("")
        self.cmbSelMethod.setObjectName(u"cmbSelMethod")

        self.gridLayout_4.addWidget(self.cmbSelMethod, 4, 1, 1, 1)

        self.txtRands = QLineEdit(self.gridLayoutWidget_4)
        self.txtRands.setObjectName(u"txtRands")

        self.gridLayout_4.addWidget(self.txtRands, 2, 1, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_4)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_4.addWidget(self.label_28, 6, 0, 1, 1)

        self.cmbSelRep = QComboBox(self.gridLayoutWidget_4)
        self.cmbSelRep.addItem("")
        self.cmbSelRep.addItem("")
        self.cmbSelRep.setObjectName(u"cmbSelRep")

        self.gridLayout_4.addWidget(self.cmbSelRep, 6, 1, 1, 1)

        self.btnReproduction = QPushButton(self.centralwidget)
        self.btnReproduction.setObjectName(u"btnReproduction")
        self.btnReproduction.setGeometry(QRect(580, 200, 151, 41))
        self.txtReproduction = QTextEdit(self.centralwidget)
        self.txtReproduction.setObjectName(u"txtReproduction")
        self.txtReproduction.setGeometry(QRect(610, 260, 201, 81))
        self.cbIsBit = QCheckBox(self.centralwidget)
        self.cbIsBit.setObjectName(u"cbIsBit")
        self.cbIsBit.setGeometry(QRect(750, 210, 121, 24))
        wGA.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wGA)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 938, 23))
        wGA.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wGA)
        self.statusbar.setObjectName(u"statusbar")
        wGA.setStatusBar(self.statusbar)

        self.retranslateUi(wGA)

        QMetaObject.connectSlotsByName(wGA)
    # setupUi

    def retranslateUi(self, wGA):
        wGA.setWindowTitle(QCoreApplication.translate("wGA", u"Genetic Algorithms", None))
        self.btnCalculate.setText(QCoreApplication.translate("wGA", u"Run GA", None))
        self.btnBack.setText(QCoreApplication.translate("wGA", u"Back", None))
        self.label_24.setText(QCoreApplication.translate("wGA", u"Upper Bound", None))
        self.txtRepMut2.setText(QCoreApplication.translate("wGA", u"0.8425", None))
        self.label_14.setText(QCoreApplication.translate("wGA", u"Mutation Position", None))
        self.txtParent2.setText(QCoreApplication.translate("wGA", u"0.04762", None))
        self.txtParent1.setText(QCoreApplication.translate("wGA", u"-0.42857", None))
        self.label_2.setText(QCoreApplication.translate("wGA", u"Crossover Point", None))
        self.label_22.setText(QCoreApplication.translate("wGA", u"Number of Bits", None))
        self.label.setText(QCoreApplication.translate("wGA", u"Parents", None))
        self.txtRepMut1.setText(QCoreApplication.translate("wGA", u"0.1397", None))
        self.label_23.setText(QCoreApplication.translate("wGA", u"Lower Bound", None))
        self.txtRepLow.setText(QCoreApplication.translate("wGA", u"-1", None))
        self.txtRepUp.setText(QCoreApplication.translate("wGA", u"1", None))
        self.txtRepBits.setText(QCoreApplication.translate("wGA", u"6", None))
        self.txtRepCross.setText(QCoreApplication.translate("wGA", u"0.3772", None))
        self.label_4.setText(QCoreApplication.translate("wGA", u"Lower Bound", None))
        self.txtUp.setText(QCoreApplication.translate("wGA", u"1", None))
        self.txtFunction.setText(QCoreApplication.translate("wGA", u"-(x-0.3)**2 + 1", None))
        self.cmbOrder.setItemText(0, QCoreApplication.translate("wGA", u"Ascending", None))
        self.cmbOrder.setItemText(1, QCoreApplication.translate("wGA", u"Descending", None))

        self.label_8.setText(QCoreApplication.translate("wGA", u"Population Size", None))
        self.label_10.setText(QCoreApplication.translate("wGA", u"Crossover Rate", None))
        self.label_9.setText(QCoreApplication.translate("wGA", u"Generations", None))
        self.label_5.setText(QCoreApplication.translate("wGA", u"Upper Bound", None))
        self.txtRank.setText(QCoreApplication.translate("wGA", u"1.0", None))
        self.label_6.setText(QCoreApplication.translate("wGA", u"Order", None))
        self.txtMut.setText(QCoreApplication.translate("wGA", u"0.2", None))
        self.txtBits.setText(QCoreApplication.translate("wGA", u"6", None))
        self.txtGens.setText(QCoreApplication.translate("wGA", u"20", None))
        self.txtPop.setText(QCoreApplication.translate("wGA", u"10", None))
        self.label_7.setText(QCoreApplication.translate("wGA", u"Number of Bits", None))
        self.label_11.setText(QCoreApplication.translate("wGA", u"Mutation Rate", None))
        self.label_3.setText(QCoreApplication.translate("wGA", u"Fitness Function", None))
        self.txtCross.setText(QCoreApplication.translate("wGA", u"0.8", None))
        self.txtLow.setText(QCoreApplication.translate("wGA", u"-1", None))
        self.label_12.setText(QCoreApplication.translate("wGA", u"Method", None))
        self.label_13.setText(QCoreApplication.translate("wGA", u"Rank Power", None))
        self.cmbMethod.setItemText(0, QCoreApplication.translate("wGA", u"Rank based", None))
        self.cmbMethod.setItemText(1, QCoreApplication.translate("wGA", u"Fitness based", None))

        self.btnSelection.setText(QCoreApplication.translate("wGA", u"Test Selection", None))
        self.label_21.setText(QCoreApplication.translate("wGA", u"Rands", None))
        self.txtValues.setText(QCoreApplication.translate("wGA", u"1, 3, 6, 7, 11", None))
        self.cmbSelOrder.setItemText(0, QCoreApplication.translate("wGA", u"Ascending", None))
        self.cmbSelOrder.setItemText(1, QCoreApplication.translate("wGA", u"Descending", None))

        self.label_20.setText(QCoreApplication.translate("wGA", u"Fitness", None))
        self.label_27.setText(QCoreApplication.translate("wGA", u"Rank Power", None))
        self.label_25.setText(QCoreApplication.translate("wGA", u"Method", None))
        self.txtFitness.setText(QCoreApplication.translate("wGA", u"0.1, 0.55, 0.4, 0.2, 0.15", None))
        self.label_19.setText(QCoreApplication.translate("wGA", u"Values", None))
        self.label_26.setText(QCoreApplication.translate("wGA", u"Order", None))
        self.txtSelRank.setText(QCoreApplication.translate("wGA", u"1.0", None))
        self.cmbSelMethod.setItemText(0, QCoreApplication.translate("wGA", u"Rank based", None))
        self.cmbSelMethod.setItemText(1, QCoreApplication.translate("wGA", u"Fitness based", None))

        self.txtRands.setText(QCoreApplication.translate("wGA", u"0.0975, 0.2785, 0.5469, 0.9575, 0.9649", None))
        self.label_28.setText(QCoreApplication.translate("wGA", u"Replacement", None))
        self.cmbSelRep.setItemText(0, QCoreApplication.translate("wGA", u"Yes", None))
        self.cmbSelRep.setItemText(1, QCoreApplication.translate("wGA", u"No", None))

        self.btnReproduction.setText(QCoreApplication.translate("wGA", u"Test Reproduction", None))
        self.cbIsBit.setText(QCoreApplication.translate("wGA", u"Enter as Bits?", None))
    # retranslateUi


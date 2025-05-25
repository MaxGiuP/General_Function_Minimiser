# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multiobjective.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_wMultiObjective(object):
    def setupUi(self, wMultiObjective):
        if not wMultiObjective.objectName():
            wMultiObjective.setObjectName(u"wMultiObjective")
        wMultiObjective.resize(635, 542)
        self.centralwidget = QWidget(wMultiObjective)
        self.centralwidget.setObjectName(u"centralwidget")
        self.txtOutput = QTextEdit(self.centralwidget)
        self.txtOutput.setObjectName(u"txtOutput")
        self.txtOutput.setGeometry(QRect(220, 170, 371, 181))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 170, 201, 116))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rbEigenvectors = QRadioButton(self.verticalLayoutWidget)
        self.rbEigenvectors.setObjectName(u"rbEigenvectors")
        self.rbEigenvectors.setChecked(True)

        self.verticalLayout.addWidget(self.rbEigenvectors)

        self.rbFuzzyLogic = QRadioButton(self.verticalLayoutWidget)
        self.rbFuzzyLogic.setObjectName(u"rbFuzzyLogic")

        self.verticalLayout.addWidget(self.rbFuzzyLogic)

        self.rbPareto = QRadioButton(self.verticalLayoutWidget)
        self.rbPareto.setObjectName(u"rbPareto")

        self.verticalLayout.addWidget(self.rbPareto)

        self.rbParetoTable = QRadioButton(self.verticalLayoutWidget)
        self.rbParetoTable.setObjectName(u"rbParetoTable")

        self.verticalLayout.addWidget(self.rbParetoTable)

        self.btnCalculate = QPushButton(self.centralwidget)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(310, 380, 151, 41))
        self.cbPlot = QCheckBox(self.centralwidget)
        self.cbPlot.setObjectName(u"cbPlot")
        self.cbPlot.setGeometry(QRect(30, 310, 121, 24))
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(70, 390, 97, 26))
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 311, 141))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.txtFunctions = QTextEdit(self.formLayoutWidget)
        self.txtFunctions.setObjectName(u"txtFunctions")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.txtFunctions)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.SpanningRole, self.label)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(340, 10, 160, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txtRight = QTextEdit(self.gridLayoutWidget)
        self.txtRight.setObjectName(u"txtRight")

        self.gridLayout.addWidget(self.txtRight, 1, 1, 1, 1)

        self.txtLeft = QTextEdit(self.gridLayoutWidget)
        self.txtLeft.setObjectName(u"txtLeft")

        self.gridLayout.addWidget(self.txtLeft, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        wMultiObjective.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wMultiObjective)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 635, 23))
        wMultiObjective.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wMultiObjective)
        self.statusbar.setObjectName(u"statusbar")
        wMultiObjective.setStatusBar(self.statusbar)

        self.retranslateUi(wMultiObjective)

        QMetaObject.connectSlotsByName(wMultiObjective)
    # setupUi

    def retranslateUi(self, wMultiObjective):
        wMultiObjective.setWindowTitle(QCoreApplication.translate("wMultiObjective", u"MainWindow", None))
        self.rbEigenvectors.setText(QCoreApplication.translate("wMultiObjective", u"Eigenvectors", None))
        self.rbFuzzyLogic.setText(QCoreApplication.translate("wMultiObjective", u"Fuzzy Logic", None))
        self.rbPareto.setText(QCoreApplication.translate("wMultiObjective", u"Pareto Dominance", None))
        self.rbParetoTable.setText(QCoreApplication.translate("wMultiObjective", u"Pareto Dominance Table", None))
        self.btnCalculate.setText(QCoreApplication.translate("wMultiObjective", u"Calculate", None))
        self.cbPlot.setText(QCoreApplication.translate("wMultiObjective", u"Plot function", None))
        self.btnBack.setText(QCoreApplication.translate("wMultiObjective", u"Back", None))
        self.label.setText(QCoreApplication.translate("wMultiObjective", u"Functions", None))
        self.label_2.setText(QCoreApplication.translate("wMultiObjective", u"Min", None))
        self.label_3.setText(QCoreApplication.translate("wMultiObjective", u"Max", None))
    # retranslateUi


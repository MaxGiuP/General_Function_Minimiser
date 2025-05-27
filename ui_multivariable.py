# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'multivariable.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_wMultiVariable(object):
    def setupUi(self, wMultiVariable):
        if not wMultiVariable.objectName():
            wMultiVariable.setObjectName(u"wMultiVariable")
        wMultiVariable.resize(800, 600)
        self.centralwidget = QWidget(wMultiVariable)
        self.centralwidget.setObjectName(u"centralwidget")
        self.cbPlot = QCheckBox(self.centralwidget)
        self.cbPlot.setObjectName(u"cbPlot")
        self.cbPlot.setGeometry(QRect(470, 10, 121, 24))
        self.txtOutput = QTextEdit(self.centralwidget)
        self.txtOutput.setObjectName(u"txtOutput")
        self.txtOutput.setGeometry(QRect(180, 120, 371, 141))
        self.btnCalculate = QPushButton(self.centralwidget)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(320, 280, 151, 41))
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(170, 280, 97, 26))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 451, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txtx = QLineEdit(self.gridLayoutWidget)
        self.txtx.setObjectName(u"txtx")

        self.gridLayout.addWidget(self.txtx, 1, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 5, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)

        self.txtFunction = QLineEdit(self.gridLayoutWidget)
        self.txtFunction.setObjectName(u"txtFunction")

        self.gridLayout.addWidget(self.txtFunction, 0, 2, 1, 5)

        self.txth = QLineEdit(self.gridLayoutWidget)
        self.txth.setObjectName(u"txth")

        self.gridLayout.addWidget(self.txth, 1, 6, 1, 1)

        self.txty = QLineEdit(self.gridLayoutWidget)
        self.txty.setObjectName(u"txty")

        self.gridLayout.addWidget(self.txty, 1, 4, 1, 1)

        self.txtIterations = QLineEdit(self.gridLayoutWidget)
        self.txtIterations.setObjectName(u"txtIterations")

        self.gridLayout.addWidget(self.txtIterations, 2, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 120, 171, 146))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rbSteepest = QRadioButton(self.verticalLayoutWidget)
        self.rbSteepest.setObjectName(u"rbSteepest")
        self.rbSteepest.setChecked(True)

        self.verticalLayout.addWidget(self.rbSteepest)

        self.rbConjugate = QRadioButton(self.verticalLayoutWidget)
        self.rbConjugate.setObjectName(u"rbConjugate")

        self.verticalLayout.addWidget(self.rbConjugate)

        self.rbNewton = QRadioButton(self.verticalLayoutWidget)
        self.rbNewton.setObjectName(u"rbNewton")

        self.verticalLayout.addWidget(self.rbNewton)

        self.rbBFGS = QRadioButton(self.verticalLayoutWidget)
        self.rbBFGS.setObjectName(u"rbBFGS")

        self.verticalLayout.addWidget(self.rbBFGS)

        self.rbHJ = QRadioButton(self.verticalLayoutWidget)
        self.rbHJ.setObjectName(u"rbHJ")

        self.verticalLayout.addWidget(self.rbHJ)

        wMultiVariable.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wMultiVariable)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        wMultiVariable.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wMultiVariable)
        self.statusbar.setObjectName(u"statusbar")
        wMultiVariable.setStatusBar(self.statusbar)

        self.retranslateUi(wMultiVariable)

        QMetaObject.connectSlotsByName(wMultiVariable)
    # setupUi

    def retranslateUi(self, wMultiVariable):
        wMultiVariable.setWindowTitle(QCoreApplication.translate("wMultiVariable", u"Multi Variable Search", None))
        self.cbPlot.setText(QCoreApplication.translate("wMultiVariable", u"Plot function", None))
        self.btnCalculate.setText(QCoreApplication.translate("wMultiVariable", u"Calculate", None))
        self.btnBack.setText(QCoreApplication.translate("wMultiVariable", u"Back", None))
        self.txtx.setText(QCoreApplication.translate("wMultiVariable", u"0", None))
        self.label_2.setText(QCoreApplication.translate("wMultiVariable", u"Starting Points", None))
        self.label_5.setText(QCoreApplication.translate("wMultiVariable", u"h", None))
        self.label_4.setText(QCoreApplication.translate("wMultiVariable", u"y", None))
        self.txtFunction.setText(QCoreApplication.translate("wMultiVariable", u"x1 - x2 + 2*(x1**2) + 2*x1*x2 + x2**3", None))
        self.txth.setText(QCoreApplication.translate("wMultiVariable", u"2", None))
        self.txty.setText(QCoreApplication.translate("wMultiVariable", u"1", None))
        self.txtIterations.setText(QCoreApplication.translate("wMultiVariable", u"2", None))
        self.label_6.setText(QCoreApplication.translate("wMultiVariable", u"x", None))
        self.label.setText(QCoreApplication.translate("wMultiVariable", u"Function", None))
        self.label_3.setText(QCoreApplication.translate("wMultiVariable", u"Number of Iterations", None))
        self.rbSteepest.setText(QCoreApplication.translate("wMultiVariable", u"Steepest Descent", None))
        self.rbConjugate.setText(QCoreApplication.translate("wMultiVariable", u"Conjugate Gradient", None))
        self.rbNewton.setText(QCoreApplication.translate("wMultiVariable", u"Netwon's Method", None))
        self.rbBFGS.setText(QCoreApplication.translate("wMultiVariable", u"BFGS", None))
        self.rbHJ.setText(QCoreApplication.translate("wMultiVariable", u"Hooke and Jeeves", None))
    # retranslateUi


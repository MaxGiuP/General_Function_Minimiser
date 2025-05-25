# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'constrained.ui'
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

class Ui_wConstrained(object):
    def setupUi(self, wConstrained):
        if not wConstrained.objectName():
            wConstrained.setObjectName(u"wConstrained")
        wConstrained.resize(611, 459)
        self.centralwidget = QWidget(wConstrained)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 471, 180))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txtFunction = QLineEdit(self.gridLayoutWidget)
        self.txtFunction.setObjectName(u"txtFunction")

        self.gridLayout.addWidget(self.txtFunction, 0, 1, 1, 2)

        self.txtEq = QTextEdit(self.gridLayoutWidget)
        self.txtEq.setObjectName(u"txtEq")

        self.gridLayout.addWidget(self.txtEq, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.txtIneq = QTextEdit(self.gridLayoutWidget)
        self.txtIneq.setObjectName(u"txtIneq")

        self.gridLayout.addWidget(self.txtIneq, 2, 1, 1, 1)

        self.txtOutput = QTextEdit(self.centralwidget)
        self.txtOutput.setObjectName(u"txtOutput")
        self.txtOutput.setGeometry(QRect(210, 240, 281, 141))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 190, 181, 146))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rbLagrange = QRadioButton(self.verticalLayoutWidget)
        self.rbLagrange.setObjectName(u"rbLagrange")
        self.rbLagrange.setChecked(True)

        self.verticalLayout.addWidget(self.rbLagrange)

        self.rbFixedPenalty = QRadioButton(self.verticalLayoutWidget)
        self.rbFixedPenalty.setObjectName(u"rbFixedPenalty")

        self.verticalLayout.addWidget(self.rbFixedPenalty)

        self.rbVaryingDoC = QRadioButton(self.verticalLayoutWidget)
        self.rbVaryingDoC.setObjectName(u"rbVaryingDoC")

        self.verticalLayout.addWidget(self.rbVaryingDoC)

        self.rbVaryingSL = QRadioButton(self.verticalLayoutWidget)
        self.rbVaryingSL.setObjectName(u"rbVaryingSL")

        self.verticalLayout.addWidget(self.rbVaryingSL)

        self.rbAugmented = QRadioButton(self.verticalLayoutWidget)
        self.rbAugmented.setObjectName(u"rbAugmented")

        self.verticalLayout.addWidget(self.rbAugmented)

        self.btnCalculate = QPushButton(self.centralwidget)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(270, 190, 151, 41))
        self.cbPlot = QCheckBox(self.centralwidget)
        self.cbPlot.setObjectName(u"cbPlot")
        self.cbPlot.setGeometry(QRect(490, 10, 121, 24))
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(10, 380, 97, 26))
        wConstrained.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wConstrained)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 611, 23))
        wConstrained.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wConstrained)
        self.statusbar.setObjectName(u"statusbar")
        wConstrained.setStatusBar(self.statusbar)

        self.retranslateUi(wConstrained)

        QMetaObject.connectSlotsByName(wConstrained)
    # setupUi

    def retranslateUi(self, wConstrained):
        wConstrained.setWindowTitle(QCoreApplication.translate("wConstrained", u"ConstrainedWindow", None))
        self.txtFunction.setText(QCoreApplication.translate("wConstrained", u"5 / (x1*(x2**2))", None))
        self.txtEq.setDocumentTitle("")
        self.txtEq.setPlaceholderText(QCoreApplication.translate("wConstrained", u"x1**2 + x2**2 - 4", None))
        self.label_2.setText(QCoreApplication.translate("wConstrained", u"Equality Constraints", None))
        self.label.setText(QCoreApplication.translate("wConstrained", u"Function", None))
        self.label_3.setText(QCoreApplication.translate("wConstrained", u"Inequality Constraints", None))
        self.rbLagrange.setText(QCoreApplication.translate("wConstrained", u"Lagrange Multipliers", None))
        self.rbFixedPenalty.setText(QCoreApplication.translate("wConstrained", u"Fixed Penalty", None))
        self.rbVaryingDoC.setText(QCoreApplication.translate("wConstrained", u"Varying DoC", None))
        self.rbVaryingSL.setText(QCoreApplication.translate("wConstrained", u"Varying SL", None))
        self.rbAugmented.setText(QCoreApplication.translate("wConstrained", u"Augmented Lagrange", None))
        self.btnCalculate.setText(QCoreApplication.translate("wConstrained", u"Calculate", None))
        self.cbPlot.setText(QCoreApplication.translate("wConstrained", u"Plot function", None))
        self.btnBack.setText(QCoreApplication.translate("wConstrained", u"Back", None))
    # retranslateUi


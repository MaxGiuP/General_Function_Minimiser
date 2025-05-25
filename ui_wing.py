# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wing.ui'
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
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_wWing(object):
    def setupUi(self, wWing):
        if not wWing.objectName():
            wWing.setObjectName(u"wWing")
        wWing.resize(800, 496)
        self.centralwidget = QWidget(wWing)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnCalculate = QPushButton(self.centralwidget)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(170, 260, 151, 41))
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(30, 270, 97, 26))
        self.txtOutput = QTextEdit(self.centralwidget)
        self.txtOutput.setObjectName(u"txtOutput")
        self.txtOutput.setGeometry(QRect(10, 310, 371, 141))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 451, 252))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txtCLCoeff = QLineEdit(self.gridLayoutWidget)
        self.txtCLCoeff.setObjectName(u"txtCLCoeff")

        self.gridLayout.addWidget(self.txtCLCoeff, 0, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.txtAlphaGuess = QLineEdit(self.gridLayoutWidget)
        self.txtAlphaGuess.setObjectName(u"txtAlphaGuess")

        self.gridLayout.addWidget(self.txtAlphaGuess, 4, 1, 1, 1)

        self.txtCDConst = QLineEdit(self.gridLayoutWidget)
        self.txtCDConst.setObjectName(u"txtCDConst")

        self.gridLayout.addWidget(self.txtCDConst, 2, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.txtCLOff = QLineEdit(self.gridLayoutWidget)
        self.txtCLOff.setObjectName(u"txtCLOff")

        self.gridLayout.addWidget(self.txtCLOff, 1, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.txtCDQuad = QLineEdit(self.gridLayoutWidget)
        self.txtCDQuad.setObjectName(u"txtCDQuad")

        self.gridLayout.addWidget(self.txtCDQuad, 3, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.txtStallLimit = QLineEdit(self.gridLayoutWidget)
        self.txtStallLimit.setObjectName(u"txtStallLimit")

        self.gridLayout.addWidget(self.txtStallLimit, 5, 1, 1, 1)

        self.txtCruise = QLineEdit(self.gridLayoutWidget)
        self.txtCruise.setObjectName(u"txtCruise")

        self.gridLayout.addWidget(self.txtCruise, 6, 1, 1, 1)

        self.txtLanding = QLineEdit(self.gridLayoutWidget)
        self.txtLanding.setObjectName(u"txtLanding")

        self.gridLayout.addWidget(self.txtLanding, 7, 1, 1, 1)

        self.cbPlot = QCheckBox(self.centralwidget)
        self.cbPlot.setObjectName(u"cbPlot")
        self.cbPlot.setGeometry(QRect(350, 270, 97, 24))
        wWing.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wWing)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        wWing.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wWing)
        self.statusbar.setObjectName(u"statusbar")
        wWing.setStatusBar(self.statusbar)

        self.retranslateUi(wWing)

        QMetaObject.connectSlotsByName(wWing)
    # setupUi

    def retranslateUi(self, wWing):
        wWing.setWindowTitle(QCoreApplication.translate("wWing", u"Wing Question", None))
        self.btnCalculate.setText(QCoreApplication.translate("wWing", u"Calculate", None))
        self.btnBack.setText(QCoreApplication.translate("wWing", u"Back", None))
        self.txtCLCoeff.setText(QCoreApplication.translate("wWing", u"0.093", None))
        self.label_6.setText(QCoreApplication.translate("wWing", u"Stall Limit", None))
        self.label_2.setText(QCoreApplication.translate("wWing", u"CL Offset", None))
        self.txtAlphaGuess.setText(QCoreApplication.translate("wWing", u"5", None))
        self.txtCDConst.setText(QCoreApplication.translate("wWing", u"0.032", None))
        self.label_4.setText(QCoreApplication.translate("wWing", u"CD Constant", None))
        self.label_5.setText(QCoreApplication.translate("wWing", u"CD Quadratic", None))
        self.txtCLOff.setText(QCoreApplication.translate("wWing", u"1", None))
        self.label.setText(QCoreApplication.translate("wWing", u"CL Coefficient", None))
        self.label_7.setText(QCoreApplication.translate("wWing", u"Cruise Speed", None))
        self.label_3.setText(QCoreApplication.translate("wWing", u"Alpha Guess", None))
        self.txtCDQuad.setText(QCoreApplication.translate("wWing", u"0.055", None))
        self.label_8.setText(QCoreApplication.translate("wWing", u"Landing Speed", None))
        self.txtStallLimit.setText(QCoreApplication.translate("wWing", u"14", None))
        self.txtCruise.setText(QCoreApplication.translate("wWing", u"40", None))
        self.txtLanding.setText(QCoreApplication.translate("wWing", u"15", None))
        self.cbPlot.setText(QCoreApplication.translate("wWing", u"Show Plot", None))
    # retranslateUi


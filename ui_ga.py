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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_wGA(object):
    def setupUi(self, wGA):
        if not wGA.objectName():
            wGA.setObjectName(u"wGA")
        wGA.resize(800, 600)
        self.centralwidget = QWidget(wGA)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 451, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.txtx1 = QLineEdit(self.gridLayoutWidget)
        self.txtx1.setObjectName(u"txtx1")

        self.gridLayout.addWidget(self.txtx1, 1, 2, 1, 1)

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

        self.txtx3 = QLineEdit(self.gridLayoutWidget)
        self.txtx3.setObjectName(u"txtx3")

        self.gridLayout.addWidget(self.txtx3, 1, 6, 1, 1)

        self.txtx2 = QLineEdit(self.gridLayoutWidget)
        self.txtx2.setObjectName(u"txtx2")

        self.gridLayout.addWidget(self.txtx2, 1, 4, 1, 1)

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

        self.txtOutput = QTextEdit(self.centralwidget)
        self.txtOutput.setObjectName(u"txtOutput")
        self.txtOutput.setGeometry(QRect(240, 110, 371, 141))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 110, 244, 86))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rbGolden = QRadioButton(self.verticalLayoutWidget)
        self.rbGolden.setObjectName(u"rbGolden")
        self.rbGolden.setChecked(True)

        self.verticalLayout.addWidget(self.rbGolden)

        self.rbInverse = QRadioButton(self.verticalLayoutWidget)
        self.rbInverse.setObjectName(u"rbInverse")

        self.verticalLayout.addWidget(self.rbInverse)

        self.rbNewton = QRadioButton(self.verticalLayoutWidget)
        self.rbNewton.setObjectName(u"rbNewton")

        self.verticalLayout.addWidget(self.rbNewton)

        self.btnCalculate = QPushButton(self.centralwidget)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(310, 270, 151, 41))
        self.cbPlot = QCheckBox(self.centralwidget)
        self.cbPlot.setObjectName(u"cbPlot")
        self.cbPlot.setGeometry(QRect(10, 200, 121, 24))
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(30, 270, 97, 26))
        wGA.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wGA)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        wGA.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wGA)
        self.statusbar.setObjectName(u"statusbar")
        wGA.setStatusBar(self.statusbar)

        self.retranslateUi(wGA)

        QMetaObject.connectSlotsByName(wGA)
    # setupUi

    def retranslateUi(self, wGA):
        wGA.setWindowTitle(QCoreApplication.translate("wGA", u"MainWindow", None))
        self.txtx1.setText(QCoreApplication.translate("wGA", u"0.5", None))
        self.label_2.setText(QCoreApplication.translate("wGA", u"Starting Points", None))
        self.label_5.setText(QCoreApplication.translate("wGA", u"x3", None))
        self.label_4.setText(QCoreApplication.translate("wGA", u"x2", None))
        self.txtFunction.setText(QCoreApplication.translate("wGA", u"x**5 - 2*(x**3) - 10*x + 5", None))
        self.txtx3.setText(QCoreApplication.translate("wGA", u"2", None))
        self.txtx2.setText(QCoreApplication.translate("wGA", u"1", None))
        self.txtIterations.setText(QCoreApplication.translate("wGA", u"2", None))
        self.label_6.setText(QCoreApplication.translate("wGA", u"x1", None))
        self.label.setText(QCoreApplication.translate("wGA", u"Function", None))
        self.label_3.setText(QCoreApplication.translate("wGA", u"Number of Iterations", None))
        self.rbGolden.setText(QCoreApplication.translate("wGA", u"Golden Search", None))
        self.rbInverse.setText(QCoreApplication.translate("wGA", u"Inverse Parabolic Interpolation", None))
        self.rbNewton.setText(QCoreApplication.translate("wGA", u"Netwon's Method", None))
        self.btnCalculate.setText(QCoreApplication.translate("wGA", u"Calculate", None))
        self.cbPlot.setText(QCoreApplication.translate("wGA", u"Plot function", None))
        self.btnBack.setText(QCoreApplication.translate("wGA", u"Back", None))
    # retranslateUi


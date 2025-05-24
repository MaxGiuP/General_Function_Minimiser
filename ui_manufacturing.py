# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manufacturing.ui'
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

class Ui_wManufacturing(object):
    def setupUi(self, wManufacturing):
        if not wManufacturing.objectName():
            wManufacturing.setObjectName(u"wManufacturing")
        wManufacturing.resize(464, 400)
        self.centralwidget = QWidget(wManufacturing)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnCalculate = QPushButton(self.centralwidget)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(270, 130, 151, 41))
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(120, 140, 97, 26))
        self.txtOutput = QTextEdit(self.centralwidget)
        self.txtOutput.setObjectName(u"txtOutput")
        self.txtOutput.setGeometry(QRect(10, 190, 371, 141))
        self.cbPlot = QCheckBox(self.centralwidget)
        self.cbPlot.setObjectName(u"cbPlot")
        self.cbPlot.setGeometry(QRect(0, 140, 121, 24))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 451, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.txtFunction = QLineEdit(self.gridLayoutWidget)
        self.txtFunction.setObjectName(u"txtFunction")

        self.gridLayout.addWidget(self.txtFunction, 0, 2, 1, 4)

        self.txtIterations = QLineEdit(self.gridLayoutWidget)
        self.txtIterations.setObjectName(u"txtIterations")

        self.gridLayout.addWidget(self.txtIterations, 2, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)

        self.txtMin = QLineEdit(self.gridLayoutWidget)
        self.txtMin.setObjectName(u"txtMin")

        self.gridLayout.addWidget(self.txtMin, 1, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.txtMax = QLineEdit(self.gridLayoutWidget)
        self.txtMax.setObjectName(u"txtMax")

        self.gridLayout.addWidget(self.txtMax, 1, 4, 1, 1)

        wManufacturing.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wManufacturing)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 464, 23))
        wManufacturing.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wManufacturing)
        self.statusbar.setObjectName(u"statusbar")
        wManufacturing.setStatusBar(self.statusbar)

        self.retranslateUi(wManufacturing)

        QMetaObject.connectSlotsByName(wManufacturing)
    # setupUi

    def retranslateUi(self, wManufacturing):
        wManufacturing.setWindowTitle(QCoreApplication.translate("wManufacturing", u"MainWindow", None))
        self.btnCalculate.setText(QCoreApplication.translate("wManufacturing", u"Calculate", None))
        self.btnBack.setText(QCoreApplication.translate("wManufacturing", u"Back", None))
        self.cbPlot.setText(QCoreApplication.translate("wManufacturing", u"Plot function", None))
        self.label_3.setText(QCoreApplication.translate("wManufacturing", u"Step Size", None))
        self.label_6.setText(QCoreApplication.translate("wManufacturing", u"Min", None))
        self.txtFunction.setText(QCoreApplication.translate("wManufacturing", u"x + 1/x", None))
        self.txtIterations.setText(QCoreApplication.translate("wManufacturing", u"0.25", None))
        self.label_4.setText(QCoreApplication.translate("wManufacturing", u"Max", None))
        self.txtMin.setText(QCoreApplication.translate("wManufacturing", u"0.5", None))
        self.label.setText(QCoreApplication.translate("wManufacturing", u"Function", None))
        self.label_2.setText(QCoreApplication.translate("wManufacturing", u"Starting Points", None))
        self.txtMax.setText(QCoreApplication.translate("wManufacturing", u"1", None))
    # retranslateUi


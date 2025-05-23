# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_wMenu(object):
    def setupUi(self, wMenu):
        if not wMenu.objectName():
            wMenu.setObjectName(u"wMenu")
        wMenu.resize(800, 600)
        self.centralwidget = QWidget(wMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnShowLinear = QPushButton(self.centralwidget)
        self.btnShowLinear.setObjectName(u"btnShowLinear")
        self.btnShowLinear.setGeometry(QRect(10, 10, 141, 71))
        self.btnMultivariable = QPushButton(self.centralwidget)
        self.btnMultivariable.setObjectName(u"btnMultivariable")
        self.btnMultivariable.setGeometry(QRect(160, 10, 141, 71))
        self.btnGA = QPushButton(self.centralwidget)
        self.btnGA.setObjectName(u"btnGA")
        self.btnGA.setGeometry(QRect(310, 10, 141, 71))
        self.btnConstrained = QPushButton(self.centralwidget)
        self.btnConstrained.setObjectName(u"btnConstrained")
        self.btnConstrained.setGeometry(QRect(10, 120, 141, 71))
        self.btnMultiobjective = QPushButton(self.centralwidget)
        self.btnMultiobjective.setObjectName(u"btnMultiobjective")
        self.btnMultiobjective.setGeometry(QRect(160, 120, 141, 71))
        self.btnWing = QPushButton(self.centralwidget)
        self.btnWing.setObjectName(u"btnWing")
        self.btnWing.setGeometry(QRect(30, 340, 181, 71))
        self.btnManufacturing = QPushButton(self.centralwidget)
        self.btnManufacturing.setObjectName(u"btnManufacturing")
        self.btnManufacturing.setGeometry(QRect(30, 420, 181, 71))
        wMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        wMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wMenu)
        self.statusbar.setObjectName(u"statusbar")
        wMenu.setStatusBar(self.statusbar)

        self.retranslateUi(wMenu)

        QMetaObject.connectSlotsByName(wMenu)
    # setupUi

    def retranslateUi(self, wMenu):
        wMenu.setWindowTitle(QCoreApplication.translate("wMenu", u"MainWindow", None))
        self.btnShowLinear.setText(QCoreApplication.translate("wMenu", u"Linear", None))
        self.btnMultivariable.setText(QCoreApplication.translate("wMenu", u"Multi-Variable", None))
        self.btnGA.setText(QCoreApplication.translate("wMenu", u"Genetic Algorithm", None))
        self.btnConstrained.setText(QCoreApplication.translate("wMenu", u"Constrained", None))
        self.btnMultiobjective.setText(QCoreApplication.translate("wMenu", u"Multi-Objective", None))
        self.btnWing.setText(QCoreApplication.translate("wMenu", u"Wing Question", None))
        self.btnManufacturing.setText(QCoreApplication.translate("wMenu", u"Manufacturing Question", None))
    # retranslateUi


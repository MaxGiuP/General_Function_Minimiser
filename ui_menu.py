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
        wMenu.resize(460, 459)
        self.centralwidget = QWidget(wMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnLinear = QPushButton(self.centralwidget)
        self.btnLinear.setObjectName(u"btnLinear")
        self.btnLinear.setGeometry(QRect(10, 10, 141, 71))
        self.btnMultiVariable = QPushButton(self.centralwidget)
        self.btnMultiVariable.setObjectName(u"btnMultiVariable")
        self.btnMultiVariable.setGeometry(QRect(160, 10, 141, 71))
        self.btnGA = QPushButton(self.centralwidget)
        self.btnGA.setObjectName(u"btnGA")
        self.btnGA.setGeometry(QRect(310, 10, 141, 71))
        self.btnConstrained = QPushButton(self.centralwidget)
        self.btnConstrained.setObjectName(u"btnConstrained")
        self.btnConstrained.setGeometry(QRect(10, 120, 141, 71))
        self.btnMultiObjective = QPushButton(self.centralwidget)
        self.btnMultiObjective.setObjectName(u"btnMultiObjective")
        self.btnMultiObjective.setGeometry(QRect(160, 120, 141, 71))
        self.btnWing = QPushButton(self.centralwidget)
        self.btnWing.setObjectName(u"btnWing")
        self.btnWing.setGeometry(QRect(130, 250, 181, 71))
        self.btnManufacturing = QPushButton(self.centralwidget)
        self.btnManufacturing.setObjectName(u"btnManufacturing")
        self.btnManufacturing.setGeometry(QRect(130, 330, 181, 71))
        wMenu.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wMenu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 460, 23))
        wMenu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wMenu)
        self.statusbar.setObjectName(u"statusbar")
        wMenu.setStatusBar(self.statusbar)

        self.retranslateUi(wMenu)

        QMetaObject.connectSlotsByName(wMenu)
    # setupUi

    def retranslateUi(self, wMenu):
        wMenu.setWindowTitle(QCoreApplication.translate("wMenu", u"Menu", None))
        self.btnLinear.setText(QCoreApplication.translate("wMenu", u"Linear", None))
        self.btnMultiVariable.setText(QCoreApplication.translate("wMenu", u"Multi-Variable", None))
        self.btnGA.setText(QCoreApplication.translate("wMenu", u"Genetic Algorithm", None))
        self.btnConstrained.setText(QCoreApplication.translate("wMenu", u"Constrained", None))
        self.btnMultiObjective.setText(QCoreApplication.translate("wMenu", u"Multi-Objective", None))
        self.btnWing.setText(QCoreApplication.translate("wMenu", u"Wing Question", None))
        self.btnManufacturing.setText(QCoreApplication.translate("wMenu", u"Manufacturing Question", None))
    # retranslateUi


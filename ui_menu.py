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
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 10, 141, 71))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 10, 141, 71))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 120, 141, 71))
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
        self.pushButton_2.setText(QCoreApplication.translate("wMenu", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("wMenu", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("wMenu", u"PushButton", None))
    # retranslateUi


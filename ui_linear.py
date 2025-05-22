# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'linear.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_wLinear(object):
    def setupUi(self, wLinear):
        if not wLinear.objectName():
            wLinear.setObjectName(u"wLinear")
        wLinear.resize(469, 310)
        self.centralwidget = QWidget(wLinear)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnCalculate = QPushButton(self.centralwidget)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(170, 120, 97, 71))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 120, 160, 86))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.rbGolden = QRadioButton(self.verticalLayoutWidget)
        self.rbGolden.setObjectName(u"rbGolden")

        self.verticalLayout.addWidget(self.rbGolden)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout.addWidget(self.radioButton_3)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(280, 120, 181, 91))
        self.cbPlot = QCheckBox(self.centralwidget)
        self.cbPlot.setObjectName(u"cbPlot")
        self.cbPlot.setGeometry(QRect(20, 210, 121, 24))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 451, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)

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

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 5)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 1, 6, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 4, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)

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

        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(190, 230, 97, 26))
        wLinear.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(wLinear)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 469, 23))
        self.menuLinear_Search = QMenu(self.menubar)
        self.menuLinear_Search.setObjectName(u"menuLinear_Search")
        wLinear.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(wLinear)
        self.statusbar.setObjectName(u"statusbar")
        wLinear.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuLinear_Search.menuAction())

        self.retranslateUi(wLinear)

        QMetaObject.connectSlotsByName(wLinear)
    # setupUi

    def retranslateUi(self, wLinear):
        wLinear.setWindowTitle(QCoreApplication.translate("wLinear", u"MainWindow", None))
        self.btnCalculate.setText(QCoreApplication.translate("wLinear", u"Calculate", None))
        self.rbGolden.setText(QCoreApplication.translate("wLinear", u"Golden Search", None))
        self.radioButton_2.setText(QCoreApplication.translate("wLinear", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("wLinear", u"RadioButton", None))
        self.cbPlot.setText(QCoreApplication.translate("wLinear", u"Plot function", None))
        self.label_2.setText(QCoreApplication.translate("wLinear", u"Starting Points", None))
        self.label_5.setText(QCoreApplication.translate("wLinear", u"x3", None))
        self.label_4.setText(QCoreApplication.translate("wLinear", u"x2", None))
        self.label_6.setText(QCoreApplication.translate("wLinear", u"x1", None))
        self.label.setText(QCoreApplication.translate("wLinear", u"Function", None))
        self.label_3.setText(QCoreApplication.translate("wLinear", u"Number of Iterations", None))
        self.btnBack.setText(QCoreApplication.translate("wLinear", u"Back", None))
        self.menuLinear_Search.setTitle("")
    # retranslateUi


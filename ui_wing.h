/********************************************************************************
** Form generated from reading UI file 'wing.ui'
**
** Created by: Qt User Interface Compiler version 5.15.17
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WING_H
#define UI_WING_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_wWing
{
public:
    QWidget *centralwidget;
    QPushButton *btnCalculate;
    QPushButton *btnBack;
    QTextEdit *txtOutput;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QLineEdit *txtCLCoeff;
    QLabel *label_6;
    QLabel *label_2;
    QLineEdit *txtAlphaGuess;
    QLineEdit *txtCDConst;
    QLabel *label_4;
    QLabel *label_5;
    QLineEdit *txtCLOff;
    QLabel *label;
    QLabel *label_7;
    QLabel *label_3;
    QLineEdit *txtCDQuad;
    QLabel *label_8;
    QLineEdit *txtStallLimit;
    QLineEdit *txtCruise;
    QLineEdit *txtLanding;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *wWing)
    {
        if (wWing->objectName().isEmpty())
            wWing->setObjectName(QString::fromUtf8("wWing"));
        wWing->resize(468, 496);
        centralwidget = new QWidget(wWing);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        btnCalculate = new QPushButton(centralwidget);
        btnCalculate->setObjectName(QString::fromUtf8("btnCalculate"));
        btnCalculate->setGeometry(QRect(170, 260, 151, 41));
        btnBack = new QPushButton(centralwidget);
        btnBack->setObjectName(QString::fromUtf8("btnBack"));
        btnBack->setGeometry(QRect(30, 270, 97, 26));
        txtOutput = new QTextEdit(centralwidget);
        txtOutput->setObjectName(QString::fromUtf8("txtOutput"));
        txtOutput->setGeometry(QRect(10, 310, 441, 141));
        gridLayoutWidget = new QWidget(centralwidget);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(0, 0, 451, 252));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        txtCLCoeff = new QLineEdit(gridLayoutWidget);
        txtCLCoeff->setObjectName(QString::fromUtf8("txtCLCoeff"));

        gridLayout->addWidget(txtCLCoeff, 0, 1, 1, 1);

        label_6 = new QLabel(gridLayoutWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_6, 5, 0, 1, 1);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        txtAlphaGuess = new QLineEdit(gridLayoutWidget);
        txtAlphaGuess->setObjectName(QString::fromUtf8("txtAlphaGuess"));

        gridLayout->addWidget(txtAlphaGuess, 4, 1, 1, 1);

        txtCDConst = new QLineEdit(gridLayoutWidget);
        txtCDConst->setObjectName(QString::fromUtf8("txtCDConst"));

        gridLayout->addWidget(txtCDConst, 2, 1, 1, 1);

        label_4 = new QLabel(gridLayoutWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 2, 0, 1, 1);

        label_5 = new QLabel(gridLayoutWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout->addWidget(label_5, 3, 0, 1, 1);

        txtCLOff = new QLineEdit(gridLayoutWidget);
        txtCLOff->setObjectName(QString::fromUtf8("txtCLOff"));

        gridLayout->addWidget(txtCLOff, 1, 1, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label, 0, 0, 1, 1);

        label_7 = new QLabel(gridLayoutWidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_7, 6, 0, 1, 1);

        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_3, 4, 0, 1, 1);

        txtCDQuad = new QLineEdit(gridLayoutWidget);
        txtCDQuad->setObjectName(QString::fromUtf8("txtCDQuad"));

        gridLayout->addWidget(txtCDQuad, 3, 1, 1, 1);

        label_8 = new QLabel(gridLayoutWidget);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_8, 7, 0, 1, 1);

        txtStallLimit = new QLineEdit(gridLayoutWidget);
        txtStallLimit->setObjectName(QString::fromUtf8("txtStallLimit"));

        gridLayout->addWidget(txtStallLimit, 5, 1, 1, 1);

        txtCruise = new QLineEdit(gridLayoutWidget);
        txtCruise->setObjectName(QString::fromUtf8("txtCruise"));

        gridLayout->addWidget(txtCruise, 6, 1, 1, 1);

        txtLanding = new QLineEdit(gridLayoutWidget);
        txtLanding->setObjectName(QString::fromUtf8("txtLanding"));

        gridLayout->addWidget(txtLanding, 7, 1, 1, 1);

        wWing->setCentralWidget(centralwidget);
        menubar = new QMenuBar(wWing);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 468, 23));
        wWing->setMenuBar(menubar);
        statusbar = new QStatusBar(wWing);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        wWing->setStatusBar(statusbar);

        retranslateUi(wWing);

        QMetaObject::connectSlotsByName(wWing);
    } // setupUi

    void retranslateUi(QMainWindow *wWing)
    {
        wWing->setWindowTitle(QCoreApplication::translate("wWing", "Wing Question", nullptr));
        btnCalculate->setText(QCoreApplication::translate("wWing", "Calculate", nullptr));
        btnBack->setText(QCoreApplication::translate("wWing", "Back", nullptr));
        txtCLCoeff->setText(QCoreApplication::translate("wWing", "0.093", nullptr));
        label_6->setText(QCoreApplication::translate("wWing", "Stall Limit", nullptr));
        label_2->setText(QCoreApplication::translate("wWing", "CL Offset", nullptr));
        txtAlphaGuess->setText(QCoreApplication::translate("wWing", "5", nullptr));
        txtCDConst->setText(QCoreApplication::translate("wWing", "0.032", nullptr));
        label_4->setText(QCoreApplication::translate("wWing", "CD Constant", nullptr));
        label_5->setText(QCoreApplication::translate("wWing", "CD Quadratic", nullptr));
        txtCLOff->setText(QCoreApplication::translate("wWing", "1", nullptr));
        label->setText(QCoreApplication::translate("wWing", "CL Coefficient", nullptr));
        label_7->setText(QCoreApplication::translate("wWing", "Cruise Speed", nullptr));
        label_3->setText(QCoreApplication::translate("wWing", "Alpha Guess", nullptr));
        txtCDQuad->setText(QCoreApplication::translate("wWing", "0.055", nullptr));
        label_8->setText(QCoreApplication::translate("wWing", "Landing Speed", nullptr));
        txtStallLimit->setText(QCoreApplication::translate("wWing", "14", nullptr));
        txtCruise->setText(QCoreApplication::translate("wWing", "40", nullptr));
        txtLanding->setText(QCoreApplication::translate("wWing", "15", nullptr));
    } // retranslateUi

};

namespace Ui {
    class wWing: public Ui_wWing {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WING_H

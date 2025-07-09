/********************************************************************************
** Form generated from reading UI file 'multivariable.ui'
**
** Created by: Qt User Interface Compiler version 6.9.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MULTIVARIABLE_H
#define UI_MULTIVARIABLE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_wMultiVariable
{
public:
    QWidget *centralwidget;
    QCheckBox *cbPlot;
    QTextEdit *txtOutput;
    QPushButton *btnCalculate;
    QPushButton *btnBack;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QLineEdit *txtx;
    QLabel *label_2;
    QLabel *label_5;
    QLabel *label_4;
    QLineEdit *txtFunction;
    QLineEdit *txth;
    QLineEdit *txty;
    QLineEdit *txtIterations;
    QLabel *label_6;
    QLabel *label;
    QLabel *label_3;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QRadioButton *rbSteepest;
    QRadioButton *rbConjugate;
    QRadioButton *rbNewton;
    QRadioButton *rbBFGS;
    QRadioButton *rbHJ;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *wMultiVariable)
    {
        if (wMultiVariable->objectName().isEmpty())
            wMultiVariable->setObjectName("wMultiVariable");
        wMultiVariable->resize(800, 600);
        centralwidget = new QWidget(wMultiVariable);
        centralwidget->setObjectName("centralwidget");
        cbPlot = new QCheckBox(centralwidget);
        cbPlot->setObjectName("cbPlot");
        cbPlot->setGeometry(QRect(470, 10, 121, 24));
        txtOutput = new QTextEdit(centralwidget);
        txtOutput->setObjectName("txtOutput");
        txtOutput->setGeometry(QRect(180, 120, 371, 141));
        btnCalculate = new QPushButton(centralwidget);
        btnCalculate->setObjectName("btnCalculate");
        btnCalculate->setGeometry(QRect(320, 280, 151, 41));
        btnBack = new QPushButton(centralwidget);
        btnBack->setObjectName("btnBack");
        btnBack->setGeometry(QRect(170, 280, 97, 26));
        gridLayoutWidget = new QWidget(centralwidget);
        gridLayoutWidget->setObjectName("gridLayoutWidget");
        gridLayoutWidget->setGeometry(QRect(10, 10, 451, 111));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName("gridLayout");
        gridLayout->setContentsMargins(0, 0, 0, 0);
        txtx = new QLineEdit(gridLayoutWidget);
        txtx->setObjectName("txtx");

        gridLayout->addWidget(txtx, 1, 2, 1, 1);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName("label_2");
        label_2->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        label_5 = new QLabel(gridLayoutWidget);
        label_5->setObjectName("label_5");

        gridLayout->addWidget(label_5, 1, 5, 1, 1);

        label_4 = new QLabel(gridLayoutWidget);
        label_4->setObjectName("label_4");

        gridLayout->addWidget(label_4, 1, 3, 1, 1);

        txtFunction = new QLineEdit(gridLayoutWidget);
        txtFunction->setObjectName("txtFunction");

        gridLayout->addWidget(txtFunction, 0, 2, 1, 5);

        txth = new QLineEdit(gridLayoutWidget);
        txth->setObjectName("txth");

        gridLayout->addWidget(txth, 1, 6, 1, 1);

        txty = new QLineEdit(gridLayoutWidget);
        txty->setObjectName("txty");

        gridLayout->addWidget(txty, 1, 4, 1, 1);

        txtIterations = new QLineEdit(gridLayoutWidget);
        txtIterations->setObjectName("txtIterations");

        gridLayout->addWidget(txtIterations, 2, 2, 1, 1);

        label_6 = new QLabel(gridLayoutWidget);
        label_6->setObjectName("label_6");
        label_6->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_6, 1, 1, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName("label");
        label->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label, 0, 0, 1, 2);

        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName("label_3");
        label_3->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_3, 2, 0, 1, 2);

        verticalLayoutWidget = new QWidget(centralwidget);
        verticalLayoutWidget->setObjectName("verticalLayoutWidget");
        verticalLayoutWidget->setGeometry(QRect(10, 120, 171, 146));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setObjectName("verticalLayout");
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        rbSteepest = new QRadioButton(verticalLayoutWidget);
        rbSteepest->setObjectName("rbSteepest");
        rbSteepest->setChecked(true);

        verticalLayout->addWidget(rbSteepest);

        rbConjugate = new QRadioButton(verticalLayoutWidget);
        rbConjugate->setObjectName("rbConjugate");

        verticalLayout->addWidget(rbConjugate);

        rbNewton = new QRadioButton(verticalLayoutWidget);
        rbNewton->setObjectName("rbNewton");

        verticalLayout->addWidget(rbNewton);

        rbBFGS = new QRadioButton(verticalLayoutWidget);
        rbBFGS->setObjectName("rbBFGS");

        verticalLayout->addWidget(rbBFGS);

        rbHJ = new QRadioButton(verticalLayoutWidget);
        rbHJ->setObjectName("rbHJ");

        verticalLayout->addWidget(rbHJ);

        wMultiVariable->setCentralWidget(centralwidget);
        menubar = new QMenuBar(wMultiVariable);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 800, 23));
        wMultiVariable->setMenuBar(menubar);
        statusbar = new QStatusBar(wMultiVariable);
        statusbar->setObjectName("statusbar");
        wMultiVariable->setStatusBar(statusbar);

        retranslateUi(wMultiVariable);

        QMetaObject::connectSlotsByName(wMultiVariable);
    } // setupUi

    void retranslateUi(QMainWindow *wMultiVariable)
    {
        wMultiVariable->setWindowTitle(QCoreApplication::translate("wMultiVariable", "Multi Variable Search", nullptr));
        cbPlot->setText(QCoreApplication::translate("wMultiVariable", "Plot function", nullptr));
        btnCalculate->setText(QCoreApplication::translate("wMultiVariable", "Calculate", nullptr));
        btnBack->setText(QCoreApplication::translate("wMultiVariable", "Back", nullptr));
        label_2->setText(QCoreApplication::translate("wMultiVariable", "Starting Points", nullptr));
        label_5->setText(QCoreApplication::translate("wMultiVariable", "h", nullptr));
        label_4->setText(QCoreApplication::translate("wMultiVariable", "y", nullptr));
        txtFunction->setText(QString());
        txtFunction->setPlaceholderText(QCoreApplication::translate("wMultiVariable", "Python style input", nullptr));
        txth->setPlaceholderText(QCoreApplication::translate("wMultiVariable", "Step Size", nullptr));
        txtIterations->setText(QCoreApplication::translate("wMultiVariable", "1", nullptr));
        label_6->setText(QCoreApplication::translate("wMultiVariable", "x", nullptr));
        label->setText(QCoreApplication::translate("wMultiVariable", "Function", nullptr));
        label_3->setText(QCoreApplication::translate("wMultiVariable", "Number of Iterations", nullptr));
        rbSteepest->setText(QCoreApplication::translate("wMultiVariable", "Steepest Descent", nullptr));
        rbConjugate->setText(QCoreApplication::translate("wMultiVariable", "Conjugate Gradient", nullptr));
        rbNewton->setText(QCoreApplication::translate("wMultiVariable", "Netwon's Method", nullptr));
        rbBFGS->setText(QCoreApplication::translate("wMultiVariable", "BFGS", nullptr));
        rbHJ->setText(QCoreApplication::translate("wMultiVariable", "Hooke and Jeeves", nullptr));
    } // retranslateUi

};

namespace Ui {
    class wMultiVariable: public Ui_wMultiVariable {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MULTIVARIABLE_H

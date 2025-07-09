/********************************************************************************
** Form generated from reading UI file 'constrained.ui'
**
** Created by: Qt User Interface Compiler version 5.15.17
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CONSTRAINED_H
#define UI_CONSTRAINED_H

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

class Ui_wConstrained
{
public:
    QWidget *centralwidget;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QLineEdit *txtFunction;
    QTextEdit *txtEq;
    QLabel *label_2;
    QLabel *label;
    QLabel *label_3;
    QTextEdit *txtIneq;
    QTextEdit *txtOutput;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QRadioButton *rbLagrange;
    QRadioButton *rbFixedPenaltyAny;
    QRadioButton *rbFixedPenaltyEach;
    QRadioButton *rbVaryingDoC;
    QRadioButton *rbVaryingSL;
    QRadioButton *rbAugmented;
    QPushButton *btnCalculate;
    QCheckBox *cbPlot;
    QPushButton *btnBack;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *wConstrained)
    {
        if (wConstrained->objectName().isEmpty())
            wConstrained->setObjectName(QString::fromUtf8("wConstrained"));
        wConstrained->resize(611, 459);
        centralwidget = new QWidget(wConstrained);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        gridLayoutWidget = new QWidget(centralwidget);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(10, 0, 471, 180));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        txtFunction = new QLineEdit(gridLayoutWidget);
        txtFunction->setObjectName(QString::fromUtf8("txtFunction"));

        gridLayout->addWidget(txtFunction, 0, 1, 1, 2);

        txtEq = new QTextEdit(gridLayoutWidget);
        txtEq->setObjectName(QString::fromUtf8("txtEq"));

        gridLayout->addWidget(txtEq, 1, 1, 1, 1);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label, 0, 0, 1, 1);

        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_3, 2, 0, 1, 1);

        txtIneq = new QTextEdit(gridLayoutWidget);
        txtIneq->setObjectName(QString::fromUtf8("txtIneq"));

        gridLayout->addWidget(txtIneq, 2, 1, 1, 1);

        txtOutput = new QTextEdit(centralwidget);
        txtOutput->setObjectName(QString::fromUtf8("txtOutput"));
        txtOutput->setGeometry(QRect(230, 240, 281, 141));
        verticalLayoutWidget = new QWidget(centralwidget);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(10, 190, 311, 212));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        rbLagrange = new QRadioButton(verticalLayoutWidget);
        rbLagrange->setObjectName(QString::fromUtf8("rbLagrange"));
        rbLagrange->setChecked(true);

        verticalLayout->addWidget(rbLagrange);

        rbFixedPenaltyAny = new QRadioButton(verticalLayoutWidget);
        rbFixedPenaltyAny->setObjectName(QString::fromUtf8("rbFixedPenaltyAny"));

        verticalLayout->addWidget(rbFixedPenaltyAny);

        rbFixedPenaltyEach = new QRadioButton(verticalLayoutWidget);
        rbFixedPenaltyEach->setObjectName(QString::fromUtf8("rbFixedPenaltyEach"));

        verticalLayout->addWidget(rbFixedPenaltyEach);

        rbVaryingDoC = new QRadioButton(verticalLayoutWidget);
        rbVaryingDoC->setObjectName(QString::fromUtf8("rbVaryingDoC"));

        verticalLayout->addWidget(rbVaryingDoC);

        rbVaryingSL = new QRadioButton(verticalLayoutWidget);
        rbVaryingSL->setObjectName(QString::fromUtf8("rbVaryingSL"));

        verticalLayout->addWidget(rbVaryingSL);

        rbAugmented = new QRadioButton(verticalLayoutWidget);
        rbAugmented->setObjectName(QString::fromUtf8("rbAugmented"));

        verticalLayout->addWidget(rbAugmented);

        btnCalculate = new QPushButton(centralwidget);
        btnCalculate->setObjectName(QString::fromUtf8("btnCalculate"));
        btnCalculate->setGeometry(QRect(270, 190, 151, 41));
        cbPlot = new QCheckBox(centralwidget);
        cbPlot->setObjectName(QString::fromUtf8("cbPlot"));
        cbPlot->setGeometry(QRect(490, 10, 121, 24));
        btnBack = new QPushButton(centralwidget);
        btnBack->setObjectName(QString::fromUtf8("btnBack"));
        btnBack->setGeometry(QRect(310, 390, 97, 26));
        wConstrained->setCentralWidget(centralwidget);
        menubar = new QMenuBar(wConstrained);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 611, 23));
        wConstrained->setMenuBar(menubar);
        statusbar = new QStatusBar(wConstrained);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        wConstrained->setStatusBar(statusbar);

        retranslateUi(wConstrained);

        QMetaObject::connectSlotsByName(wConstrained);
    } // setupUi

    void retranslateUi(QMainWindow *wConstrained)
    {
        wConstrained->setWindowTitle(QCoreApplication::translate("wConstrained", "ConstrainedWindow", nullptr));
        txtEq->setDocumentTitle(QString());
        label_2->setText(QCoreApplication::translate("wConstrained", "Equality Constraints", nullptr));
        label->setText(QCoreApplication::translate("wConstrained", "Function", nullptr));
        label_3->setText(QCoreApplication::translate("wConstrained", "Inequality Constraints", nullptr));
        rbLagrange->setText(QCoreApplication::translate("wConstrained", "Lagrange Multipliers", nullptr));
        rbFixedPenaltyAny->setText(QCoreApplication::translate("wConstrained", "Fixed Penalty for \n"
                                                                               "ANY broken constraint", nullptr));
        rbFixedPenaltyEach->setText(QCoreApplication::translate("wConstrained", "Fixed Penalty for \n"
                                                                                "EACH broken constraint", nullptr));
        rbVaryingDoC->setText(QCoreApplication::translate("wConstrained", "Varying DoC", nullptr));
        rbVaryingSL->setText(QCoreApplication::translate("wConstrained", "Varying SL", nullptr));
        rbAugmented->setText(QCoreApplication::translate("wConstrained", "Augmented Lagrange", nullptr));
        btnCalculate->setText(QCoreApplication::translate("wConstrained", "Calculate", nullptr));
        cbPlot->setText(QCoreApplication::translate("wConstrained", "Plot function", nullptr));
        btnBack->setText(QCoreApplication::translate("wConstrained", "Back", nullptr));
    } // retranslateUi

};

namespace Ui {
class wConstrained: public Ui_wConstrained {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CONSTRAINED_H

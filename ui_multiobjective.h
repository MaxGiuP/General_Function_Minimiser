/********************************************************************************
** Form generated from reading UI file 'multiobjective.ui'
**
** Created by: Qt User Interface Compiler version 5.15.17
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MULTIOBJECTIVE_H
#define UI_MULTIOBJECTIVE_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFormLayout>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_wMultiObjective
{
public:
    QWidget *centralwidget;
    QTextEdit *txtOutput;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QRadioButton *rbEigenvectors;
    QRadioButton *rbFuzzyLogic;
    QRadioButton *rbPareto;
    QRadioButton *rbParetoTable;
    QPushButton *btnCalculate;
    QCheckBox *cbPlot;
    QPushButton *btnBack;
    QWidget *formLayoutWidget;
    QFormLayout *formLayout;
    QTextEdit *txtFunctions;
    QLabel *label;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QTextEdit *txtRight;
    QTextEdit *txtLeft;
    QLabel *label_2;
    QLabel *label_3;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *wMultiObjective)
    {
        if (wMultiObjective->objectName().isEmpty())
            wMultiObjective->setObjectName(QString::fromUtf8("wMultiObjective"));
        wMultiObjective->resize(635, 542);
        centralwidget = new QWidget(wMultiObjective);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        txtOutput = new QTextEdit(centralwidget);
        txtOutput->setObjectName(QString::fromUtf8("txtOutput"));
        txtOutput->setGeometry(QRect(220, 170, 371, 181));
        verticalLayoutWidget = new QWidget(centralwidget);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(10, 170, 201, 116));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        rbEigenvectors = new QRadioButton(verticalLayoutWidget);
        rbEigenvectors->setObjectName(QString::fromUtf8("rbEigenvectors"));
        rbEigenvectors->setChecked(true);

        verticalLayout->addWidget(rbEigenvectors);

        rbFuzzyLogic = new QRadioButton(verticalLayoutWidget);
        rbFuzzyLogic->setObjectName(QString::fromUtf8("rbFuzzyLogic"));

        verticalLayout->addWidget(rbFuzzyLogic);

        rbPareto = new QRadioButton(verticalLayoutWidget);
        rbPareto->setObjectName(QString::fromUtf8("rbPareto"));

        verticalLayout->addWidget(rbPareto);

        rbParetoTable = new QRadioButton(verticalLayoutWidget);
        rbParetoTable->setObjectName(QString::fromUtf8("rbParetoTable"));

        verticalLayout->addWidget(rbParetoTable);

        btnCalculate = new QPushButton(centralwidget);
        btnCalculate->setObjectName(QString::fromUtf8("btnCalculate"));
        btnCalculate->setGeometry(QRect(310, 380, 151, 41));
        cbPlot = new QCheckBox(centralwidget);
        cbPlot->setObjectName(QString::fromUtf8("cbPlot"));
        cbPlot->setGeometry(QRect(30, 310, 121, 24));
        btnBack = new QPushButton(centralwidget);
        btnBack->setObjectName(QString::fromUtf8("btnBack"));
        btnBack->setGeometry(QRect(70, 390, 97, 26));
        formLayoutWidget = new QWidget(centralwidget);
        formLayoutWidget->setObjectName(QString::fromUtf8("formLayoutWidget"));
        formLayoutWidget->setGeometry(QRect(10, 10, 311, 141));
        formLayout = new QFormLayout(formLayoutWidget);
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        formLayout->setContentsMargins(0, 0, 0, 0);
        txtFunctions = new QTextEdit(formLayoutWidget);
        txtFunctions->setObjectName(QString::fromUtf8("txtFunctions"));

        formLayout->setWidget(1, QFormLayout::SpanningRole, txtFunctions);

        label = new QLabel(formLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));

        formLayout->setWidget(0, QFormLayout::SpanningRole, label);

        gridLayoutWidget = new QWidget(centralwidget);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(340, 10, 160, 141));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        txtRight = new QTextEdit(gridLayoutWidget);
        txtRight->setObjectName(QString::fromUtf8("txtRight"));

        gridLayout->addWidget(txtRight, 1, 1, 1, 1);

        txtLeft = new QTextEdit(gridLayoutWidget);
        txtLeft->setObjectName(QString::fromUtf8("txtLeft"));

        gridLayout->addWidget(txtLeft, 1, 0, 1, 1);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 0, 0, 1, 1);

        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout->addWidget(label_3, 0, 1, 1, 1);

        wMultiObjective->setCentralWidget(centralwidget);
        menubar = new QMenuBar(wMultiObjective);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 635, 23));
        wMultiObjective->setMenuBar(menubar);
        statusbar = new QStatusBar(wMultiObjective);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        wMultiObjective->setStatusBar(statusbar);

        retranslateUi(wMultiObjective);

        QMetaObject::connectSlotsByName(wMultiObjective);
    } // setupUi

    void retranslateUi(QMainWindow *wMultiObjective)
    {
        wMultiObjective->setWindowTitle(QCoreApplication::translate("wMultiObjective", "Multi Objective Search", nullptr));
        rbEigenvectors->setText(QCoreApplication::translate("wMultiObjective", "Eigenvectors", nullptr));
        rbFuzzyLogic->setText(QCoreApplication::translate("wMultiObjective", "Fuzzy Logic", nullptr));
        rbPareto->setText(QCoreApplication::translate("wMultiObjective", "Pareto Dominance", nullptr));
        rbParetoTable->setText(QCoreApplication::translate("wMultiObjective", "Pareto Dominance Table", nullptr));
        btnCalculate->setText(QCoreApplication::translate("wMultiObjective", "Calculate", nullptr));
        cbPlot->setText(QCoreApplication::translate("wMultiObjective", "Plot function", nullptr));
        btnBack->setText(QCoreApplication::translate("wMultiObjective", "Back", nullptr));
        label->setText(QCoreApplication::translate("wMultiObjective", "Functions", nullptr));
        label_2->setText(QCoreApplication::translate("wMultiObjective", "Min", nullptr));
        label_3->setText(QCoreApplication::translate("wMultiObjective", "Max", nullptr));
    } // retranslateUi

};

namespace Ui {
    class wMultiObjective: public Ui_wMultiObjective {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MULTIOBJECTIVE_H

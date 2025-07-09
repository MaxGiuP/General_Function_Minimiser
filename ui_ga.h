/********************************************************************************
** Form generated from reading UI file 'ga.ui'
**
** Created by: Qt User Interface Compiler version 5.15.17
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_GA_H
#define UI_GA_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
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

class Ui_wGA
{
public:
    QWidget *centralwidget;
    QTextEdit *txtOutput;
    QPushButton *btnCalculate;
    QPushButton *btnBack;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QLabel *label_24;
    QLineEdit *txtRepMut2;
    QLabel *label_14;
    QLineEdit *txtParent2;
    QLineEdit *txtParent1;
    QLabel *label_2;
    QLabel *label_22;
    QLabel *label;
    QLineEdit *txtRepMut1;
    QLabel *label_23;
    QLineEdit *txtRepLow;
    QLineEdit *txtRepUp;
    QLineEdit *txtRepBits;
    QLineEdit *txtRepCross;
    QWidget *gridLayoutWidget_2;
    QGridLayout *gridLayout_2;
    QLabel *label_4;
    QLineEdit *txtUp;
    QComboBox *cmbOrder;
    QLabel *label_8;
    QLabel *label_10;
    QLabel *label_9;
    QLabel *label_5;
    QLineEdit *txtRank;
    QLabel *label_6;
    QLineEdit *txtMut;
    QLineEdit *txtBits;
    QLineEdit *txtGens;
    QLineEdit *txtPop;
    QLabel *label_7;
    QLabel *label_11;
    QLabel *label_3;
    QLineEdit *txtCross;
    QLineEdit *txtLow;
    QLabel *label_12;
    QLabel *label_13;
    QComboBox *cmbMethod;
    QLineEdit *txtFunction;
    QPushButton *btnSelection;
    QTextEdit *txtSelection;
    QWidget *gridLayoutWidget_4;
    QGridLayout *gridLayout_4;
    QLabel *label_21;
    QLineEdit *txtValues;
    QComboBox *cmbSelOrder;
    QLabel *label_20;
    QLabel *label_27;
    QLabel *label_25;
    QLineEdit *txtFitness;
    QLabel *label_19;
    QLabel *label_26;
    QLineEdit *txtSelRank;
    QComboBox *cmbSelMethod;
    QLineEdit *txtRands;
    QLabel *label_28;
    QComboBox *cmbSelRep;
    QPushButton *btnReproduction;
    QTextEdit *txtReproduction;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *wGA)
    {
        if (wGA->objectName().isEmpty())
            wGA->setObjectName(QString::fromUtf8("wGA"));
        wGA->resize(938, 552);
        centralwidget = new QWidget(wGA);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        txtOutput = new QTextEdit(centralwidget);
        txtOutput->setObjectName(QString::fromUtf8("txtOutput"));
        txtOutput->setGeometry(QRect(10, 420, 301, 81));
        btnCalculate = new QPushButton(centralwidget);
        btnCalculate->setObjectName(QString::fromUtf8("btnCalculate"));
        btnCalculate->setGeometry(QRect(150, 370, 151, 41));
        btnBack = new QPushButton(centralwidget);
        btnBack->setObjectName(QString::fromUtf8("btnBack"));
        btnBack->setGeometry(QRect(20, 380, 97, 26));
        gridLayoutWidget = new QWidget(centralwidget);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(590, 10, 291, 200));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        label_24 = new QLabel(gridLayoutWidget);
        label_24->setObjectName(QString::fromUtf8("label_24"));

        gridLayout->addWidget(label_24, 1, 0, 1, 1);

        txtRepMut2 = new QLineEdit(gridLayoutWidget);
        txtRepMut2->setObjectName(QString::fromUtf8("txtRepMut2"));

        gridLayout->addWidget(txtRepMut2, 5, 2, 1, 1);

        label_14 = new QLabel(gridLayoutWidget);
        label_14->setObjectName(QString::fromUtf8("label_14"));

        gridLayout->addWidget(label_14, 5, 0, 1, 1);

        txtParent2 = new QLineEdit(gridLayoutWidget);
        txtParent2->setObjectName(QString::fromUtf8("txtParent2"));

        gridLayout->addWidget(txtParent2, 3, 2, 1, 1);

        txtParent1 = new QLineEdit(gridLayoutWidget);
        txtParent1->setObjectName(QString::fromUtf8("txtParent1"));

        gridLayout->addWidget(txtParent1, 3, 1, 1, 1);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        gridLayout->addWidget(label_2, 4, 0, 1, 1);

        label_22 = new QLabel(gridLayoutWidget);
        label_22->setObjectName(QString::fromUtf8("label_22"));

        gridLayout->addWidget(label_22, 2, 0, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));

        gridLayout->addWidget(label, 3, 0, 1, 1);

        txtRepMut1 = new QLineEdit(gridLayoutWidget);
        txtRepMut1->setObjectName(QString::fromUtf8("txtRepMut1"));

        gridLayout->addWidget(txtRepMut1, 5, 1, 1, 1);

        label_23 = new QLabel(gridLayoutWidget);
        label_23->setObjectName(QString::fromUtf8("label_23"));

        gridLayout->addWidget(label_23, 0, 0, 1, 1);

        txtRepLow = new QLineEdit(gridLayoutWidget);
        txtRepLow->setObjectName(QString::fromUtf8("txtRepLow"));

        gridLayout->addWidget(txtRepLow, 0, 1, 1, 2);

        txtRepUp = new QLineEdit(gridLayoutWidget);
        txtRepUp->setObjectName(QString::fromUtf8("txtRepUp"));

        gridLayout->addWidget(txtRepUp, 1, 1, 1, 2);

        txtRepBits = new QLineEdit(gridLayoutWidget);
        txtRepBits->setObjectName(QString::fromUtf8("txtRepBits"));

        gridLayout->addWidget(txtRepBits, 2, 1, 1, 2);

        txtRepCross = new QLineEdit(gridLayoutWidget);
        txtRepCross->setObjectName(QString::fromUtf8("txtRepCross"));

        gridLayout->addWidget(txtRepCross, 4, 1, 1, 2);

        gridLayoutWidget_2 = new QWidget(centralwidget);
        gridLayoutWidget_2->setObjectName(QString::fromUtf8("gridLayoutWidget_2"));
        gridLayoutWidget_2->setGeometry(QRect(10, 10, 301, 370));
        gridLayout_2 = new QGridLayout(gridLayoutWidget_2);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        label_4 = new QLabel(gridLayoutWidget_2);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout_2->addWidget(label_4, 1, 0, 1, 1);

        txtUp = new QLineEdit(gridLayoutWidget_2);
        txtUp->setObjectName(QString::fromUtf8("txtUp"));

        gridLayout_2->addWidget(txtUp, 2, 1, 1, 1);

        cmbOrder = new QComboBox(gridLayoutWidget_2);
        cmbOrder->addItem(QString());
        cmbOrder->addItem(QString());
        cmbOrder->setObjectName(QString::fromUtf8("cmbOrder"));

        gridLayout_2->addWidget(cmbOrder, 8, 1, 1, 1);

        label_8 = new QLabel(gridLayoutWidget_2);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        gridLayout_2->addWidget(label_8, 4, 0, 1, 1);

        label_10 = new QLabel(gridLayoutWidget_2);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        gridLayout_2->addWidget(label_10, 6, 0, 1, 1);

        label_9 = new QLabel(gridLayoutWidget_2);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        gridLayout_2->addWidget(label_9, 5, 0, 1, 1);

        label_5 = new QLabel(gridLayoutWidget_2);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout_2->addWidget(label_5, 2, 0, 1, 1);

        txtRank = new QLineEdit(gridLayoutWidget_2);
        txtRank->setObjectName(QString::fromUtf8("txtRank"));

        gridLayout_2->addWidget(txtRank, 10, 1, 1, 1);

        label_6 = new QLabel(gridLayoutWidget_2);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        gridLayout_2->addWidget(label_6, 8, 0, 1, 1);

        txtMut = new QLineEdit(gridLayoutWidget_2);
        txtMut->setObjectName(QString::fromUtf8("txtMut"));

        gridLayout_2->addWidget(txtMut, 7, 1, 1, 1);

        txtBits = new QLineEdit(gridLayoutWidget_2);
        txtBits->setObjectName(QString::fromUtf8("txtBits"));

        gridLayout_2->addWidget(txtBits, 3, 1, 1, 1);

        txtGens = new QLineEdit(gridLayoutWidget_2);
        txtGens->setObjectName(QString::fromUtf8("txtGens"));

        gridLayout_2->addWidget(txtGens, 5, 1, 1, 1);

        txtPop = new QLineEdit(gridLayoutWidget_2);
        txtPop->setObjectName(QString::fromUtf8("txtPop"));

        gridLayout_2->addWidget(txtPop, 4, 1, 1, 1);

        label_7 = new QLabel(gridLayoutWidget_2);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        gridLayout_2->addWidget(label_7, 3, 0, 1, 1);

        label_11 = new QLabel(gridLayoutWidget_2);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        gridLayout_2->addWidget(label_11, 7, 0, 1, 1);

        label_3 = new QLabel(gridLayoutWidget_2);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        gridLayout_2->addWidget(label_3, 0, 0, 1, 1);

        txtCross = new QLineEdit(gridLayoutWidget_2);
        txtCross->setObjectName(QString::fromUtf8("txtCross"));

        gridLayout_2->addWidget(txtCross, 6, 1, 1, 1);

        txtLow = new QLineEdit(gridLayoutWidget_2);
        txtLow->setObjectName(QString::fromUtf8("txtLow"));

        gridLayout_2->addWidget(txtLow, 1, 1, 1, 1);

        label_12 = new QLabel(gridLayoutWidget_2);
        label_12->setObjectName(QString::fromUtf8("label_12"));

        gridLayout_2->addWidget(label_12, 9, 0, 1, 1);

        label_13 = new QLabel(gridLayoutWidget_2);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        gridLayout_2->addWidget(label_13, 10, 0, 1, 1);

        cmbMethod = new QComboBox(gridLayoutWidget_2);
        cmbMethod->addItem(QString());
        cmbMethod->addItem(QString());
        cmbMethod->setObjectName(QString::fromUtf8("cmbMethod"));

        gridLayout_2->addWidget(cmbMethod, 9, 1, 1, 1);

        txtFunction = new QLineEdit(gridLayoutWidget_2);
        txtFunction->setObjectName(QString::fromUtf8("txtFunction"));

        gridLayout_2->addWidget(txtFunction, 0, 1, 1, 1);

        btnSelection = new QPushButton(centralwidget);
        btnSelection->setObjectName(QString::fromUtf8("btnSelection"));
        btnSelection->setGeometry(QRect(370, 250, 151, 41));
        txtSelection = new QTextEdit(centralwidget);
        txtSelection->setObjectName(QString::fromUtf8("txtSelection"));
        txtSelection->setGeometry(QRect(350, 300, 201, 81));
        gridLayoutWidget_4 = new QWidget(centralwidget);
        gridLayoutWidget_4->setObjectName(QString::fromUtf8("gridLayoutWidget_4"));
        gridLayoutWidget_4->setGeometry(QRect(330, 10, 241, 234));
        gridLayout_4 = new QGridLayout(gridLayoutWidget_4);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        gridLayout_4->setContentsMargins(0, 0, 0, 0);
        label_21 = new QLabel(gridLayoutWidget_4);
        label_21->setObjectName(QString::fromUtf8("label_21"));

        gridLayout_4->addWidget(label_21, 2, 0, 1, 1);

        txtValues = new QLineEdit(gridLayoutWidget_4);
        txtValues->setObjectName(QString::fromUtf8("txtValues"));

        gridLayout_4->addWidget(txtValues, 0, 1, 1, 1);

        cmbSelOrder = new QComboBox(gridLayoutWidget_4);
        cmbSelOrder->addItem(QString());
        cmbSelOrder->addItem(QString());
        cmbSelOrder->setObjectName(QString::fromUtf8("cmbSelOrder"));

        gridLayout_4->addWidget(cmbSelOrder, 3, 1, 1, 1);

        label_20 = new QLabel(gridLayoutWidget_4);
        label_20->setObjectName(QString::fromUtf8("label_20"));

        gridLayout_4->addWidget(label_20, 1, 0, 1, 1);

        label_27 = new QLabel(gridLayoutWidget_4);
        label_27->setObjectName(QString::fromUtf8("label_27"));

        gridLayout_4->addWidget(label_27, 5, 0, 1, 1);

        label_25 = new QLabel(gridLayoutWidget_4);
        label_25->setObjectName(QString::fromUtf8("label_25"));

        gridLayout_4->addWidget(label_25, 4, 0, 1, 1);

        txtFitness = new QLineEdit(gridLayoutWidget_4);
        txtFitness->setObjectName(QString::fromUtf8("txtFitness"));

        gridLayout_4->addWidget(txtFitness, 1, 1, 1, 1);

        label_19 = new QLabel(gridLayoutWidget_4);
        label_19->setObjectName(QString::fromUtf8("label_19"));

        gridLayout_4->addWidget(label_19, 0, 0, 1, 1);

        label_26 = new QLabel(gridLayoutWidget_4);
        label_26->setObjectName(QString::fromUtf8("label_26"));

        gridLayout_4->addWidget(label_26, 3, 0, 1, 1);

        txtSelRank = new QLineEdit(gridLayoutWidget_4);
        txtSelRank->setObjectName(QString::fromUtf8("txtSelRank"));

        gridLayout_4->addWidget(txtSelRank, 5, 1, 1, 1);

        cmbSelMethod = new QComboBox(gridLayoutWidget_4);
        cmbSelMethod->addItem(QString());
        cmbSelMethod->addItem(QString());
        cmbSelMethod->setObjectName(QString::fromUtf8("cmbSelMethod"));

        gridLayout_4->addWidget(cmbSelMethod, 4, 1, 1, 1);

        txtRands = new QLineEdit(gridLayoutWidget_4);
        txtRands->setObjectName(QString::fromUtf8("txtRands"));

        gridLayout_4->addWidget(txtRands, 2, 1, 1, 1);

        label_28 = new QLabel(gridLayoutWidget_4);
        label_28->setObjectName(QString::fromUtf8("label_28"));

        gridLayout_4->addWidget(label_28, 6, 0, 1, 1);

        cmbSelRep = new QComboBox(gridLayoutWidget_4);
        cmbSelRep->addItem(QString());
        cmbSelRep->addItem(QString());
        cmbSelRep->setObjectName(QString::fromUtf8("cmbSelRep"));

        gridLayout_4->addWidget(cmbSelRep, 6, 1, 1, 1);

        btnReproduction = new QPushButton(centralwidget);
        btnReproduction->setObjectName(QString::fromUtf8("btnReproduction"));
        btnReproduction->setGeometry(QRect(650, 210, 151, 41));
        txtReproduction = new QTextEdit(centralwidget);
        txtReproduction->setObjectName(QString::fromUtf8("txtReproduction"));
        txtReproduction->setGeometry(QRect(630, 270, 201, 81));
        wGA->setCentralWidget(centralwidget);
        menubar = new QMenuBar(wGA);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 938, 25));
        wGA->setMenuBar(menubar);
        statusbar = new QStatusBar(wGA);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        wGA->setStatusBar(statusbar);

        retranslateUi(wGA);

        QMetaObject::connectSlotsByName(wGA);
    } // setupUi

    void retranslateUi(QMainWindow *wGA)
    {
        wGA->setWindowTitle(QCoreApplication::translate("wGA", "Genetic Algorithms", nullptr));
        btnCalculate->setText(QCoreApplication::translate("wGA", "Run GA", nullptr));
        btnBack->setText(QCoreApplication::translate("wGA", "Back", nullptr));
        label_24->setText(QCoreApplication::translate("wGA", "Upper Bound", nullptr));
        label_14->setText(QCoreApplication::translate("wGA", "Mutation Position", nullptr));
        label_2->setText(QCoreApplication::translate("wGA", "Crossover Point", nullptr));
        label_22->setText(QCoreApplication::translate("wGA", "Number of Bits", nullptr));
        label->setText(QCoreApplication::translate("wGA", "Parents", nullptr));
        label_23->setText(QCoreApplication::translate("wGA", "Lower Bound", nullptr));
        txtRepLow->setText(QCoreApplication::translate("wGA", "-1", nullptr));
        txtRepUp->setText(QCoreApplication::translate("wGA", "1", nullptr));
        label_4->setText(QCoreApplication::translate("wGA", "Lower Bound", nullptr));
        txtUp->setText(QCoreApplication::translate("wGA", "1", nullptr));
        cmbOrder->setItemText(0, QCoreApplication::translate("wGA", "Ascending", nullptr));
        cmbOrder->setItemText(1, QCoreApplication::translate("wGA", "Descending", nullptr));

        label_8->setText(QCoreApplication::translate("wGA", "Population Size", nullptr));
        label_10->setText(QCoreApplication::translate("wGA", "Crossover Rate", nullptr));
        label_9->setText(QCoreApplication::translate("wGA", "Generations", nullptr));
        label_5->setText(QCoreApplication::translate("wGA", "Upper Bound", nullptr));
        txtRank->setText(QCoreApplication::translate("wGA", "1.0", nullptr));
        label_6->setText(QCoreApplication::translate("wGA", "Order", nullptr));
        txtMut->setText(QCoreApplication::translate("wGA", "0.2", nullptr));
        txtBits->setText(QCoreApplication::translate("wGA", "6", nullptr));
        txtGens->setText(QCoreApplication::translate("wGA", "20", nullptr));
        txtPop->setText(QCoreApplication::translate("wGA", "10", nullptr));
        label_7->setText(QCoreApplication::translate("wGA", "Number of Bits", nullptr));
        label_11->setText(QCoreApplication::translate("wGA", "Mutation Rate", nullptr));
        label_3->setText(QCoreApplication::translate("wGA", "Fitness Function", nullptr));
        txtCross->setText(QCoreApplication::translate("wGA", "0.8", nullptr));
        txtLow->setText(QCoreApplication::translate("wGA", "-1", nullptr));
        label_12->setText(QCoreApplication::translate("wGA", "Method", nullptr));
        label_13->setText(QCoreApplication::translate("wGA", "Rank Power", nullptr));
        cmbMethod->setItemText(0, QCoreApplication::translate("wGA", "Rank based", nullptr));
        cmbMethod->setItemText(1, QCoreApplication::translate("wGA", "Fitness based", nullptr));

        btnSelection->setText(QCoreApplication::translate("wGA", "Test Selection", nullptr));
        label_21->setText(QCoreApplication::translate("wGA", "Rands", nullptr));
        txtValues->setText(QString());
        txtValues->setPlaceholderText(QCoreApplication::translate("wGA", "Comma separated", nullptr));
        cmbSelOrder->setItemText(0, QCoreApplication::translate("wGA", "Ascending", nullptr));
        cmbSelOrder->setItemText(1, QCoreApplication::translate("wGA", "Descending", nullptr));

        label_20->setText(QCoreApplication::translate("wGA", "Fitness", nullptr));
        label_27->setText(QCoreApplication::translate("wGA", "Rank Power", nullptr));
        label_25->setText(QCoreApplication::translate("wGA", "Method", nullptr));
        txtFitness->setText(QString());
        txtFitness->setPlaceholderText(QCoreApplication::translate("wGA", "Comma separated", nullptr));
        label_19->setText(QCoreApplication::translate("wGA", "Values", nullptr));
        label_26->setText(QCoreApplication::translate("wGA", "Order", nullptr));
        txtSelRank->setText(QCoreApplication::translate("wGA", "1.0", nullptr));
        cmbSelMethod->setItemText(0, QCoreApplication::translate("wGA", "Rank based", nullptr));
        cmbSelMethod->setItemText(1, QCoreApplication::translate("wGA", "Fitness based", nullptr));

        txtRands->setText(QString());
        label_28->setText(QCoreApplication::translate("wGA", "Replacement", nullptr));
        cmbSelRep->setItemText(0, QCoreApplication::translate("wGA", "Yes", nullptr));
        cmbSelRep->setItemText(1, QCoreApplication::translate("wGA", "No", nullptr));

        btnReproduction->setText(QCoreApplication::translate("wGA", "Test Reproduction", nullptr));
    } // retranslateUi

};

namespace Ui {
    class wGA: public Ui_wGA {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_GA_H

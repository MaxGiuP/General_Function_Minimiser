/********************************************************************************
** Form generated from reading UI file 'manufacturing.ui'
**
** Created by: Qt User Interface Compiler version 5.15.17
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MANUFACTURING_H
#define UI_MANUFACTURING_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
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

class Ui_wManufacturing
{
public:
    QWidget *centralwidget;
    QPushButton *btnCalculate;
    QPushButton *btnBack;
    QTextEdit *txtOutput;
    QCheckBox *cbPlot;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QLabel *label_3;
    QLabel *label_6;
    QLineEdit *txtFunction;
    QLineEdit *txtStep;
    QLabel *label_4;
    QLineEdit *txtMin;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *txtMax;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *wManufacturing)
    {
        if (wManufacturing->objectName().isEmpty())
            wManufacturing->setObjectName(QString::fromUtf8("wManufacturing"));
        wManufacturing->resize(464, 400);
        centralwidget = new QWidget(wManufacturing);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        btnCalculate = new QPushButton(centralwidget);
        btnCalculate->setObjectName(QString::fromUtf8("btnCalculate"));
        btnCalculate->setGeometry(QRect(270, 130, 151, 41));
        btnBack = new QPushButton(centralwidget);
        btnBack->setObjectName(QString::fromUtf8("btnBack"));
        btnBack->setGeometry(QRect(120, 140, 97, 26));
        txtOutput = new QTextEdit(centralwidget);
        txtOutput->setObjectName(QString::fromUtf8("txtOutput"));
        txtOutput->setGeometry(QRect(10, 190, 431, 141));
        cbPlot = new QCheckBox(centralwidget);
        cbPlot->setObjectName(QString::fromUtf8("cbPlot"));
        cbPlot->setGeometry(QRect(0, 140, 121, 24));
        gridLayoutWidget = new QWidget(centralwidget);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(0, 0, 451, 111));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_3, 2, 0, 1, 2);

        label_6 = new QLabel(gridLayoutWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_6, 1, 1, 1, 1);

        txtFunction = new QLineEdit(gridLayoutWidget);
        txtFunction->setObjectName(QString::fromUtf8("txtFunction"));

        gridLayout->addWidget(txtFunction, 0, 2, 1, 4);

        txtStep = new QLineEdit(gridLayoutWidget);
        txtStep->setObjectName(QString::fromUtf8("txtStep"));

        gridLayout->addWidget(txtStep, 2, 2, 1, 1);

        label_4 = new QLabel(gridLayoutWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 1, 3, 1, 1);

        txtMin = new QLineEdit(gridLayoutWidget);
        txtMin->setObjectName(QString::fromUtf8("txtMin"));

        gridLayout->addWidget(txtMin, 1, 2, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label, 0, 0, 1, 2);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        txtMax = new QLineEdit(gridLayoutWidget);
        txtMax->setObjectName(QString::fromUtf8("txtMax"));

        gridLayout->addWidget(txtMax, 1, 4, 1, 1);

        wManufacturing->setCentralWidget(centralwidget);
        menubar = new QMenuBar(wManufacturing);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 464, 23));
        wManufacturing->setMenuBar(menubar);
        statusbar = new QStatusBar(wManufacturing);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        wManufacturing->setStatusBar(statusbar);

        retranslateUi(wManufacturing);

        QMetaObject::connectSlotsByName(wManufacturing);
    } // setupUi

    void retranslateUi(QMainWindow *wManufacturing)
    {
        wManufacturing->setWindowTitle(QCoreApplication::translate("wManufacturing", "Manufacturing Question", nullptr));
        btnCalculate->setText(QCoreApplication::translate("wManufacturing", "Calculate", nullptr));
        btnBack->setText(QCoreApplication::translate("wManufacturing", "Back", nullptr));
        cbPlot->setText(QCoreApplication::translate("wManufacturing", "Plot function", nullptr));
        label_3->setText(QCoreApplication::translate("wManufacturing", "Step Size", nullptr));
        label_6->setText(QCoreApplication::translate("wManufacturing", "Min", nullptr));
        txtFunction->setPlaceholderText(QCoreApplication::translate("wManufacturing", "Python style input", nullptr));
        label_4->setText(QCoreApplication::translate("wManufacturing", "Max", nullptr));
        label->setText(QCoreApplication::translate("wManufacturing", "Function", nullptr));
        label_2->setText(QCoreApplication::translate("wManufacturing", "Starting Points", nullptr));
    } // retranslateUi

};

namespace Ui {
    class wManufacturing: public Ui_wManufacturing {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MANUFACTURING_H

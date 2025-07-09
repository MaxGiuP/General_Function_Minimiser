/********************************************************************************
** Form generated from reading UI file 'linear.ui'
**
** Created by: Qt User Interface Compiler version 5.15.17
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_LINEAR_H
#define UI_LINEAR_H

#include <QtCore/QVariant>

//#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_wLinear
{
public:
    QWidget *centralwidget;
    QPushButton *btnCalculate;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QRadioButton *rbGolden;
    QRadioButton *rbInverse;
    QRadioButton *rbNewton;
    QTextEdit *txtOutput;
    QCheckBox *cbPlot;
    QWidget *gridLayoutWidget;
    QGridLayout *gridLayout;
    QLineEdit *txtx1;
    QLabel *label_2;
    QLabel *label_5;
    QLabel *label_4;
    QLineEdit *txtFunction;
    QLineEdit *txtx3;
    QLineEdit *txtx2;
    QLineEdit *txtIterations;
    QLabel *label_6;
    QLabel *label;
    QLabel *label_3;
    QPushButton *btnBack;
    QPushButton *btnCalculate_2;
    QPushButton *btnBack_2;
    QMenuBar *menubar;
    QMenu *menuLinear_Search;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *wLinear)
    {
        if (wLinear->objectName().isEmpty())
            wLinear->setObjectName(QString::fromUtf8("wLinear"));
        wLinear->resize(724, 403);
        centralwidget = new QWidget(wLinear);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        btnCalculate = new QPushButton(centralwidget);
        btnCalculate->setObjectName(QString::fromUtf8("btnCalculate"));
        btnCalculate->setGeometry(QRect(320, 280, 151, 41));
        verticalLayoutWidget = new QWidget(centralwidget);
        verticalLayoutWidget->setObjectName(QString::fromUtf8("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(10, 120, 244, 86));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        rbGolden = new QRadioButton(verticalLayoutWidget);
        rbGolden->setObjectName(QString::fromUtf8("rbGolden"));
        rbGolden->setChecked(true);

        verticalLayout->addWidget(rbGolden);

        rbInverse = new QRadioButton(verticalLayoutWidget);
        rbInverse->setObjectName(QString::fromUtf8("rbInverse"));

        verticalLayout->addWidget(rbInverse);

        rbNewton = new QRadioButton(verticalLayoutWidget);
        rbNewton->setObjectName(QString::fromUtf8("rbNewton"));

        verticalLayout->addWidget(rbNewton);

        txtOutput = new QTextEdit(centralwidget);
        txtOutput->setObjectName(QString::fromUtf8("txtOutput"));
        txtOutput->setGeometry(QRect(250, 120, 371, 141));
        cbPlot = new QCheckBox(centralwidget);
        cbPlot->setObjectName(QString::fromUtf8("cbPlot"));
        cbPlot->setGeometry(QRect(20, 210, 121, 24));
        gridLayoutWidget = new QWidget(centralwidget);
        gridLayoutWidget->setObjectName(QString::fromUtf8("gridLayoutWidget"));
        gridLayoutWidget->setGeometry(QRect(10, 10, 451, 111));
        gridLayout = new QGridLayout(gridLayoutWidget);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        gridLayout->setContentsMargins(0, 0, 0, 0);
        txtx1 = new QLineEdit(gridLayoutWidget);
        txtx1->setObjectName(QString::fromUtf8("txtx1"));

        gridLayout->addWidget(txtx1, 1, 2, 1, 1);

        label_2 = new QLabel(gridLayoutWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_2, 1, 0, 1, 1);

        label_5 = new QLabel(gridLayoutWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        gridLayout->addWidget(label_5, 1, 5, 1, 1);

        label_4 = new QLabel(gridLayoutWidget);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        gridLayout->addWidget(label_4, 1, 3, 1, 1);

        txtFunction = new QLineEdit(gridLayoutWidget);
        txtFunction->setObjectName(QString::fromUtf8("txtFunction"));

        gridLayout->addWidget(txtFunction, 0, 2, 1, 5);

        txtx3 = new QLineEdit(gridLayoutWidget);
        txtx3->setObjectName(QString::fromUtf8("txtx3"));

        gridLayout->addWidget(txtx3, 1, 6, 1, 1);

        txtx2 = new QLineEdit(gridLayoutWidget);
        txtx2->setObjectName(QString::fromUtf8("txtx2"));

        gridLayout->addWidget(txtx2, 1, 4, 1, 1);

        txtIterations = new QLineEdit(gridLayoutWidget);
        txtIterations->setObjectName(QString::fromUtf8("txtIterations"));

        gridLayout->addWidget(txtIterations, 2, 2, 1, 1);

        label_6 = new QLabel(gridLayoutWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_6, 1, 1, 1, 1);

        label = new QLabel(gridLayoutWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label, 0, 0, 1, 2);

        label_3 = new QLabel(gridLayoutWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setAlignment(Qt::AlignmentFlag::AlignRight|Qt::AlignmentFlag::AlignTrailing|Qt::AlignmentFlag::AlignVCenter);

        gridLayout->addWidget(label_3, 2, 0, 1, 2);

        btnBack = new QPushButton(centralwidget);
        btnBack->setObjectName(QString::fromUtf8("btnBack"));
        btnBack->setGeometry(QRect(40, 280, 97, 26));
        btnCalculate_2 = new QPushButton(centralwidget);
        btnCalculate_2->setObjectName(QString::fromUtf8("btnCalculate_2"));
        btnCalculate_2->setGeometry(QRect(460, 380, 151, 41));
        btnBack_2 = new QPushButton(centralwidget);
        btnBack_2->setObjectName(QString::fromUtf8("btnBack_2"));
        btnBack_2->setGeometry(QRect(180, 380, 97, 26));
        wLinear->setCentralWidget(centralwidget);
        menubar = new QMenuBar(wLinear);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 724, 23));
        menuLinear_Search = new QMenu(menubar);
        menuLinear_Search->setObjectName(QString::fromUtf8("menuLinear_Search"));
        wLinear->setMenuBar(menubar);
        statusbar = new QStatusBar(wLinear);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        wLinear->setStatusBar(statusbar);

        menubar->addAction(menuLinear_Search->menuAction());

        retranslateUi(wLinear);

        QMetaObject::connectSlotsByName(wLinear);
    } // setupUi

    void retranslateUi(QMainWindow *wLinear)
    {
        wLinear->setWindowTitle(QCoreApplication::translate("wLinear", "Linear Search", nullptr));
        btnCalculate->setText(QCoreApplication::translate("wLinear", "Calculate", nullptr));
        rbGolden->setText(QCoreApplication::translate("wLinear", "Golden Search", nullptr));
        rbInverse->setText(QCoreApplication::translate("wLinear", "Inverse Parabolic Interpolation", nullptr));
        rbNewton->setText(QCoreApplication::translate("wLinear", "Netwon's Method", nullptr));
        cbPlot->setText(QCoreApplication::translate("wLinear", "Plot function", nullptr));
        label_2->setText(QCoreApplication::translate("wLinear", "Starting Points", nullptr));
        label_5->setText(QCoreApplication::translate("wLinear", "x3", nullptr));
        label_4->setText(QCoreApplication::translate("wLinear", "x2", nullptr));
        txtFunction->setPlaceholderText(QCoreApplication::translate("wLinear", "Write in Python style", nullptr));
        txtIterations->setText(QCoreApplication::translate("wLinear", "1", nullptr));
        label_6->setText(QCoreApplication::translate("wLinear", "x1", nullptr));
        label->setText(QCoreApplication::translate("wLinear", "Function", nullptr));
        label_3->setText(QCoreApplication::translate("wLinear", "Number of Iterations", nullptr));
        btnBack->setText(QCoreApplication::translate("wLinear", "Back", nullptr));
        btnCalculate_2->setText(QCoreApplication::translate("wLinear", "Calculate", nullptr));
        btnBack_2->setText(QCoreApplication::translate("wLinear", "Back", nullptr));
        menuLinear_Search->setTitle(QString());
    } // retranslateUi

};

namespace Ui {
    class wLinear: public Ui_wLinear {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_LINEAR_H

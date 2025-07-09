/********************************************************************************
** Form generated from reading UI file 'menu.ui'
**
** Created by: Qt User Interface Compiler version 6.9.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MENU_H
#define UI_MENU_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_wMenu
{
public:
    QWidget *centralwidget;
    QPushButton *btnLinear;
    QPushButton *btnMultiVariable;
    QPushButton *btnGA;
    QPushButton *btnConstrained;
    QPushButton *btnMultiObjective;
    QPushButton *btnWing;
    QPushButton *btnManufacturing;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *wMenu)
    {
        if (wMenu->objectName().isEmpty())
            wMenu->setObjectName("wMenu");
        wMenu->resize(460, 459);
        centralwidget = new QWidget(wMenu);
        centralwidget->setObjectName("centralwidget");
        btnLinear = new QPushButton(centralwidget);
        btnLinear->setObjectName("btnLinear");
        btnLinear->setGeometry(QRect(10, 10, 141, 71));
        btnMultiVariable = new QPushButton(centralwidget);
        btnMultiVariable->setObjectName("btnMultiVariable");
        btnMultiVariable->setGeometry(QRect(160, 10, 141, 71));
        btnGA = new QPushButton(centralwidget);
        btnGA->setObjectName("btnGA");
        btnGA->setGeometry(QRect(310, 10, 141, 71));
        btnConstrained = new QPushButton(centralwidget);
        btnConstrained->setObjectName("btnConstrained");
        btnConstrained->setGeometry(QRect(10, 120, 141, 71));
        btnMultiObjective = new QPushButton(centralwidget);
        btnMultiObjective->setObjectName("btnMultiObjective");
        btnMultiObjective->setGeometry(QRect(160, 120, 141, 71));
        btnWing = new QPushButton(centralwidget);
        btnWing->setObjectName("btnWing");
        btnWing->setGeometry(QRect(130, 250, 181, 71));
        btnManufacturing = new QPushButton(centralwidget);
        btnManufacturing->setObjectName("btnManufacturing");
        btnManufacturing->setGeometry(QRect(130, 330, 181, 71));
        wMenu->setCentralWidget(centralwidget);
        menubar = new QMenuBar(wMenu);
        menubar->setObjectName("menubar");
        menubar->setGeometry(QRect(0, 0, 460, 23));
        wMenu->setMenuBar(menubar);
        statusbar = new QStatusBar(wMenu);
        statusbar->setObjectName("statusbar");
        wMenu->setStatusBar(statusbar);

        retranslateUi(wMenu);

        QMetaObject::connectSlotsByName(wMenu);
    } // setupUi

    void retranslateUi(QMainWindow *wMenu)
    {
        wMenu->setWindowTitle(QCoreApplication::translate("wMenu", "Menu", nullptr));
        btnLinear->setText(QCoreApplication::translate("wMenu", "Linear", nullptr));
        btnMultiVariable->setText(QCoreApplication::translate("wMenu", "Multi-Variable", nullptr));
        btnGA->setText(QCoreApplication::translate("wMenu", "Genetic Algorithm", nullptr));
        btnConstrained->setText(QCoreApplication::translate("wMenu", "Constrained", nullptr));
        btnMultiObjective->setText(QCoreApplication::translate("wMenu", "Multi-Objective", nullptr));
        btnWing->setText(QCoreApplication::translate("wMenu", "Wing Question", nullptr));
        btnManufacturing->setText(QCoreApplication::translate("wMenu", "Manufacturing Question", nullptr));
    } // retranslateUi

};

namespace Ui {
    class wMenu: public Ui_wMenu {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MENU_H

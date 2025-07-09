#include "menu.h"
#include "linear.h"
#include "multivariable.h"
#include "ga.h"
#include "constrained.h"
#include "multiobjective.h"
#include "wing.h"
#include "manufacturing.h"

#include <QDebug>

Menu::Menu(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::wMenu)
{
    ui->setupUi(this);
    connect(ui->btnLinear,         &QPushButton::clicked, this, &Menu::btnLinear_clicked);
    connect(ui->btnMultiVariable,  &QPushButton::clicked, this, &Menu::btnMultiVariable_clicked);
    connect(ui->btnGA,             &QPushButton::clicked, this, &Menu::btnGA_clicked);
    connect(ui->btnConstrained,    &QPushButton::clicked, this, &Menu::btnConstrained_clicked);
    connect(ui->btnMultiObjective, &QPushButton::clicked, this, &Menu::btnMultiObjective_clicked);
    connect(ui->btnWing,           &QPushButton::clicked, this, &Menu::btnWing_clicked);
    connect(ui->btnManufacturing,  &QPushButton::clicked, this, &Menu::btnManufacturing_clicked);
}

Menu::~Menu()
{
    delete ui;
}

void Menu::btnLinear_clicked() {
    qDebug() << "Show Linear";
    hide();
    LinearWindow *w = new LinearWindow(this);
    w->show();
}

void Menu::btnMultiVariable_clicked() {
    qDebug() << "Show Multi-Variable";
    hide();
    MultiVariableWindow *w = new MultiVariableWindow(this);
    w->show();
}

void Menu::btnGA_clicked() {
    qDebug() << "Show GA";
    hide();
    GAWindow *w = new GAWindow(this);
    w->show();
}

void Menu::btnConstrained_clicked() {
    qDebug() << "Show Constrained";
    hide();
    ConstrainedWindow *w = new ConstrainedWindow(this);
    w->show();
}

void Menu::btnMultiObjective_clicked() {
    qDebug() << "Show Multi-Objective";
    hide();
    MultiObjectiveWindow *w = new MultiObjectiveWindow(this);
    w->show();
}

void Menu::btnWing_clicked() {
    qDebug() << "Show Wing";
    hide();
    WingWindow *w = new WingWindow(this);
    w->show();
}

void Menu::btnManufacturing_clicked() {
    qDebug() << "Show Manufacturing";
    hide();
    ManufacturingWindow *w = new ManufacturingWindow(this);
    w->show();
}

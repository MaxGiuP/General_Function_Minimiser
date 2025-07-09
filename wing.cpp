// wing.cpp
#include "wing.h"
#include "menu.h"
#include "python_utils.h"
#include <QDebug>

WingWindow::WingWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::wWing)
{
    ui->setupUi(this);
    connect(ui->btnCalculate, &QPushButton::clicked,
            this, &WingWindow::btnCalculate_clicked);
    connect(ui->btnBack,      &QPushButton::clicked,
            this, &WingWindow::btnBack_clicked);
    qDebug() << "WingWindow initialized";
}

WingWindow::~WingWindow()
{
    delete ui;
}

void WingWindow::btnCalculate_clicked()
{
    qDebug() << "Calculate clicked";

    //bool showPlot = ui->cbPlot->isChecked();
    QString cl_coeff            = ui->txtCLCoeff->text();
    QString cl_offset           = ui->txtCLOff->text();
    QString cd_const            = ui->txtCDConst->text();
    QString cd_quad             = ui->txtCDQuad->text();
    QString initial_guess_alpha = ui->txtAlphaGuess->text();
    QString stall_limit         = ui->txtStallLimit->text();
    QString V_cruise            = ui->txtCruise->text();
    QString V_landing           = ui->txtLanding->text();

    QStringList args = {
        cl_coeff,
        cl_offset,
        cd_const,
        cd_quad,
        initial_guess_alpha,
        stall_limit,
        V_cruise,
        V_landing,
        //showPlot ? "1" : "0"
    };

    // Call the Python function:
    // Note: assumes a Python wrapper so that
    // module “Optimisers.WingQuestion.WingQuestion”
    // exposes optimise_wing(...)
    QString result = callPythonFunction(
        "Optimisers.WingQuestion.WingQuestion",
        "optimise_wing",
        args
        );

    qDebug() << "Python returned:" << result;
    ui->txtOutput->setText(result);
}

void WingWindow::btnBack_clicked()
{
    qDebug() << "Back clicked";
    hide();
    Menu *m = new Menu(this);
    m->show();
}

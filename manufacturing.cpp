// manufacturing.cpp
#include "manufacturing.h"
#include "menu.h"
#include "python_utils.h"       // our helper for calling into Python
#include <QDebug>

ManufacturingWindow::ManufacturingWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::wManufacturing)
{
    ui->setupUi(this);  // build the widgets :contentReference[oaicite:2]{index=2}
    connect(ui->btnCalculate, &QPushButton::clicked,
            this, &ManufacturingWindow::btnCalculate_clicked);
    connect(ui->btnBack,      &QPushButton::clicked,
            this, &ManufacturingWindow::btnBack_clicked);
    qDebug() << "ManufacturingWindow initialized";
}

ManufacturingWindow::~ManufacturingWindow()
{
    delete ui;
}

void ManufacturingWindow::btnCalculate_clicked()
{
    qDebug() << "Calculate clicked";
    bool showPlot = ui->cbPlot->isChecked();
    QString fn    = ui->txtFunction->text();
    QString minV  = ui->txtMin->text();
    QString maxV  = ui->txtMax->text();
    QString step  = ui->txtStep->text();

    // Call the Python function ManuPerf.manufacturing(...)
    QStringList args = { fn, minV, maxV, step, showPlot ? "1" : "0" };
    QString result = callPythonFunction(
        "Optimisers.ManufacturingQuestion",  // module
        "manufacturing",                      // function name
        args
        );

    ui->txtOutput->setText(result);
}

void ManufacturingWindow::btnBack_clicked()
{
    qDebug() << "Back clicked";
    hide();
    Menu *m = new Menu(this);
    m->show();
}

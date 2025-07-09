// constrained.cpp
#include "constrained.h"
#include "menu.h"
#include "python_utils.h"
#include <QDebug>

ConstrainedWindow::ConstrainedWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::wConstrained)
{
    ui->setupUi(this);
    connect(ui->btnCalculate, &QPushButton::clicked,
            this, &ConstrainedWindow::btnCalculate_clicked);
    connect(ui->btnBack,      &QPushButton::clicked,
            this, &ConstrainedWindow::btnBack_clicked);
    qDebug() << "ConstrainedWindow initialized";
}

ConstrainedWindow::~ConstrainedWindow()
{
    delete ui;
}

void ConstrainedWindow::btnCalculate_clicked()
{
    qDebug() << "Calculate clicked";
    bool showPlot = ui->cbPlot->isChecked();
    QString fn   = ui->txtFunction->text();
    QStringList eq   = ui->txtEq->toPlainText().split('\n', Qt::SkipEmptyParts);
    QStringList ineq = ui->txtIneq->toPlainText().split('\n', Qt::SkipEmptyParts);

    // Common params
    double R          = 0.01;
    QString method    = "BFGS";
    QString start     = QStringList{"1","1"}.join(";");
    int scale         = 10;
    int maxRound      = 6;
    double tol        = 1e-6;

    // Decide module/function
    QString module, function;
    QStringList args;
    if (ui->rbLagrange->isChecked()) {
        module   = "Optimisers.Constrained.ConstrainedLagrange";
        function = "lagrange";
        args     = { fn, eq.join(";"), ineq.join(";"), showPlot ? "1" : "0" };
    }
    else if (ui->rbFixedPenaltyAny->isChecked()) {
        module   = "Optimisers.Constrained.ConstrainedPenaltyFixedAny";
        function = "fixed_penalty";
        args     = { fn, eq.join(";"), ineq.join(";"),
                QString::number(R), start, method, showPlot ? "1" : "0" };
    }
    else if (ui->rbFixedPenaltyEach->isChecked()) {
        module   = "Optimisers.Constrained.ConstrainedPenaltyFixedEach";
        function = "fixed_penalty";
        args     = { fn, eq.join(";"), ineq.join(";"),
                QString::number(R), start, method, showPlot ? "1" : "0" };
    }
    else if (ui->rbVaryingSL->isChecked()) {
        module   = "Optimisers.Constrained.ConstrainedPenaltyVaryingSL";
        function = "varying_sl";
        args     = { fn, eq.join(";"), ineq.join(";"),
                QString::number(R), QString::number(scale),
                QString::number(maxRound), QString::number(tol),
                start, method, showPlot ? "1" : "0" };
    }
    else if (ui->rbVaryingDoC->isChecked()) {
        module   = "Optimisers.Constrained.ConstrainedPenaltyVaryingDoC";
        function = "varying_doc";
        args     = { fn, eq.join(";"), ineq.join(";"),
                QString::number(R), start, method, showPlot ? "1" : "0" };
    }
    else if (ui->rbAugmented->isChecked()) {
        module   = "Optimisers.Constrained.ConstrainedAugmented";
        function = "augmented";
        args     = { fn, eq.join(";"), ineq.join(";") };
    }

    // Call into Python and display
    QString result = callPythonFunction(module, function, args);
    qDebug() << "Python returned:" << result;
    ui->txtOutput->setText(result);
}

void ConstrainedWindow::btnBack_clicked()
{
    qDebug() << "Back clicked";
    hide();
    Menu *m = new Menu(this);
    m->show();
}

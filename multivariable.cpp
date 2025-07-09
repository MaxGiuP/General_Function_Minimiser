// multivariable.cpp
#include "multivariable.h"
#include "menu.h"
#include "python_utils.h"
#include <QDebug>

MultiVariableWindow::MultiVariableWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::wMultiVariable)
{
    ui->setupUi(this);
    connect(ui->btnCalculate, &QPushButton::clicked,
            this, &MultiVariableWindow::btnCalculate_clicked);
    connect(ui->btnBack,      &QPushButton::clicked,
            this, &MultiVariableWindow::btnBack_clicked);
    qDebug() << "MultiVariableWindow initialized";
}

MultiVariableWindow::~MultiVariableWindow()
{
    delete ui;
}

void MultiVariableWindow::btnCalculate_clicked()
{
    qDebug() << "Calculate clicked";

    bool showPlot      = ui->cbPlot->isChecked();
    QString fn         = ui->txtFunction->text();
    int iterations     = ui->txtIterations->text().toInt();
    double x           = ui->txtx->text().toDouble();
    double y           = ui->txty->text().toDouble();
    double h           = ui->txth->text().toDouble();

    // Prepare the "start" argument as "x;y"
    QString start = QStringList{ QString::number(x), QString::number(y) }
                        .join(";");

    QString module;
    QString function;
    QStringList args;

    if (ui->rbSteepest->isChecked()) {
        module   = "Optimisers.MultiVariable.SteepestDescent";
        function = "steepest_descent";
        args     = { fn, start,
                QString::number(iterations),
                showPlot ? "1" : "0" };
    }
    else if (ui->rbConjugate->isChecked()) {
        module   = "Optimisers.MultiVariable.ConjugateGradient";
        function = "conjugate_gradient";
        args     = { fn, start,
                QString::number(iterations),
                showPlot ? "1" : "0" };
    }
    else if (ui->rbNewton->isChecked()) {
        module   = "Optimisers.MultiVariable.NewtonsMethodMulti";
        function = "newton_multivariate";
        args     = { fn, start,
                QString::number(iterations),
                showPlot ? "1" : "0" };
    }
    else if (ui->rbBFGS->isChecked()) {
        module   = "Optimisers.MultiVariable.BFGS";
        function = "bfgs";
        args     = { fn, start,
                QString::number(iterations),
                showPlot ? "1" : "0" };
    }
    else if (ui->rbHJ->isChecked()) {
        module   = "Optimisers.MultiVariable.HookeandJeeves";
        function = "hooke_jeeves";
        args     = { fn, start,
                QString::number(h),
                QString::number(iterations),
                showPlot ? "1" : "0" };
    }

    // Call the Python backend
    QString result = callPythonFunction(module, function, args);
    qDebug() << "Python returned:" << result;
    ui->txtOutput->setText(result);
}

void MultiVariableWindow::btnBack_clicked()
{
    qDebug() << "Back clicked";
    hide();
    Menu *m = new Menu(this);
    m->show();
}

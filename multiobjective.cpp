// multiobjective.cpp
#include "multiobjective.h"
#include "menu.h"
#include "python_utils.h"
#include <QDebug>

MultiObjectiveWindow::MultiObjectiveWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::wMultiObjective)
{
    ui->setupUi(this);
    connect(ui->btnCalculate, &QPushButton::clicked,
            this, &MultiObjectiveWindow::btnCalculate_clicked);
    connect(ui->btnBack, &QPushButton::clicked,
            this, &MultiObjectiveWindow::btnBack_clicked);
    qDebug() << "MultiObjectiveWindow initialized";
}

MultiObjectiveWindow::~MultiObjectiveWindow()
{
    delete ui;
}

void MultiObjectiveWindow::btnCalculate_clicked()
{
    qDebug() << "Calculate clicked";
    bool showPlot = ui->cbPlot->isChecked();

    // Gather functions
    QStringList functions = ui->txtFunctions
                                ->toPlainText()
                                .split('\n', Qt::SkipEmptyParts);

    // Gather thresholds
    QStringList left  = ui->txtLeft
                           ->toPlainText()
                           .split('\n', Qt::SkipEmptyParts);
    QStringList right = ui->txtRight
                            ->toPlainText()
                            .split('\n', Qt::SkipEmptyParts);

    QStringList args;
    QString module, function;

    if (ui->rbEigenvectors->isChecked()) {
        module   = "Optimisers.MultiObjective.EigenvectorMethod";
        function = "eigenvector_weights";
        // single arg: functions
        args << functions.join(";");
    }
    else if (ui->rbFuzzyLogic->isChecked()) {
        module   = "Optimisers.MultiObjective.FuzzyLogic";
        function = "fuzzy";
        // args: functions, thresholds as "l1,r1;l2,r2;..."
        QStringList thr;
        for (int i = 0; i < qMin(left.size(), right.size()); ++i)
            thr << left[i] + "," + right[i];
        args << functions.join(";")
             << thr.join(";");
    }
    else if (ui->rbPareto->isChecked()) {
        module   = "Optimisers.MultiObjective.ParetoDominance";
        function = "pareto_front";
        args << functions.join(";")
             << (showPlot ? "1" : "0");
    }
    else if (ui->rbParetoTable->isChecked()) {
        module   = "Optimisers.MultiObjective.ParetoDominanceTable";
        function = "pareto_analysis";
        // build x_values from left only
        QStringList xvals = left;
        // samples = 1..xvals.size()
        QStringList samples;
        for (int i = 1; i <= xvals.size(); ++i)
            samples << QString::number(i);
        args << functions.join(";")
             << xvals.join(";")
             << samples.join(";")
             << (showPlot ? "1" : "0");
    }

    // Call into Python
    QString result = callPythonFunction(module, function, args);
    qDebug() << "Python returned:" << result;
    ui->txtOutput->setText(result);
}

void MultiObjectiveWindow::btnBack_clicked()
{
    qDebug() << "Back clicked";
    hide();
    Menu *m = new Menu(this);
    m->show();
}

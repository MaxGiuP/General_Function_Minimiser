// ga.cpp
#include "ga.h"
#include "menu.h"
#include "python_utils.h"
#include <QDebug>

GAWindow::GAWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::wGA)
{
    ui->setupUi(this);

    connect(ui->btnCalculate, &QPushButton::clicked,
            this, &GAWindow::btnCalculate_clicked);
    connect(ui->btnSelection, &QPushButton::clicked,
            this, &GAWindow::btnSelection_clicked);
    connect(ui->btnReproduction, &QPushButton::clicked,
            this, &GAWindow::btnReproduction_clicked);
    connect(ui->btnBack, &QPushButton::clicked,
            this, &GAWindow::btnBack_clicked);

    qDebug() << "GAWindow Initialised";
}

GAWindow::~GAWindow()
{
    delete ui;
}

void GAWindow::btnCalculate_clicked()
{
    qDebug() << "Run GA clicked";

    // Gather inputs
    QString fitness_fn     = ui->txtFunction->text();
    double lower           = ui->txtLow->text().toDouble();
    double upper           = ui->txtUp->text().toDouble();
    int bits               = ui->txtBits->text().toInt();
    int pop_size           = ui->txtPop->text().toInt();
    int generations        = ui->txtGens->text().toInt();
    double crossover_rate  = ui->txtCross->text().toDouble();
    double mutation_rate   = ui->txtMut->text().toDouble();
    QString order          = ui->cmbOrder->currentText();
    QString method         = ui->cmbMethod->currentText();
    double rank_power      = ui->txtRank->text().toDouble();

    // Build argument list
    QStringList args = {
        fitness_fn,
        QString::number(lower),
        QString::number(upper),
        QString::number(bits),
        QString::number(pop_size),
        QString::number(generations),
        QString::number(crossover_rate),
        QString::number(mutation_rate),
        order,
        method,
        QString::number(rank_power)
    };

    // Call a top-level Python function run_ga defined in GA_Combined.py
    QString result = callPythonFunction(
        "Optimisers.GeneticAlgorithms.GA_Combined",
        "run_ga",
        args
        );

    ui->txtOutput->setText(result);
}

void GAWindow::btnSelection_clicked()
{
    qDebug() << "Selection clicked";

    // Gather inputs
    QStringList values = ui->txtValues->text()
                             .split(",", Qt::SkipEmptyParts);
    QStringList fitness = ui->txtFitness->text()
                              .split(",", Qt::SkipEmptyParts);
    QStringList rands   = ui->txtRands->text()
                            .split(",", Qt::SkipEmptyParts);
    QString order       = ui->cmbSelOrder->currentText();
    QString method      = ui->cmbSelMethod->currentText();
    bool replacement    = (ui->cmbSelRep->currentText() == "Yes");
    double rank_power   = ui->txtSelRank->text().toDouble();

    // Build args
    QStringList args = {
        values.join(";"),
        fitness.join(";"),
        rands.join(";"),
        order,
        method,
        QString::number(rank_power),
        replacement ? "1" : "0"
    };

    QString pool = callPythonFunction(
        "Optimisers.GeneticAlgorithms.GA_Combined",
        "roulette_selection_indices",
        args
        );

    ui->txtSelection->setText("Roulette Pool: " + pool);
}

void GAWindow::btnReproduction_clicked()
{
    qDebug() << "Reproduction clicked";

    // Gather inputs
    double lower           = ui->txtRepLow->text().toDouble();
    double upper           = ui->txtRepUp->text().toDouble();
    int bits               = ui->txtBits->text().toInt();
    int crossover_point    = int(ui->txtRepCross->text().toDouble() * (bits - 1)) + 1;

    QList<double> parents = {
        ui->txtParent1->text().toDouble(),
        ui->txtParent2->text().toDouble()
    };

    QStringList args = {
        QString::number(lower),
        QString::number(upper),
        QString::number(bits),
        QString::number(crossover_point),
        // mutation positions as semicolon-separated:
        ui->txtRepMut1->text() + ";" + ui->txtRepMut2->text(),
        // parents as semicolon-separated:
        QString::number(parents[0]) + ";" + QString::number(parents[1])
    };

    QString children = callPythonFunction(
        "Optimisers.GeneticAlgorithms.GA_Combined",
        "reproduce_parametric",
        args
        );

    ui->txtReproduction->setText("Children:\n" + children);
}

void GAWindow::btnBack_clicked()
{
    qDebug() << "Back clicked";
    hide();
    Menu *m = new Menu(this);
    m->show();
}

#include "constrainedwindow.h"
#include <QDebug>

ConstrainedWindow::ConstrainedWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::wConstrained)
    , mainWindow(nullptr)
{
    ui->setupUi(this);

    connect(ui->btnCalculate, &QPushButton::clicked,
            this, &ConstrainedWindow::btnCalculate_clicked);
    connect(ui->btnBack, &QPushButton::clicked,
            this, &ConstrainedWindow::btnBack_clicked);

    qDebug() << "ConstrainedWindow Initialised";
}

ConstrainedWindow::~ConstrainedWindow()
{
    delete ui;
    // if mainWindow was created, it will be reparented and deleted by Qt
}

void ConstrainedWindow::btnCalculate_clicked()
{
    qDebug() << "Calculate clicked";

    bool showPlot = ui->cbPlot->isChecked();
    QString functionText = ui->txtFunction->text();
    QStringList equalities   = ui->txtEq->toPlainText().split('\n', Qt::SkipEmptyParts);
    QStringList inequalities = ui->txtIneq->toPlainText().split('\n', Qt::SkipEmptyParts);

    // Default parameters
    QVector<double> start{1.0, 1.0};
    double R      = 0.01;
    QString method = "BFGS";
    int scale     = 10;
    int max_round = 6;
    double tol    = 1e-6;

    QString result;

    if (ui->rbLagrange->isChecked()) {
        qDebug() << "Starting Lagrange";
        result = ConstrainedLagrange::lagrange(
            functionText, equalities, inequalities, showPlot);
        qDebug() << "End Lagrange";
    }
    else if (ui->rbFixedPenaltyAny->isChecked()) {
        qDebug() << "Starting fixed penalty ANY";
        result = ConstrainedPenaltyFixedAny::fixed_penalty(
            functionText, equalities, inequalities,
            R, start, method, showPlot);
        qDebug() << "Finished fixed penalty ANY";
    }
    else if (ui->rbFixedPenaltyEach->isChecked()) {
        qDebug() << "Starting fixed penalty EACH";
        result = ConstrainedPenaltyFixedEach::fixed_penalty(
            functionText, equalities, inequalities,
            R, start, method, showPlot);
        qDebug() << "Finished fixed penalty EACH";
    }
    else if (ui->rbVaryingSL->isChecked()) {
        qDebug() << "Starting Varying SL";
        result = ConstrainedPenaltyVaryingSL::varying_sl(
            functionText, equalities, inequalities,
            R, scale, max_round, tol,
            start, method, showPlot);
        qDebug() << "Finished Varying SL";
    }
    else if (ui->rbVaryingDoC->isChecked()) {
        qDebug() << "Starting Varying DoC";
        result = ConstrainedPenaltyVaryingDoC::varying_doc(
            functionText, equalities, inequalities,
            R, start, method, showPlot);
        qDebug() << "Finished Varying DoC";
    }
    else if (ui->rbAugmented->isChecked()) {
        qDebug() << "Starting Augmented";
        result = ConstrainedAugmented::augmented(
            functionText, equalities, inequalities);
        qDebug() << "Finished Augmented";
    }

    ui->txtOutput->setText(result);
}

void ConstrainedWindow::btnBack_clicked()
{
    qDebug() << "Back clicked";
    this->hide();
    mainWindow = new MainWindow(this);
    mainWindow->show();
}

#include "linear.h"
#include "python_utils.h"
#include "menu.h"

#include <QDebug>

LinearWindow::LinearWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::wLinear)
{
    ui->setupUi(this);
    connect(ui->btnCalculate, &QPushButton::clicked,
            this, &LinearWindow::btnCalculate_clicked);
    connect(ui->btnBack, &QPushButton::clicked,
            this, &LinearWindow::btnBack_clicked);
}

LinearWindow::~LinearWindow()
{
    delete ui;
}

void LinearWindow::btnCalculate_clicked()
{
    bool showPlot = ui->cbPlot->isChecked();
    QString fn = ui->txtFunction->text();
    QString it = ui->txtIterations->text();
    QString x1 = ui->txtx1->text();
    QString x2 = ui->txtx2->text();
    QString x3 = ui->txtx3->text();

    // Decide which Python function to call
    QString module = "Optimisers.LinearSearch.GoldenSection";
    QString function = "golden_section_search";
    if (ui->rbInverse->isChecked()) {
        module = "Optimisers.LinearSearch.InverseParabolicInterpolation";
        function = "inverse_parabolic_interpolation";
    } else if (ui->rbNewton->isChecked()) {
        module = "Optimisers.LinearSearch.NewtonsMethodLinear";
        function = "newtons_method";
    }

    // Build args: (fn, x1, x2, x3, it, showPlot)
    QStringList args = { fn, x1, x2, x3, it, showPlot ? "1" : "0" };

    QString result = callPythonFunction(module, function, args);
    qDebug() << "Python returned:" << result;
    ui->txtOutput->setText(result);
}

void LinearWindow::btnBack_clicked()
{
    hide();
    Menu *m = new Menu(this);
    m->show();
}

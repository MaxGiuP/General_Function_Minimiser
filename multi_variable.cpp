#include "multi_variable.h"
#include "ui_multi_variable.h"
#include "globalfunctions.h"
#include "main_menu.h"
#include "QTextEdit"

multi_variable::multi_variable(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::multi_variable)
{
    ui->setupUi(this);
}

multi_variable::~multi_variable()
{
    delete ui;
}

double func(QString f, int count, ...)
{
    int i;
    va_list args;
    va_start(args, count);

    f.replace(" ", "");
    for (int i = 0; i < count; i++) {
        f.replace(QString::number(97 + i), QString::number(va_arg(args, double)));
    }

    va_end(args);
    return evaluateExpression(f);
}

double Steep_Descent(double x1, double x2, double x3, QString inp, double tol, int max)
{
    double ans;

    return ans;
}

void multi_variable::on_btnCalculate_clicked()
{
    QString func, var;
    func = ui->txtFunc->text();
    var = ui->txtVar->text();

    QLineEdit *sol = ui->txtSol;
    if (ui->rbSD->isChecked() == true)
    {
        sol->setText(QString::number(Steep_Descent()));
    }
    else if(ui->rbCG->isChecked() == true)
    {

    }
    else if(ui->rbNM->isChecked() == true)
    {

    }
    else if(ui->rbBFGS->isChecked() == true)
    {

    }
    else if(ui->rbHJ->isChecked() == true)
    {

    }
}

void multi_variable::on_btnBack_clicked()
{
    this->hide();
    Main_Menu *menu = new Main_Menu;
    menu->show();
}

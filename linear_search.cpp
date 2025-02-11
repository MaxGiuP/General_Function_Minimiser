#include "linear_search.h"
#include "ui_linear_search.h"
#include "main_menu.h"
#include <qmessagebox.h>
#include <QString>
#include <QDebug>
#include <QRegularExpression>
#include <cmath>

linear_search::linear_search(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::linear_search)
{
    ui->setupUi(this);
}

linear_search::~linear_search()
{
    delete ui;
}

const double phi = 2 - (1 + sqrt(5)) / 2;

double evaluateExpression(QString f);

double func(double x, QString f)
{
    f.replace("x", QString::number(x));

    int startPos = f.indexOf("(");
    while (startPos != -1) {
        int endPos = f.indexOf(")", startPos);
        if (endPos == -1) {
            qWarning() << "Mismatched parentheses!";
            return 0;
        }

        QString subExpr = f.mid(startPos + 1, endPos - startPos - 1);

        double result = evaluateExpression(subExpr);

        f.replace(startPos, endPos - startPos + 1, QString::number(result));

        startPos = f.indexOf("(");
    }

    return evaluateExpression(f);
}

double evaluateExpression(QString f)
{
    QRegularExpression regExp("(\\d*\\.?\\d+|[+\\-*/^()])");
    QRegularExpressionMatchIterator iter = regExp.globalMatch(f);
    QStringList tokens;

    while (iter.hasNext()) {
        QRegularExpressionMatch match = iter.next();
        tokens << match.captured(0);
    }

    for (int i = 0; i < tokens.size(); ++i) {
        if (tokens[i] == "^") {
            double left = tokens[i - 1].toDouble();
            double right = tokens[i + 1].toDouble();
            double result = std::pow(left, right);
            tokens.replace(i - 1, QString::number(result));
            tokens.removeAt(i);
            tokens.removeAt(i);
            i--;
        }
    }

    for (int i = 0; i < tokens.size(); ++i) {
        if (tokens[i] == "*" || tokens[i] == "/") {
            double left = tokens[i - 1].toDouble();
            double right = tokens[i + 1].toDouble();
            double result = 0;

            if (tokens[i] == "*") {
                result = left * right;
            } else if (tokens[i] == "/") {
                if (right != 0) {
                    result = left / right;
                } else {
                    qWarning() << "Division by zero!";
                    return 0;
                }
            }

            tokens.replace(i - 1, QString::number(result));
            tokens.removeAt(i);
            tokens.removeAt(i);
            i--;
        }
    }

    double result = tokens[0].toDouble();
    for (int i = 1; i < tokens.size(); i += 2) {
        QString op = tokens[i];
        double value = tokens[i + 1].toDouble();

        if (op == "+") {
            result += value;
        } else if (op == "-") {
            result -= value;
        }
    }

    return result;
}

double GoldenSection(double x1, double x2, double x3, QString inp, double tol, int max)
{
    double x4;
    int i = 0;

    while (x3 - x1 > tol && i < max)
    {
        if (x3-x2 > x2-x1)
        {
            x4 = (phi) * (x3 - x2) + x2;

            if (func(x2, inp) > func(x4, inp))
            {
                x1 = x2;
                x2 = x4;
            }
            else
            {
                x3 = x4;
            }
        }
        else
        {
            x4 = (1 - phi) * (x2 - x1) + x1;

            if (func(x2, inp) > func(x4, inp))
            {
                x3 = x2;
                x2 = x4;
            }
            else
            {
                x1 = x4;
            }
        }
        i++;
    }

    return (x1+x3) / 2.0;
}

double Parabolic(double x1, double x2, double x3, QString inp, double tol, int max)
{
    double f1, f2, f3;
    double x_new;
    int max_iterations = 1000;
    int iteration = 0;

    while (std::abs(x3 - x1) > tol && iteration < max)
    {
        f1 = func(x1, inp);
        f2 = func(x2, inp);
        f3 = func(x3, inp);

        double numerator = (x2 - x1) * (x2 - x1) * (f2 - f3) - (x2 - x3) * (x2 - x3) * (f2 - f1);
        double denominator = (x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1);

        if (std::abs(denominator) < 1e-10) { // Avoid division by zero
            qDebug() << "Denominator too close to zero. Stopping early.";
            return x2;
        }

        x_new = x2 - 0.5 * (numerator / denominator);

        if (x_new > x2) {
            if (func(x_new, inp) < f2) {
                x1 = x2;
                x2 = x_new;
            } else {
                x3 = x_new;
            }
        } else {
            if (func(x_new, inp) < f2) {
                x3 = x2;
                x2 = x_new;
            } else {
                x1 = x_new;
            }
        }

        iteration++;

        if (iteration > max_iterations) {
            qDebug() << "Maximum iterations reached in Inverse Parabolic Search.";
            return x2;
        }

    }

    return x2;
}

double Newton(double x1, QString inp, double tol, int max)
{
    double fp, fpp;
    double h = 0.01;
    double x, temp;
    int i = 0;

    x = x1;
    fp = (func(x + h, inp) - func(x - h, inp)) / (2.0 * h);
    fpp = (func(x + h, inp) - 2.0 * func(x, inp) + func(x - h, inp)) / (h * h);

    temp = 10;
    while (std::abs(x - temp) > tol && i < max)
    {
        fp = (func(x + h, inp) - func(x - h, inp)) / (2.0 * h);
        fpp = (func(x + h, inp) - 2.0 * func(x, inp) + func(x - h, inp)) / (h * h);

        qDebug() << x;
        temp = x;
        x = x - (fp/fpp);
        i++;
    }

    qDebug() << "End newton";

    return x;
}

void linear_search::on_pBGRCalc_clicked()
{
    double x1, x2, x3, tol;
    int i = 0;
    int max = 0;

    tol = ui->leTol->text().toDouble();
    x1 = ui->leX1->text().toDouble();
    x2 = ui->leX2->text().toDouble();
    x3 = ui->leX3->text().toDouble();
    max = ui->leIter->text().toInt();

    QString inp = ui->leFunc->text();

    if (ui->rbtnGolden->isChecked() == true)
    {
        ui->leSol->setText(QString::number(GoldenSection(x1, x2, x3, inp, tol, max)));
    }
    else if(ui->rbtnParabolic->isChecked() == true)
    {
        ui->leSol->setText(QString::number(Parabolic(x1, x2, x3, inp, tol, max)));
    }
    else if(ui->rbtnNewton->isChecked() == true)
    {
        ui->leSol->setText(QString::number(Newton(x1, inp, tol, max)));
        qDebug() << "Newton's";
    }

    qDebug() << "DONE";

}


void linear_search::on_rbtnNewton_clicked()
{
    ui->leX3->setEnabled(false);
    ui->leX2->setEnabled(false);
    ui->leX3->setText("");
    ui->leX2->setText("");
}


void linear_search::on_rbtnParabolic_clicked()
{
    ui->leX3->setEnabled(true);
    ui->leX2->setEnabled(true);
}


void linear_search::on_rbtnGolden_clicked()
{
    ui->leX3->setEnabled(true);
    ui->leX2->setEnabled(true);
}


void linear_search::on_btnBack_clicked()
{
    this->hide();
    Main_Menu *menu = new Main_Menu(this);
    menu->show();
}


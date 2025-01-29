#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <qmessagebox.h>
#include <QString>
#include <QDebug>
#include <QRegularExpression>
#include <cmath>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
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

double GoldenSection(double x1, double x2, double x3, QString inp, double tol)
{
    double x4;
    int i = 0;

    while (x3 - x1 > tol && i < 100000)
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

double Parabolic(double x1, double x2, double x3, QString inp, double tol)
{

    return 0;
}

double Newton(double x1, double x2, double x3, QString inp, double tol)
{

    return 0;
}

void MainWindow::on_pBGRCalc_clicked()
{
    double x1, x2, x3, tol, answer;
    int i = 0;

    tol = ui->leTol->text().toDouble();
    x1 = ui->leX1->text().toDouble();
    x2 = ui->leX2->text().toDouble();
    x3 = ui->leX3->text().toDouble();

    QString inp = ui->leFunc->text();

    if (ui->rbtnGolden->isEnabled() == true)
    {
        ui->leSol->setText(QString::number(GoldenSection(x1, x2, x3, inp, tol)));
    }
    else if(ui->rbtnParabolic->isEnabled() == true)
    {
        ui->leSol->setText(QString::number(Parabolic(x1, x2, x3, inp, tol)));
    }
    else
    {
        ui->leSol->setText(QString::number(Newton(x1, x2, x3, inp, tol)));
    }

    qDebug() << "DONE";

}


void MainWindow::on_rbtnNewton_clicked()
{
    ui->leX3->setEnabled(false);
    ui->leX2->setEnabled(false);
    ui->leX3->setText("");
    ui->leX2->setText("");
}


void MainWindow::on_rbtnParabolic_clicked()
{
    ui->leX3->setEnabled(true);
    ui->leX2->setEnabled(true);
}


void MainWindow::on_rbtnGolden_clicked()
{
    ui->leX3->setEnabled(true);
    ui->leX2->setEnabled(true);
}


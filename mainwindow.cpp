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

void MainWindow::on_pBGRCalc_clicked()
{
    double x1, x2, x3, x4, tol;
    int i = 0;

    tol = ui->leTol->text().toDouble();
    x1 = ui->lEx1->text().toDouble();
    x2 = ui->lEx2->text().toDouble();
    x3 = ui->lEx3->text().toDouble();

    QString inp = ui->leFunc->text();

    while (x3 - x1 > tol)
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
        qDebug() << i << " x1 is " << x1;
        qDebug() << i << " x2 is " << x2;
        qDebug() << i << " x3 is " << x3;
        qDebug() << i << " x4 is " << x4;
        qDebug() << i << " average of x1 and x3 is " << (x1 + x3) / 2.0;

        i++;
    }

    ui->leSol->setText(QString::number((x1+x3) / 2.0));

    qDebug() << "DONE";

}


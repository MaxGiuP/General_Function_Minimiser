#include "multi_variable.h"
#include "ui_multi_variable.h"
#include "globalfunctions.h"
#include "linear_search.h"
#include "main_menu.h"
#include "QTextEdit"

const double h = 0.01;
const double phi = 2 - (1 + sqrt(5)) / 2;

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

double func_vec(QString f, QVector<double> x)
{
    QStringList x_str;
    int count = x.count();
    f.replace(" ", "");
    ;
    for (int i = 0; i < count; i++)
    {
        x_str.append(QString::number(x[i]));
    }

    for (int i = 0; i < count; i++)
    {
        f.replace("x" + QString::number(i + 1), x_str[i]);
    }

    return evaluateExpression(f);
}

std::pair<double,double> getInterval(QString func_lambda, double alphaLow, double alphaHigh)
{
    if (alphaLow < 0) alphaLow = 0;
    if (alphaHigh <= alphaLow) alphaHigh = alphaLow + 1.0;

    double fLow  = func(func_lambda, alphaLow);
    double fHigh = func(func_lambda, alphaHigh);

    // If we already bracket a minimum:
    if (fHigh > fLow) {
        return std::make_pair(alphaLow, alphaHigh);
    }

    // Exponential expansion: up to 20 expansions
    for (int i = 0; i < 20; i++)
    {
        double oldAlpha = alphaHigh;
        double oldVal   = fHigh;
        alphaHigh *= 2.0;
        fHigh = func(func_lambda, alphaHigh);

        // If we see fHigh > oldVal, bracket found
        if (fHigh > oldVal) {
            return {oldAlpha, alphaHigh};
        }
    }

    // If we get here, the function never went up,
    // so it's likely decreasing or nearly flat.
    // Return the biggest range we have.
    return {alphaHigh/2, alphaHigh};
}

QStringList Steep_Descent(QStringList x_str, QString inp, double tol, int max)
{
    int EndLoop = 0;
    double diff = 0;
    double alpha0 = 0;
    double alpha1 = 0;

    int count = x_str.count();
    if (count == 0) {
        qDebug() << "Error: No variables provided!";
        return QStringList();
    }

    QString func_lambda;
    QVector<double> x(count);
    QVector<double> p_derivatives(count);

    double lambda = 1;  // Initial Guess for Line Search
    for (int i = 0; i < count; i++)
    {
        x[i] = x_str[i].toDouble();
    }

    int iter = 0;
    QVector<double> x_2 = x;
    while (EndLoop == 0 && iter < max)
    {
        qDebug() << ("iter loop: " + QString::number(iter));
        x_2 = x;  // Store previous x values
        diff = 100;
        func_lambda = inp;

        for (int i = 0; i < count; i++)
        {
            QVector<double> forward = x;
            forward[i] = forward[i] + h;
            QVector<double> backward = x;
            backward[i] = backward[i] - h;

            p_derivatives[i] = (func_vec(inp, forward) - func_vec(inp, backward)) / (2 * h);
            qDebug() << "gradients[" + QString::number(i) + "]: " << p_derivatives[i];
            func_lambda.replace("x" + QString::number(i + 1), "(" + QString::number(x[i]) + "-" + QString::number(p_derivatives[i]) + "*x)");
        }


        auto [f0, f1] = getInterval(func_lambda, alpha0, alpha1);
        qDebug() << "func_lambda: " << func_lambda;
        qDebug() << "f0: " << f0 << "  f1: " << f1;
        lambda = GoldenSection(f0, f1, std::abs(f1 - f0)*phi + f0, func_lambda, 0.1, 30);
        qDebug() << "lambda: " << lambda;

        for (int i = 0; i < count; i++)
        {
            x[i] = x[i] - lambda * p_derivatives[i];
            qDebug() << "x[" + QString::number(i) + "]: " << lambda;
        }

        if (iter > 0)
        {
            if (std::abs(x[0] - x_2[0]) < diff)
            {
                diff = std::abs(x[0] - x_2[0]);
                if (diff < tol)
                {
                    EndLoop = 1;
                }
            }
        }

        qDebug() << "x1 is: " + QString::number(x[0]);
        qDebug() << "x2 is: " + QString::number(x[1]);
        qDebug() << "\n\n";
        iter++;
    }

    for (int i = 0; i < count; i++)
    {
        x_str[i] = QString::number(x[i]);
    }

    return x_str;  // Return the final values as a QStringList
}

QStringList Conjugate_Gradient(QStringList x_str, QString inp, double tol, int max)
{
    int EndLoop = 0;
    double del_f; double last_del_f;
    double diff = 0;
    double alpha0 = 0;
    double alpha1 = 0;

    int count = x_str.count();
    if (count == 0) {
        qDebug() << "Error: No variables provided!";
        return QStringList();
    }

    QString func_lambda;
    QVector<double> x(count);
    QVector<double> S(count);

    double lambda = 1;  // Initial Guess for Line Search
    for (int i = 0; i < count; i++)
    {
        x[i] = x_str[i].toDouble();
    }

    int iter = 0;
    QVector<double> x_2 = x;
    while (EndLoop == 0 && iter < max)
    {
        qDebug() << ("iter loop: " + QString::number(iter));
        x_2 = x;  // Store previous x values
        diff = 100;
        func_lambda = inp;

        for (int i = 0; i < count; i++)
        {
            qDebug() << "gradients[" + QString::number(i) + "]: " << S[i];
            func_lambda.replace("x" + QString::number(i + 1), "(" + QString::number(x[i]) + "-" + QString::number(S[i]) + "*x)");
        }

        for (int i = 0; i < count; i++)
        {
            QVector<double> forward = x;
            forward[i] = forward[i] + h;
            QVector<double> backward = x;
            backward[i] = backward[i] - h;

            last_del_f = del_f;
            del_f = (func_vec(inp, forward) - func_vec(inp, backward)) / (2 * h);
            if (iter == 0)
            {
                S[i] = -del_f;
            }
            else
            {
                S[i] = -del_f + pow((del_f), 2) / pow((last_del_f), 2) * S[i];
            }


            qDebug() << "S[" + QString::number(i) + "]: " << S[i];
            func_lambda.replace("x" + QString::number(i + 1), "(" + QString::number(x[i]) + "-" + QString::number(S[i]) + "*x)");
        }


        auto [f0, f1] = getInterval(func_lambda, alpha0, alpha1);
        qDebug() << "func_lambda: " << func_lambda;
        qDebug() << "f0: " << f0 << "  f1: " << f1;
        lambda = GoldenSection(f0, f1, std::abs(f1 - f0)*phi + f0, func_lambda, 0.1, 30);
        qDebug() << "lambda: " << lambda;

        if (iter != 0)
        {
            lambda = -lambda;
        }

        for (int i = 0; i < count; i++)
        {
            x[i] = x[i] - lambda * S[i];
            qDebug() << "x[" + QString::number(i) + "]: " << lambda;
        }

        if (iter > 0)
        {
            if (std::abs(x[0] - x_2[0]) < diff)
            {
                diff = std::abs(x[0] - x_2[0]);
                if (diff < tol)
                {
                    EndLoop = 1;
                }
            }
        }

        qDebug() << "x1 is: " + QString::number(x[0]);
        qDebug() << "x2 is: " + QString::number(x[1]);
        qDebug() << "\n\n";
        iter++;
    }

    for (int i = 0; i < count; i++)
    {
        x_str[i] = QString::number(x[i]);
    }

    return x_str;  // Return the final values as a QStringList
}

QStringList Newton_Method(QStringList x_str, QString inp, double tol, int max)
{
    int EndLoop = 0;
    double del_f; double last_del_f;
    double diff = 0;
    double alpha0 = 0;
    double alpha1 = 0;

    int count = x_str.count();
    if (count == 0) {
        qDebug() << "Error: No variables provided!";
        return QStringList();
    }

    QString func_lambda;
    QVector<double> x(count);
    QVector<double> S(count);

    double lambda = 1;  // Initial Guess for Line Search
    for (int i = 0; i < count; i++)
    {
        x[i] = x_str[i].toDouble();
    }

    int iter = 0;
    QVector<double> x_2 = x;
    while (EndLoop == 0 && iter < max)
    {
        qDebug() << ("iter loop: " + QString::number(iter));
        x_2 = x;  // Store previous x values
        diff = 100;
        func_lambda = inp;

        for (int i = 0; i < count; i++)
        {
            qDebug() << "gradients[" + QString::number(i) + "]: " << S[i];
            func_lambda.replace("x" + QString::number(i + 1), "(" + QString::number(x[i]) + "-" + QString::number(S[i]) + "*x)");
        }

        for (int i = 0; i < count; i++)
        {
            QVector<double> forward = x;
            forward[i] = forward[i] + h;
            QVector<double> backward = x;
            backward[i] = backward[i] - h;

            last_del_f = del_f;
            del_f = (func_vec(inp, forward) - func_vec(inp, backward)) / (2 * h);
            if (iter == 0)
            {
                S[i] = -del_f;
            }
            else
            {
                S[i] = -del_f + pow((del_f), 2) / pow((last_del_f), 2) * S[i];
            }


            qDebug() << "S[" + QString::number(i) + "]: " << S[i];
            func_lambda.replace("x" + QString::number(i + 1), "(" + QString::number(x[i]) + "-" + QString::number(S[i]) + "*x)");
        }


        auto [f0, f1] = getInterval(func_lambda, alpha0, alpha1);
        qDebug() << "func_lambda: " << func_lambda;
        qDebug() << "f0: " << f0 << "  f1: " << f1;
        lambda = GoldenSection(f0, f1, std::abs(f1 - f0)*phi + f0, func_lambda, 0.1, 30);
        qDebug() << "lambda: " << lambda;

        if (iter != 0)
        {
            lambda = -lambda;
        }

        for (int i = 0; i < count; i++)
        {
            x[i] = x[i] - lambda * S[i];
            qDebug() << "x[" + QString::number(i) + "]: " << lambda;
        }

        if (iter > 0)
        {
            if (std::abs(x[0] - x_2[0]) < diff)
            {
                diff = std::abs(x[0] - x_2[0]);
                if (diff < tol)
                {
                    EndLoop = 1;
                }
            }
        }

        qDebug() << "x1 is: " + QString::number(x[0]);
        qDebug() << "x2 is: " + QString::number(x[1]);
        qDebug() << "\n\n";
        iter++;
    }

    for (int i = 0; i < count; i++)
    {
        x_str[i] = QString::number(x[i]);
    }

    return x_str;  // Return the final values as a QStringList
}

void multi_variable::on_btnCalculate_clicked()
{
    QString inp = ui->txtFunc->text();
    QStringList x = ui->txtX->text().replace(" ", "").split(",");
    double tol = ui->txtTol->text().toDouble();
    int max = ui->txtIter->text().toInt();  // Ensure `txtMaxIter` exists in the UI

    QLineEdit *sol = ui->txtSol;
    QStringList result;

    if (ui->rbSD->isChecked())  // Steepest Descent
    {
        result = Steep_Descent(x, inp, tol, max);
    }
    else if(ui->rbCG->isChecked())  // Conjugate Gradient (Use Different Function)
    {
        result = Conjugate_Gradient(x, inp, tol, max);
    }
    else if(ui->rbNM->isChecked())  // Newton's Method
    {
        result = Newton_Method(x, inp, tol, max);
    }
    else if(ui->rbBFGS->isChecked())  // BFGS
    {
        //result = BFGS(x, inp, tol, max);
    }
    else if(ui->rbHJ->isChecked())  // Hooke-Jeeves
    {
        //result = Hooke_Jeeves(x, inp, tol, max);
    }

    // Join the vector with commas and set as output
    sol->setText(result.join(", "));
}

void multi_variable::on_btnBack_clicked()
{
    this->hide();
    Main_Menu *menu = new Main_Menu;
    menu->show();
}

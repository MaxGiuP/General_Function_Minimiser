#include "multi_variable.h"
#include "ui_multi_variable.h"
#include "globalfunctions.h"
#include "linear_search.h"
#include "main_menu.h"
#include "QTextEdit"
#include <cmath>

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

    if (fHigh > fLow) {
        return std::make_pair(alphaLow, alphaHigh);
    }

    for (int i = 0; i < 20; i++)
    {
        double oldAlpha = alphaHigh;
        double oldVal   = fHigh;
        alphaHigh *= 2.0;
        fHigh = func(func_lambda, alphaHigh);

        if (fHigh > oldVal) {
            return {oldAlpha, alphaHigh};
        }
    }

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
            func_lambda.replace("x" + QString::number(i + 1), "(" + QString::number(x[i]) + "-" + QString::number(p_derivatives[i]) + "*x)");
        }


        auto [f0, f1] = getInterval(func_lambda, alpha0, alpha1);
        lambda = GoldenSection(f0, std::abs(f1 - f0)*phi + f0, f1, func_lambda, 0.1, 30);

        for (int i = 0; i < count; i++)
        {
            x[i] = x[i] - lambda * p_derivatives[i];
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
    double abs_del = 0;       // Will hold the sum of squares of the current gradient
    double last_abs_del = 0;  // Sum of squares of the previous gradient
    double diff = 0;

    int count = x_str.count();
    if (count == 0) {
        qDebug() << "Error: No variables provided!";
        return QStringList();
    }

    QString func_lambda;
    QVector<double> x(count);
    QVector<double> p_derivatives(count);
    QVector<double> S(count);

    double lambda = 1;  // Initial guess for the line search step length
    // Load initial x values.
    for (int i = 0; i < count; i++) {
        x[i] = x_str[i].toDouble();
    }

    int iter = 0;
    QVector<double> x_2 = x;

    while (EndLoop == 0 && iter < max)
    {
        x_2 = x;

        last_abs_del = abs_del;
        abs_del = 0;
        func_lambda = inp;

        for (int i = 0; i < count; i++)
        {
            QVector<double> forward = x;
            forward[i] += h;
            QVector<double> backward = x;
            backward[i] -= h;

            p_derivatives[i] = (func_vec(inp, forward) - func_vec(inp, backward)) / (2 * h);
            abs_del += pow(p_derivatives[i], 2);
            qDebug() << "p_derivatives[" << i << "]: " << p_derivatives[i];
        }


        for (int i = 0; i < count; i++)
        {
            if (iter == 0 || last_abs_del == 0)
            {
                S[i] = -p_derivatives[i];
            }
            else
            {
                S[i] = -p_derivatives[i] + abs_del / last_abs_del * S[i];
            }

            func_lambda.replace("x" + QString::number(i + 1), "(" + QString::number(x[i]) + "+" + QString::number(S[i]) + "*x)");
        }

        auto [f0, f1] = getInterval(func_lambda, 0, 5);
        lambda = GoldenSection(f0, f0 + (f1 - f0)*phi, f1, func_lambda, 0.01, 50);

        for (int i = 0; i < count; i++)
        {
            x[i] = x[i] + lambda * S[i];
        }


        double norm_diff = 0;
        for (int i = 0; i < count; i++)
        {
            norm_diff += pow(x[i] - x_2[i], 2);
        }
        norm_diff = sqrt(norm_diff);
        if (norm_diff < tol)
        {
            EndLoop = 1;
        }

        iter++;
    }

    for (int i = 0; i < count; i++) {
        x_str[i] = QString::number(x[i]);
    }

    return x_str;
}


void invertMatrix(double **M, int count) {
    double **aug = new double*[count];
    for (int i = 0; i < count; i++) {
        aug[i] = new double[2 * count];

        for (int j = 0; j < count; j++) {
            aug[i][j] = M[i][j];
        }
        for (int j = count; j < 2 * count; j++) {
            aug[i][j] = (i == (j - count)) ? 1.0 : 0.0;
        }
    }

    for (int i = 0; i < count; i++) {
        int pivot = i;
        for (int j = i + 1; j < count; j++) {
            if (fabs(aug[j][i]) > fabs(aug[pivot][i])) {
                pivot = j;
            }
        }

        if (pivot != i) {
            for (int j = 0; j < 2 * count; j++) {
                double temp = aug[i][j];
                aug[i][j] = aug[pivot][j];
                aug[pivot][j] = temp;
            }
        }

        if (fabs(aug[i][i]) < 1e-9) {
            qDebug() << "Hessian is singular, adding small identity matrix perturbation.";
            for (int i = 0; i < count; i++) {
                M[i][i] += 1e-6;
            }
        }

        double pivotValue = aug[i][i];
        for (int j = 0; j < 2 * count; j++) {
            aug[i][j] /= pivotValue;
        }

        for (int j = 0; j < count; j++) {
            if (j != i) {
                double factor = aug[j][i];
                for (int k = 0; k < 2 * count; k++) {
                    aug[j][k] -= factor * aug[i][k];
                }
            }
        }
    }

    for (int i = 0; i < count; i++) {
        for (int j = 0; j < count; j++) {
            M[i][j] = aug[i][j + count];
        }
    }

    for (int i = 0; i < count; i++) {
        delete[] aug[i];
    }
    delete[] aug;
}

QStringList Newton_Method(QStringList x_str, QString inp, double tol, int max)
{
    int EndLoop = 0;
    double diff = 0;
    double row_total;
    int count = x_str.count();
    if (count == 0)
    {
        qDebug() << "Error: No variables provided!";
        return QStringList();
    }

    QString func_lambda;
    QVector<double> x(count);
    QVector<double> p_derivatives(count);
    double **H = new double*[count];
    for (int i = 0; i < count; i++)
    {
        H[i] = new double[count];
        x[i] = x_str[i].toDouble();
    }

    int iter = 0;
    QVector<double> x_2 = x;
    while (EndLoop == 0 && iter < max)
    {
        diff = 100;
        x_2 = x;
        func_lambda = inp;

        for (int i = 0; i < count; i++)
        {
            QVector<double> forward = x;
            forward[i] += h;
            QVector<double> backward = x;
            backward[i] -= h;
            p_derivatives[i] = (func_vec(inp, forward) - func_vec(inp, backward)) / (2 * h);
        }

        //Fills Hessian
        for (int i = 0; i < count; i++)
        {
            for (int j = 0; j < count; j++)
            {
                if (i == j) {
                    QVector<double> forward = x, backward = x;
                    forward[i] += h;
                    backward[i] -= h;
                    double v1 = func_vec(inp, forward);
                    double v2 = func_vec(inp, backward);
                    double v0 = func_vec(inp, x);

                    H[i][j] = (v1 - 2 * v0 + v2) / pow(h, 2);

                }
                else
                {
                    QVector<double> f1 = x, f2 = x, f3 = x, f4 = x;
                    f1[i] += h; f1[j] += h;
                    f2[i] += h; f2[j] -= h;
                    f3[i] -= h; f3[j] += h;
                    f4[i] -= h; f4[j] -= h;

                    double v1 = func_vec(inp, f1);
                    double v2 = func_vec(inp, f2);
                    double v3 = func_vec(inp, f3);
                    double v4 = func_vec(inp, f4);

                    H[i][j] = (v1 - v2 - v3 + v4) / (4 * h * h);
                }

            }
        }

        invertMatrix(H, count);

        for (int i = 0; i < count; i++)
        {
            row_total = 0;
            for (int j = 0; j < count; j++)
            {
                row_total += p_derivatives[j] * H[i][j];
            }

            x[i] = x[i] - row_total;
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

        iter++;
    }

    for (int i = 0; i < count; i++)
    {
        delete[] H[i];
    }
    delete[] H;

    for (int i = 0; i < count; i++)
    {
        x_str[i] = QString::number(x[i]);
    }

    return x_str;
}

QStringList BFGS(QStringList x_str, QString inp, double tol, int max)
{
    int count = x_str.count();
    if (count == 0)
    {
        qDebug() << "Error: No variables provided!";
        return QStringList();
    }

    QVector<double> x(count), grad(count), grad_old(count), s(count), y(count);
    QVector<QVector<double>> B_inv(count, QVector<double>(count, 0));

    for (int i = 0; i < count; i++)
    {
        x[i] = x_str[i].toDouble();
        B_inv[i][i] = 1.0;
    }

    int iter = 0;
    while (iter < max)
    {
        for (int i = 0; i < count; i++)
        {
            QVector<double> forward = x, backward = x;
            forward[i] += h;
            backward[i] -= h;
            grad[i] = (func_vec(inp, forward) - func_vec(inp, backward)) / (2 * h);
        }

        QVector<double> p(count, 0);
        for (int i = 0; i < count; i++)
        {
            for (int j = 0; j < count; j++)
            {
                p[i] -= B_inv[i][j] * grad[j];
            }
        }

        double alpha = 1.0;
        QVector<double> x_new = x;
        for (int i = 0; i < count; i++)
        {
            x_new[i] = x[i] + alpha * p[i];
        }

        for (int i = 0; i < count; i++)
        {
            QVector<double> forward = x_new, backward = x_new;
            forward[i] += h;
            backward[i] -= h;
            grad_old[i] = grad[i];
            grad[i] = (func_vec(inp, forward) - func_vec(inp, backward)) / (2 * h);
        }

        for (int i = 0; i < count; i++)
        {
            s[i] = x_new[i] - x[i];
            y[i] = grad[i] - grad_old[i];
        }

        double sy = 0, yBy = 0;
        QVector<double> By(count, 0);
        for (int i = 0; i < count; i++)
        {
            sy += s[i] * y[i];
            for (int j = 0; j < count; j++)
            {
                By[i] += B_inv[i][j] * y[j];
            }
        }

        for (int i = 0; i < count; i++)
        {
            yBy += y[i] * By[i];
        }

        if (sy > 1e-10)
        {
            for (int i = 0; i < count; i++)
            {
                for (int j = 0; j < count; j++)
                {
                    B_inv[i][j] += (s[i] * s[j]) / sy - (By[i] * By[j]) / yBy;
                }
            }
        }

        double norm = 0;
        for (int i = 0; i < count; i++)
        {
            norm += fabs(x_new[i] - x[i]);
            x[i] = x_new[i];
        }

        if (norm < tol)
        {
            break;
        }

        iter++;
    }

    for (int i = 0; i < count; i++)
    {
        x_str[i] = QString::number(x[i]);
    }

    return x_str;
}


QStringList Hooke_Jeeves(QStringList x_str, QString inp, double tol, int max)
{
    int count = x_str.count();
    if (count == 0) {
        qDebug() << "Error: No variables provided!";
        return QStringList();
    }

    QVector<double> x(count);
    for (int i = 0; i < count; i++) {
        x[i] = x_str[i].toDouble();
    }

    QVector<double> step(count, 1.0);
    const double alpha = 0.5;

    int iter = 0;
    double f_best = func_vec(inp, x);
    QVector<double> x_best = x;

    while (*std::max_element(step.begin(), step.end()) > tol && iter < max)
    {
        QVector<double> x_new = x_best;
        double f_new = f_best;

        for (int i = 0; i < count; i++) {
            QVector<double> x_try = x_new;

            x_try[i] += step[i];
            double f_try = func_vec(inp, x_try);
            if (f_try < f_new) {
                x_new[i] = x_try[i];
                f_new = f_try;
                continue;
            }

            x_try[i] = x_new[i] - step[i];
            f_try = func_vec(inp, x_try);
            if (f_try < f_new) {
                x_new[i] = x_try[i];
                f_new = f_try;
            }
        }

        if (f_new < f_best) {
            QVector<double> pattern_move(count);
            for (int i = 0; i < count; i++) {
                pattern_move[i] = x_new[i] + (x_new[i] - x_best[i]);
            }

            double f_pattern = func_vec(inp, pattern_move);
            if (f_pattern < f_new) {
                x_best = pattern_move;
                f_best = f_pattern;
            } else {
                x_best = x_new;
                f_best = f_new;
            }
        }
        else {
            for (int i = 0; i < count; i++) {
                step[i] *= alpha;
            }
        }

        iter++;
    }

    for (int i = 0; i < count; i++) {
        x_str[i] = QString::number(x_best[i]);
    }

    return x_str;
}

void multi_variable::on_btnCalculate_clicked()
{
    QString inp = ui->txtFunc->text();
    QStringList x = ui->txtX->text().replace(" ", "").split(",");
    double tol = ui->txtTol->text().toDouble();
    int max = ui->txtIter->text().toInt();

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
        result = BFGS(x, inp, tol, max);
    }
    else if(ui->rbHJ->isChecked())  // Hooke-Jeeves
    {
        result = Hooke_Jeeves(x, inp, tol, max);
    }

    sol->setText(result.join(", "));
}

void multi_variable::on_btnBack_clicked()
{
    this->hide();
    Main_Menu *menu = new Main_Menu;
    menu->show();
}

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

        qDebug() << "abs_del (current gradient norm^2): " << abs_del;
        qDebug() << "last_abs_del: " << last_abs_del;


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
            qDebug() << "S[" << i << "]: " << S[i];
        }

        qDebug() << "func lambda: " << func_lambda;


        auto [f0, f1] = getInterval(func_lambda, 0, 5);
        qDebug() << "f0: " << f0 << "f1: " << f1;
        lambda = GoldenSection(f0, f0 + (f1 - f0)*phi, f1, func_lambda, 0.01, 50);
        qDebug() << "lambda: " << lambda;


        for (int i = 0; i < count; i++)
        {
            x[i] = x[i] + lambda * S[i];
            qDebug() << "x[" << i << "]: " << x[i];
        }


        double norm_diff = 0;
        for (int i = 0; i < count; i++)
        {
            norm_diff += pow(x[i] - x_2[i], 2);
        }
        norm_diff = sqrt(norm_diff);
        qDebug() << "norm_diff: " << norm_diff;
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
    // Augmented matrix (M | I)
    double **aug = new double*[count];
    for (int i = 0; i < count; i++) {
        aug[i] = new double[2 * count];

        // Copy M into the left side of aug and identity matrix into the right
        for (int j = 0; j < count; j++) {
            aug[i][j] = M[i][j];
        }
        for (int j = count; j < 2 * count; j++) {
            aug[i][j] = (i == (j - count)) ? 1.0 : 0.0;
        }
    }

    // Perform Gaussian elimination
    for (int i = 0; i < count; i++) {
        // Find the pivot row
        int pivot = i;
        for (int j = i + 1; j < count; j++) {
            if (fabs(aug[j][i]) > fabs(aug[pivot][i])) {
                pivot = j;
            }
        }

        // Manually swap rows using a temporary variable (since swap() is not allowed)
        if (pivot != i) {
            for (int j = 0; j < 2 * count; j++) {
                double temp = aug[i][j];
                aug[i][j] = aug[pivot][j];
                aug[pivot][j] = temp;
            }
        }

        // Check if matrix is singular
        if (fabs(aug[i][i]) < 1e-9) {
            qDebug() << "Hessian is singular, adding small identity matrix perturbation.";
            for (int i = 0; i < count; i++) {
                M[i][i] += 1e-6;
            }
        }

        // Normalize pivot row
        double pivotValue = aug[i][i];
        for (int j = 0; j < 2 * count; j++) {
            aug[i][j] /= pivotValue;
        }

        // Eliminate other rows
        for (int j = 0; j < count; j++) {
            if (j != i) {
                double factor = aug[j][i];
                for (int k = 0; k < 2 * count; k++) {
                    aug[j][k] -= factor * aug[i][k];
                }
            }
        }
    }

    // Copy inverse back into M
    for (int i = 0; i < count; i++) {
        for (int j = 0; j < count; j++) {
            M[i][j] = aug[i][j + count];
        }
    }

    // Free memory
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
                    double v0 = func_vec(inp, x);  // Original function value

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

        //Invert Hessian
        invertMatrix(H, count);

        //Evalute
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

    return x_str;  // Return the final values as a QStringList
}

QStringList BFGS(QStringList x_str, QString inp, double tol, int max)
{
    const double h = 1e-5;  // Small step for finite differences
    const double phi = 2 - (1 + sqrt(5)) / 2;  // Golden ratio
    int count = x_str.count();
    if (count == 0) {
        qDebug() << "Error: No variables provided!";
        return QStringList();
    }

    QVector<double> x(count);
    QVector<double> g(count), g_new(count), s(count), y(count);
    QVector<QVector<double>> B_inv(count, QVector<double>(count, 0.0));

    for (int i = 0; i < count; i++) {
        x[i] = x_str[i].toDouble();
        B_inv[i][i] = 1.0;  // Start with identity matrix for inverse Hessian
    }

    int iter = 0;
    double diff = 1e9;
    QVector<double> x_new = x;
    QVector<double> S(count);

    while (diff > tol && iter < max) {
        // Compute Gradient g_k
        for (int i = 0; i < count; i++) {
            QVector<double> forward = x, backward = x;
            forward[i] += h;
            backward[i] -= h;
            g[i] = (func_vec(inp, forward) - func_vec(inp, backward)) / (2 * h);
        }

        // Compute Search Direction p_k = -B_inv * g_k
        QVector<double> p(count, 0.0);
        for (int i = 0; i < count; i++) {
            for (int j = 0; j < count; j++) {
                p[i] -= B_inv[i][j] * g[j];
            }
        }

        // Line search using Golden Section Search
        double alpha0 = 0;
        double alpha1 = 1;
        QString func_lambda = inp;
        for (int i = 0; i < count; i++) {
            func_lambda.replace("x" + QString::number(i + 1), "(" + QString::number(x[i]) + "-" + QString::number(p[i]) + "*x)");
        }
        auto [f0, f1] = getInterval(func_lambda, alpha0, alpha1);
        double lambda = GoldenSection(f0, std::abs(f1 - f0) * phi + f0, f1, func_lambda, 0.1, 30);

        // Update x_k+1 = x_k + lambda * p_k
        for (int i = 0; i < count; i++) {
            x_new[i] = x[i] + lambda * p[i];
        }

        // Compute new gradient g_k+1
        for (int i = 0; i < count; i++) {
            QVector<double> forward = x_new, backward = x_new;
            forward[i] += h;
            backward[i] -= h;
            g_new[i] = (func_vec(inp, forward) - func_vec(inp, backward)) / (2 * h);
        }

        // Compute s_k = x_k+1 - x_k and y_k = g_k+1 - g_k
        for (int i = 0; i < count; i++) {
            s[i] = x_new[i] - x[i];
            y[i] = g_new[i] - g[i];
        }

        // Compute rho_k = 1 / (y_k^T * s_k)
        double ys = 0.0, ss = 0.0;
        for (int i = 0; i < count; i++) {
            ys += y[i] * s[i];
            ss += s[i] * s[i];
        }
        if (ys == 0) break;  // Avoid division by zero

        double rho = 1.0 / ys;

        // Update inverse Hessian B_k+1 using BFGS update formula
        QVector<QVector<double>> B_inv_new = B_inv;

        for (int i = 0; i < count; i++) {
            for (int j = 0; j < count; j++) {
                double term1 = (1.0 - rho * y[i] * s[j]) * B_inv[i][j] * (1.0 - rho * s[i] * y[j]);
                double term2 = rho * s[i] * s[j];
                B_inv_new[i][j] = term1 + term2;
            }
        }

        // Update variables for next iteration
        x = x_new;
        B_inv = B_inv_new;
        diff = ss;  // Check stopping condition ||s_k||

        iter++;
    }

    // Convert final result to QStringList
    for (int i = 0; i < count; i++) {
        x_str[i] = QString::number(x[i], 'f', 8);
    }

    return x_str;  // Return final values
}

QStringList Hooke_Jeeves(QStringList x_str, QString inp, double tol, int max)
{
    const double h = 1e-5;  // Small step for function evaluation
    int count = x_str.count();
    if (count == 0) {
        qDebug() << "Error: No variables provided!";
        return QStringList();
    }

    QVector<double> x(count);
    QVector<double> x_base(count);
    QVector<double> x_new(count);
    QVector<double> step(count, 0.5);  // Initial step size

    for (int i = 0; i < count; i++) {
        x[i] = x_str[i].toDouble();
    }

    int iter = 0;
    double diff = 1e9;
    x_base = x;  // Base point for pattern moves

    while (diff > tol && iter < max)
    {
        x_new = x_base;  // Start from base point
        bool improved = false;

        // Exploratory search
        for (int i = 0; i < count; i++) {
            QVector<double> test_x = x_new;
            test_x[i] += step[i];
            double f1 = func_vec(inp, test_x);

            test_x[i] = x_new[i] - step[i];
            double f2 = func_vec(inp, test_x);

            if (f1 < func_vec(inp, x_new)) {
                x_new[i] += step[i];
                improved = true;
            }
            else if (f2 < func_vec(inp, x_new)) {
                x_new[i] -= step[i];
                improved = true;
            }
        }

        // Pattern move
        if (improved) {
            for (int i = 0; i < count; i++) {
                x_new[i] = 2 * x_new[i] - x_base[i];  // Move in the same direction
            }

            if (func_vec(inp, x_new) < func_vec(inp, x_base)) {
                x_base = x_new;  // Accept pattern move
            }
            else {
                for (int i = 0; i < count; i++)
                    step[i] /= 2.0;  // Reduce step size
            }
        }
        else {
            for (int i = 0; i < count; i++)
                step[i] /= 2.0;  // Reduce step size
        }

        // Compute stopping condition
        diff = 0;
        for (int i = 0; i < count; i++) {
            diff += pow(x_new[i] - x_base[i], 2);
        }
        diff = sqrt(diff);

        iter++;
    }

    // Convert final result to QStringList
    for (int i = 0; i < count; i++) {
        x_str[i] = QString::number(x_base[i], 'f', 8);
    }

    return x_str;  // Return final values
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
        result = BFGS(x, inp, tol, max);
    }
    else if(ui->rbHJ->isChecked())  // Hooke-Jeeves
    {
        result = Hooke_Jeeves(x, inp, tol, max);
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

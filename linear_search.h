#ifndef LINEAR_SEARCH_H
#define LINEAR_SEARCH_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class linear_search;
}
QT_END_NAMESPACE

double Newton(double x1, QString inp, double tol, int max);
double GoldenSection(double x1, double x2, double x3, QString inp, double tol, int max);
double func(QString f, double x);

class linear_search : public QMainWindow
{
    Q_OBJECT

public:
    explicit linear_search(QWidget *parent = nullptr);
    ~linear_search();

private slots:
    void on_pBGRCalc_clicked();

    void on_rbtnNewton_clicked();

    void on_rbtnParabolic_clicked();

    void on_rbtnGolden_clicked();

    void on_btnBack_clicked();

private:
    Ui::linear_search *ui;
};
#endif // LINEAR_SEARCH_H

#ifndef LINEAR_SEARCH_H
#define LINEAR_SEARCH_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class linear_search;
}
QT_END_NAMESPACE

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

// ga.h
#ifndef GA_H
#define GA_H

#include <QMainWindow>
#include "ui_ga.h"

class Menu;  // forward

class GAWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit GAWindow(QWidget *parent = nullptr);
    ~GAWindow() override;

private slots:
    void btnCalculate_clicked();
    void btnSelection_clicked();
    void btnReproduction_clicked();
    void btnBack_clicked();

private:
    Ui::wGA *ui;
};

#endif // GA_H

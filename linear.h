// linear.h
#ifndef LINEAR_H
#define LINEAR_H

#include <QMainWindow>
#include "ui_linear.h"

class Menu;  // forward-declare so we can go “Back”

class LinearWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit LinearWindow(QWidget *parent = nullptr);
    ~LinearWindow() override;

private slots:
    void btnCalculate_clicked();
    void btnBack_clicked();

private:
    Ui::wLinear *ui;
};

#endif // LINEAR_H

// multivariable.h
#ifndef MULTIVARIABLE_H
#define MULTIVARIABLE_H

#include <QMainWindow>
#include "ui_multivariable.h"

class Menu;  // forward

class MultiVariableWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit MultiVariableWindow(QWidget *parent = nullptr);
    ~MultiVariableWindow() override;

private slots:
    void btnCalculate_clicked();
    void btnBack_clicked();

private:
    Ui::wMultiVariable *ui;
};

#endif // MULTIVARIABLE_H

// multiobjective.h
#ifndef MULTIOBJECTIVE_H
#define MULTIOBJECTIVE_H

#include <QMainWindow>
#include "ui_multiobjective.h"   // generated from multiobjective.ui

class Menu;

class MultiObjectiveWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit MultiObjectiveWindow(QWidget *parent = nullptr);
    ~MultiObjectiveWindow() override;

private slots:
    void btnCalculate_clicked();
    void btnBack_clicked();

private:
    Ui::wMultiObjective *ui;
};

#endif // MULTIOBJECTIVE_H

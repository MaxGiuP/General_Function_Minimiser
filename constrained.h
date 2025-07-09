// constrained.h
#ifndef CONSTRAINED_H
#define CONSTRAINED_H

#include <QMainWindow>
#include "ui_constrained.h"

class Menu;  // forward

class ConstrainedWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit ConstrainedWindow(QWidget *parent = nullptr);
    ~ConstrainedWindow() override;

private slots:
    void btnCalculate_clicked();
    void btnBack_clicked();

private:
    Ui::wConstrained *ui;
};

#endif // CONSTRAINED_H

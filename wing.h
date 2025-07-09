// wing.h
#ifndef WING_H
#define WING_H

#include <QMainWindow>
#include "ui_wing.h"    // generated from wing.ui

class Menu;  // forward declaration for “Back”

class WingWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit WingWindow(QWidget *parent = nullptr);
    ~WingWindow() override;

private slots:
    void btnCalculate_clicked();
    void btnBack_clicked();

private:
    Ui::wWing *ui;
};

#endif // WING_H

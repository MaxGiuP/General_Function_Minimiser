// manufacturing.h
#ifndef MANUFACTURING_H
#define MANUFACTURING_H

#include <QMainWindow>
#include "ui_manufacturing.h"   // generated from manufacturing.ui :contentReference[oaicite:0]{index=0}

class Menu;  // forward-declare for the “Back” action

class ManufacturingWindow : public QMainWindow {
    Q_OBJECT

public:
    explicit ManufacturingWindow(QWidget *parent = nullptr);
    ~ManufacturingWindow() override;

private slots:
    void btnCalculate_clicked();
    void btnBack_clicked();

private:
    Ui::wManufacturing *ui;    // the auto-generated UI class :contentReference[oaicite:1]{index=1}
};

#endif // MANUFACTURING_H

#ifndef MENU_H
#define MENU_H

#include <QMainWindow>
#include "ui_menu.h"    // your auto-gen header

class Menu : public QMainWindow {
    Q_OBJECT

public:
    explicit Menu(QWidget *parent = nullptr);
    ~Menu() override;

private slots:
    void btnLinear_clicked();
    void btnMultiVariable_clicked();
    void btnGA_clicked();
    void btnConstrained_clicked();
    void btnMultiObjective_clicked();
    void btnWing_clicked();
    void btnManufacturing_clicked();

private:
    Ui::wMenu *ui;
};

#endif // MENU_H

#include "main_menu.h"
#include "ui_main_menu.h"
#include "linear_search.h"

Main_Menu::Main_Menu(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::Main_Menu())
{
    ui->setupUi(this);
}

Main_Menu::~Main_Menu()
{
    delete ui;
}

void Main_Menu::on_btnLinear_clicked()
{
    this->hide();

    linear_search *lin = new linear_search(this);
    lin->show();
    \
}


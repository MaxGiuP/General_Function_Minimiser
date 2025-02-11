#include "multi_variable.h"
#include "ui_multi_variable.h"

multi_variable::multi_variable(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::multi_variable)
{
    ui->setupUi(this);
}

multi_variable::~multi_variable()
{
    delete ui;
}

#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <qmessagebox.h>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pBGRCalc_clicked()
{
    qDebug() << "NIg";
    double x1, x2, x3, x4;
    double phi = 2 - (1 + sqrt(5)) / 2;

    x1 = ui->lEx1->text().toDouble();
    x2 = ui->lEx2->text().toDouble();
    x3 = ui->lEx3->text().toDouble();

    if (x3-x2 > x2-x1)
    {
        x4 = phi * (x3 - x2) + x2;
    }
    else
    {
        x4 = phi * (x2 - x1) + x1;
    }
    ui->lEx4->setText(QString::number(x4));

}


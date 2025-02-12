#ifndef MAIN_MENU_H
#define MAIN_MENU_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class Main_Menu;
}
QT_END_NAMESPACE

class Main_Menu : public QMainWindow
{
    Q_OBJECT

public:
    explicit Main_Menu(QWidget *parent = nullptr);
    ~Main_Menu();

private slots:
    void on_btnLinear_clicked();

    void on_btnMulti_clicked();

private:
    Ui::Main_Menu *ui;
};

#endif // MAIN_MENU_H

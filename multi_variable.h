#ifndef MULTI_VARIABLE_H
#define MULTI_VARIABLE_H

#include <QMainWindow>

namespace Ui {
class multi_variable;
}

class multi_variable : public QMainWindow
{
    Q_OBJECT

public:
    explicit multi_variable(QWidget *parent = nullptr);
    ~multi_variable();

private:
    Ui::multi_variable *ui;
};

#endif // MULTI_VARIABLE_H

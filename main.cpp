#include <Python.h>
#include <QApplication>
#include <QDir>
#include "menu.h"

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    Py_Initialize();

    // ─── Insert the *source* root, two levels up from the exe ───
    {
        QDir exeDir(QCoreApplication::applicationDirPath());
        exeDir.cdUp();            // .../build/Desk-Debug
        exeDir.cdUp();            // .../Optimiser (your project root)
        QString projectRoot = exeDir.absolutePath();

        PyObject* sysPath = PySys_GetObject("path");  // borrowed ref
        PyObject* pyPath  = PyUnicode_FromString(projectRoot.toUtf8().constData());
        PyList_Insert(sysPath, 0, pyPath);
        Py_DECREF(pyPath);
    }

    // Now Menu can import Optimisers.*
    Menu w;
    w.show();

    int ret = app.exec();
    Py_Finalize();
    return ret;
}

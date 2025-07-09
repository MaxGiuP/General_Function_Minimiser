// python_utils.cpp
// python_utils.cpp
extern "C" {
#  include <Python.h>
}
#include "python_utils.h"

QString callPythonFunction(
    const QString &moduleName,
    const QString &functionName,
    const QStringList &args
    ) {

    PyObject *pName = PyUnicode_FromString(moduleName.toUtf8().constData());
    PyObject *pModule = PyImport_Import(pName);
    Py_DECREF(pName);
    if (!pModule) {
        PyErr_Print();
        return "Error: could not import " + moduleName;
    }

    PyObject *pFunc = PyObject_GetAttrString(pModule, functionName.toUtf8().constData());
    if (!pFunc || !PyCallable_Check(pFunc)) {
        PyErr_Print();
        Py_XDECREF(pFunc);
        Py_DECREF(pModule);
        return "Error: no function " + functionName;
    }

    // Build Python tuple of arguments
    PyObject *pArgs = PyTuple_New(args.size());
    for (int i = 0; i < args.size(); ++i) {
        const QString &s = args[i];
        bool okInt = false;
        long long intVal = s.toLongLong(&okInt);

        PyObject *pValue = nullptr;
        if (okInt) {
            // it was an integer
            pValue = PyLong_FromLongLong(intVal);
        } else {
            bool okFloat = false;
            double dblVal = s.toDouble(&okFloat);
            if (okFloat) {
                // it was a float
                pValue = PyFloat_FromDouble(dblVal);
            } else if (s == "1" || s == "0") {
                // explicit boolean
                pValue = PyBool_FromLong(s == "1");
            } else {
                // fallback to string
                pValue = PyUnicode_FromString(s.toUtf8().constData());
            }
        }

        if (!pValue) {
            // should never happen, but guard
            pValue = Py_None;
            Py_INCREF(pValue);
        }
        PyTuple_SetItem(pArgs, i, pValue);  // steals reference
    }


    PyObject *pResult = PyObject_CallObject(pFunc, pArgs);
    Py_DECREF(pArgs);
    Py_DECREF(pFunc);
    Py_DECREF(pModule);

    if (!pResult) {
        PyErr_Print();
        return "Error: call failed";
    }

    // Expect a string result
    const char *resC = PyUnicode_AsUTF8(pResult);
    QString result = resC ? QString::fromUtf8(resC) : "Error: bad return";
    Py_DECREF(pResult);
    return result;
}

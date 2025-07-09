// python_utils.h
#ifndef PYTHON_UTILS_H
#define PYTHON_UTILS_H

#include <QString>
#include <QStringList>

// callPythonFunction is defined in python_utils.cpp
QString callPythonFunction(
    const QString &moduleName,
    const QString &functionName,
    const QStringList &args
    );

#endif // PYTHON_UTILS_H

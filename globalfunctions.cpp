#include "globalfunctions.h"
#include <QRegularExpression>
#include <QString>
#include <QStack>
#include <cmath>

double evaluateExpression(QString f)
{
    f.replace(" ", "");

    int startPos = f.lastIndexOf("(");
    while (startPos != -1) {
        int endPos = f.indexOf(")", startPos);
        if (endPos == -1) {
            qWarning() << "Mismatched parentheses!";
            return 0;
        }

        QString subExpr = f.mid(startPos + 1, endPos - startPos - 1);
        double result = evaluateExpression(subExpr);  // Recursively evaluate

        f.replace(startPos, endPos - startPos + 1, QString::number(result));

        startPos = f.lastIndexOf("(");
    }

    QRegularExpression regExp("(\\d*\\.?\\d+|[+\\-*/^])");
    QRegularExpressionMatchIterator iter = regExp.globalMatch(f);
    QStringList tokens;

    while (iter.hasNext()) {
        QRegularExpressionMatch match = iter.next();
        tokens << match.captured(0);
    }

    for (int i = 0; i < tokens.size(); ++i) {
        if (tokens[i] == "^") {
            double left = tokens[i - 1].toDouble();
            double right = tokens[i + 1].toDouble();
            double result = std::pow(left, right);
            tokens.replace(i - 1, QString::number(result));
            tokens.removeAt(i);
            tokens.removeAt(i);
            i--;
        }
    }

    for (int i = 0; i < tokens.size(); ++i) {
        if (tokens[i] == "*" || tokens[i] == "/") {
            double left = tokens[i - 1].toDouble();
            double right = tokens[i + 1].toDouble();
            double result = 0;

            if (tokens[i] == "*") {
                result = left * right;
            } else if (tokens[i] == "/") {
                if (right != 0) {
                    result = left / right;
                } else {
                    qWarning() << "Division by zero!";
                    return 0;
                }
            }

            tokens.replace(i - 1, QString::number(result));
            tokens.removeAt(i);
            tokens.removeAt(i);
            i--;
        }
    }

    double result = tokens[0].toDouble();
    for (int i = 1; i < tokens.size(); i += 2) {
        QString op = tokens[i];
        double value = tokens[i + 1].toDouble();

        if (op == "+") {
            result += value;
        } else if (op == "-") {
            result -= value;
        }
    }

    return result;
}


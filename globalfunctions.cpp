#include "globalfunctions.h"
#include <QRegularExpression>
#include <QString>
#include <QStack>
#include <cmath>
#include <QDebug>

double evaluateExpression(QString f)
{
    // Remove spaces, handle double negatives and leading minus
    f.replace(" ", "");
    while (f.contains("--")) {
        f.replace("--", "+");
    }
    if (f.startsWith("-")) {
        f = "0" + f;
    }
    f.replace("(-", "(0-");

    // Handle parenthesized expressions recursively
    int startPos = f.lastIndexOf("(");
    while (startPos != -1) {
        int endPos = f.indexOf(")", startPos);
        if (endPos == -1) {
            qWarning() << "Mismatched parentheses!";
            return 0;
        }
        QString subExpr = f.mid(startPos + 1, endPos - startPos - 1);
        double subResult = evaluateExpression(subExpr);
        f.replace(startPos, endPos - startPos + 1, QString::number(subResult));
        startPos = f.lastIndexOf("(");
    }

    QRegularExpression tokenRegex("(?:(?<=^)|(?<=[(*/]))-\\d*\\.?\\d+|\\d*\\.?\\d+|[+\\-*/^]");
    QRegularExpressionMatchIterator iter = tokenRegex.globalMatch(f);
    QStringList tokens;
    while (iter.hasNext()) {
        QRegularExpressionMatch match = iter.next();
        tokens << match.captured(0);
    }
    if (tokens.isEmpty()) {
        return 0;
    }

    // Process exponentiation '^'
    for (int i = 0; i < tokens.size(); ++i) {
        if (tokens[i] == "^") {
            // Ensure we have a left and right operand
            if (i > 0 && i < tokens.size() - 1) {
                double left = tokens[i - 1].toDouble();
                double right = tokens[i + 1].toDouble();
                double power = std::pow(left, right);
                tokens[i - 1] = QString::number(power);
                tokens.removeAt(i);     // remove '^'
                tokens.removeAt(i);     // remove right operand
                i--; // step back to re-check
            }
        }
    }

    // Process multiplication/division
    for (int i = 0; i < tokens.size(); ++i) {
        if (tokens[i] == "*" || tokens[i] == "/") {
            // Ensure we have valid left and right operands
            if (i > 0 && i < tokens.size() - 1) {
                double left = tokens[i - 1].toDouble();
                double right = tokens[i + 1].toDouble();
                double result = 0;
                if (tokens[i] == "*") {
                    result = left * right;
                } else {  // tokens[i] == "/"
                    if (right == 0.0) {
                        qWarning() << "Division by zero!";
                        return 0;
                    }
                    result = left / right;
                }
                tokens[i - 1] = QString::number(result);
                tokens.removeAt(i);     // remove operator
                tokens.removeAt(i);     // remove right operand
                i--; // step back to re-check
            }
        }
    }

    // Process addition '+' and subtraction '-'
    if (tokens.size() % 2 == 0) {
        qWarning() << "Tokens count is even.";
        //return 0;
    }
    double result = tokens[0].toDouble();
    for (int i = 1; i + 1 < tokens.size(); i += 2) {
        QString op = tokens[i];
        double operand = tokens[i + 1].toDouble();
        if (op == "+") {
            result += operand;
        } else if (op == "-") {
            result -= operand;
        }
    }

    return result;
}

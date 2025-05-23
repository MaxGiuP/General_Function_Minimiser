#!/bin/bash

echo "Converting .ui files to Python..."
for file in *.ui; do
    out="ui_${file%.ui}.py"
    echo " → $file → $out"
    pyside6-uic "$file" -o "$out"
done
echo "UI conversion complete."

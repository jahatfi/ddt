#!/bin/bash

# Check if a filename is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <python_file>"
    exit 1
fi

PYTHON_FILE=$1

# Run pylint and store the output
OUTPUT=$(poetry run pylint "$PYTHON_FILE" 2>&1)

# Initialize counters
ERRORS=0
WARNINGS=0
CONVENTIONS=0
REFS=0
INFO=0

SCORE=0

echo "Examining each line:"
# Parse the pylint output
while IFS= read -r line; do
    echo "$line"
    if [[ $line == *": E"* ]]; then
        ((ERRORS++))
    elif [[ $line == *": W"* ]]; then
        ((WARNINGS++))
    elif [[ $line == *": C"* ]]; then
        ((CONVENTIONS++))
    elif [[ $line == *": R"* ]]; then
        ((REFS++))
    elif [[ $line == *": I"* ]]; then
        ((INFO++))
    elif [[ $line == "Your code has been rated"* ]]; then
         SCORE=$(echo "$line" | grep -oP '\d+\.\d+')
    fi
done <<< "$OUTPUT"

# Output the counts
echo "Pylint Report for $PYTHON_FILE"
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"
echo "Convention: $CONVENTIONS"
echo "Refactor: $REFS"
echo "Info: $INFO"
echo "Score: $SCORE"

chmod +x ./get_color.sh 
COLOR=$(./get_color.sh 0 10 $SCORE)

echo "ERRORS=$ERRORS" >> "$GITHUB_OUTPUT"
echo "WARNINGS=$WARNINGS" >> "$GITHUB_OUTPUT"
echo "CONVENTIONS=$CONVENTIONS" >> "$GITHUB_OUTPUT"
echo "REFS=$REFS" >> "$GITHUB_OUTPUT"
echo "INFO=$INFO" >> "$GITHUB_OUTPUT"
echo "SCORE=$SCORE" >> "$GITHUB_OUTPUT"
echo "MSG=$ERRORS error(s), $WARNINGS warning(s), $CONVENTIONS convention message(s), $REFS reference(s), and $INFO info message(s)" >> "$GITHUB_OUTPUT"
echo "COLOR=$COLOR" >> "$GITHUB_OUTPUT"
#!/bin/bash

# Check if a filename is provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <python_file> <loc>"
    exit 1
fi

FILE="$1"
echo "FILE = $FILE"
lines_of_code="$2"
echo "loc = $lines_of_code"

# Check if the file exists
if [ ! -f "$FILE" ]; then
    echo "File not found: $FILE"
    exit 1
fi

# Ensure valid loc value
if [ $lines_of_code -le 0 ]; then
    echo "No lines of code to analyze."
    exit 2
fi


get_color() {
    local percentage=$1

    if (( $(echo "$percentage > 10" | bc -l) )); then
        echo "red"
    elif (( $(echo "$percentage > 5" | bc -l) )); then
        echo "orange"
    elif (( $(echo "$percentage > 2.5" | bc -l) )); then
        echo "yellow"
    elif (( $(echo "$percentage > 0" | bc -l) )); then
        echo "90EE90"
    else
        echo "green"
    fi
}

# Run mypy and count the number of errors reported by mypy
error_count=$(poetry run mypy "$FILE" 2>&1 | grep -c 'error:')

percentage=$(echo "scale=4; ($error_count / $lines_of_code) * 100" | bc)

color=$(get_color $percentage)

# Print the results
echo "Lines of code: $lines_of_code"
echo "Mypy errors: $error_count"
echo "Percentage of mypy errors: $percentage%"
echo "color=$color"

echo "COLOR=$color" >> "$GITHUB_OUTPUT"
echo "DATA=$error_count error(s) ($percentage% by LoC)" >> "$GITHUB_OUTPUT"

return $error_count
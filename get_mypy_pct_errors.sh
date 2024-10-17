#!/bin/bash

# Check if a filename is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <python_file>"
    exit 1
fi

FILE="$1"
echo "FILE = $FILE"

# Check if the file exists
if [ ! -f "$FILE" ]; then
    echo "File not found: $FILE"
    exit 1
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
        echo "lightgreen"
    else
        echo "green"
    fi
}

# Run mypy and count the number of errors reported by mypy
error_count=$(poetry run mypy "$FILE" 2>&1 | grep -c 'error:')

# Count the number of lines of code (excluding comments and blank lines) using cloc
lines_of_code=$(cloc "$FILE" | tail -n 2 | head -n 1 | awk '{print $NF}')
echo "loc = $lines_of_code"

# Calculate the percentage of errors per line of code
if [ $lines_of_code -eq 0 ]; then
    echo "No lines of code to analyze."
    exit 1
fi
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
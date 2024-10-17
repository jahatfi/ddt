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

# Run mypy and capture the output
OUTPUT=$(mypy "$FILE" 2>&1)

# Count the number of lines of code (excluding comments and blank lines) using cloc
lines_of_code=$(cloc "$FILE" | tail -n 3 | head -n 1 | awk '{print $NF}'
echo "loc = $lines_of_code"

# Count the number of errors reported by mypy
error_count=$(echo "$OUTPUT" | grep -c 'error:')

# Calculate the percentage of errors per line of code
if [ $lines_of_code -eq 0 ]; then
    echo "No lines of code to analyze."
    exit 1
fi

percentage=$(echo "scale=2; ($error_count / $lines_of_code) * 100" | bc)

# Print the results
echo "Lines of code: $lines_of_code"
echo "Mypy errors: $error_count"
echo "Percentage of mypy errors: $percentage%"

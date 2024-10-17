#!/bin/bash
# Chaptgpt

# Check for the correct number of arguments
if [ "$#" -ne 3 ]; then
  echo "Usage: $0 <min> <max> <measured>"
  exit 1
fi

# Read input arguments
min_value=$1
max_value=$2
measured_value=$3

# Calculate the range
range=$(echo "$max_value - $min_value" | bc)

# Calculate percentage of the measured value within the range
if [ $(echo "$range == 0" | bc) -eq 1 ]; then
  echo "Error: The minimum and maximum values must be different."
  exit 1
fi

percentage=$(echo "scale=4; ($measured_value - $min_value) / $range" | bc)

# Determine the color based on the measured value
if (( $(echo "$percentage <= 0.5" | bc -l) )); then
  echo "red"
elif (( $(echo "$percentage >= 1.0" | bc -l) )); then
  echo "green"
else
  # Calculate intervals
  if (( $(echo "$percentage <= 0.6667" | bc -l) )); then
    echo "orange"
  elif (( $(echo "$percentage <= 0.8333" | bc -l) )); then
    echo "yellow"
  else
    # light green
    echo "90EE90"
  fi
fi

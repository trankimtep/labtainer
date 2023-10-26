#!/bin/bash

# Function to perform addition
add() {
  result=$(($1 + $2))
  echo "Result: $1 + $2 = $result"
}

# Function to perform subtraction
subtract() {
  result=$(($1 - $2))
  echo "Result: $1 - $2 = $result"
}

# Function to perform multiplication
multiply() {
  result=$(($1 * $2))
  echo "Result: $1 * $2 = $result"
}

# Function to perform division
divide() {
  if [ $2 -eq 0 ]; then
    echo "Error: Division by zero is not allowed."
  else
    result=$(awk "BEGIN {printf \"%.2f\", $1 / $2}")
    echo "Result: $1 / $2 = $result"
  fi
}

# Main script starts here
if [ $# -ne 3 ]; then
  echo "Usage: ./calculator.sh <number1> <operator> <number2>"
  exit 1
fi

num1=$1
operator=$2
num2=$3

case $operator in
  +)
    add $num1 $num2
    ;;
  -)
    subtract $num1 $num2
    ;;
  *)
    case $operator in
      *)
        echo "Error: Invalid operator. Use +, -, *, or /."
        ;;
    esac
    ;;
esac

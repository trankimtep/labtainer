import os
import re

# Function to check if the input string represents a correct calculation
def is_valid_calculation(input_str):
    # Remove all spaces from the input string
    input_str = input_str.replace(" ", "")
    
    # Define a regular expression pattern to match valid calculations
    pattern = r'^Result:(\d+)([+\-*/])(\d+)=(\d+)$'
    
    # Check if the input matches the pattern
    if re.match(pattern, input_str):
        num1, operator, num2, expected_result = re.findall(pattern, input_str)[0]
        num1, num2, expected_result = int(num1), int(num2), int(expected_result)
        
        # Calculate the actual result
        if operator == '+':
            actual_result = num1 + num2
        elif operator == '-':
            actual_result = num1 - num2
        elif operator == '*':
            actual_result = num1 * num2
        elif operator == '/':
            actual_result = num1 / num2

        # Compare the actual and expected results
        return actual_result == expected_result
    else:
        return False

# Directory where the files are located
directory = "/home/ubuntu/.local/result/"

# Function to find the latest file with the specified prefix
def find_latest_file(dir_path, prefix):
    latest_file = None
    latest_timestamp = 0
    
    for filename in os.listdir(dir_path):
        if filename.startswith(prefix):
            timestamp = int(re.search(r'\d{14}', filename).group())
            if timestamp > latest_timestamp:
                latest_timestamp = timestamp
                latest_file = filename
    
    return latest_file

# Find the latest file in the specified directory
latest_filename = find_latest_file(directory, "caculator.sh.stdout.")
if latest_filename:
    latest_file_path = os.path.join(directory, latest_filename)
    
    # Read the first line from the latest file
    with open(latest_file_path, 'r') as file:
        first_line = file.readline()
    
    # Check the calculation from the first line
    result = is_valid_calculation(first_line)
    
    # Write the result to /etc/result
    with open("/etc/result", 'w') as result_file:
        result_file.write("true" if result else "false")

#    print("Result: {} written to /etc/result.".format("true" if result else "false"))
else:
    print("No matching files found.")

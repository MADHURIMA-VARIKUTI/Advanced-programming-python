import os
import ast

def extsort(file_list):
    return sorted(file_list, key=lambda x: os.path.splitext(x)[1])

try:
    with open("D:\\210953314\\lab7\\a2.txt", 'r') as file:
        input_str = file.read()
        # Use ast.literal_eval to safely evaluate the input string as a Python expression
        input_list = ast.literal_eval(input_str)
        
        # Ensure that the input_list is a list
        if not isinstance(input_list, list):
            raise ValueError("Input is not a list.")

        # Sort the list based on extensions
        sorted_files = extsort(input_list)
        print(sorted_files)
except FileNotFoundError:
    print("Input file 'input.txt' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

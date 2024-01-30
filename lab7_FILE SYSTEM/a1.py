# Function to print each line of a file in reverse order
def print_lines_in_reverse(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                reversed_line = line.strip()[::-1]  # Reverse the line and strip trailing newline
                print(reversed_line)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace 'your_file.txt' with the path to your input file
print_lines_in_reverse('D:\\210953314\\lab7\\madhu_input.txt')


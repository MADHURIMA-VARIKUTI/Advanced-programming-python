   # Dictionary with line numbers as keys and [string, length] as values:
# {1: ['line one.', 9], 2: ['two.', 4], 3: ['three', 5], 4: ['four.', 5], 5: ['Five .', 6], 6: ['Sixth.', 6], 7: ['seven.', 6], 8: ['Last 8.', 7]}

# Dictionary with letter frequencies:
# {'l': 2, 'i': 3, 'n': 3, 'e': 7, 'o': 3, 't': 4, 'w': 1, 'h': 2, 'r': 2, 'f': 2, 'u': 1, 'v': 2, 's': 3, 'x': 1, 'a': 1}
    
def main():
    with open("sample.txt", "w") as file:
        file.write(" line 1.\n")
        file.write("Hello from line 2.\n")
        file.write("Line 3 is here!\n")
        file.write("Python programming is great.\n")
        file.write("Fifth line is short.\n")
        file.write("Sixth line, testing.\n")
        file.write("Lucky number seven.\n")
        file.write("Last line, number 8.\n")
    lines = []
    with open("sample.txt", "r") as file:
        lines = file.readlines()
    line_data_dict = {}
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        line_length = len(line)
        line_data_dict[line_number] = [line, line_length]
    print("Dictionary with line numbers as keys and [string, length] as values:")
    print(line_data_dict)
    letter_frequency_dict = {}
    for line in lines:
        for char in line:
            if char.isalpha():
                char_lower = char.lower()
                if char_lower in letter_frequency_dict:
                    letter_frequency_dict[char_lower] += 1
                else:
                    letter_frequency_dict[char_lower] = 1
    print("\nDictionary with letter frequencies:")
    print(letter_frequency_dict)
if __name__ == "__main__":
    main()
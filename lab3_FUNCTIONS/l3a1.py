def count_upper_lower_characters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

sample_string = input("Enter a string: ")
upper_count, lower_count = count_upper_lower_characters(sample_string)
print(f"No. of Upper case characters: {upper_count}")
print(F"No. of Lower case characters: {lower_count}")

# formatted string literal;format your string that is more readable and fast.

# Enter a string: The quick Brow Fox
# No. of Upper case characters: 3
# No. of Lower case characters: 12
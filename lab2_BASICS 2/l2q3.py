import random
def main():
    dictionary = {}
    n = int(input("Enter the number of key-value pairs: "))

    for _ in range(n):
        
        key = random.randrange(0, 100)
        value = input(f"Enter value for key {key}: ")
        dictionary[key] = value

    total_numbers = 0
    total_sum = 0
    concatenated_strings = ""
    special_char_strings = []

    for value in dictionary.values():

        if value.isdigit():
            total_numbers += 1
            total_sum += int(value)
        elif isinstance(value, str):
            concatenated_strings += value
            if all(char in "!@#$%^&*()_+[]{}|;':,.<>?/~`" for char in value):
                special_char_strings.append(value)
    
    if total_numbers > 0:
        average = total_sum / total_numbers
        print(f"Average of numeric values: {average}")
    print(f"Concatenated string: {concatenated_strings}")
    search_value = input("Enter a value to search for: ")
    found_keys = [key for key, value in dictionary.items() if value == search_value]
    
    if found_keys:
        print(f"Keys with value '{search_value}': {found_keys}")
    else:
        print(f"No keys found with value '{search_value}'")

    print("Values with only special characters:")

    for value in special_char_strings:
        print(value)
        
if __name__ == "__main__":

    main()
    
    # The variable __name__ for the file/module that is run will be always __main__. 
    # But the __name__ variable for all other modules that are being imported will be set to their module's name.
    
# Enter the number of key-value pairs: 6
# Enter value for key 41: 15
# Enter value for key 48: madhu
# Enter value for key 1: $@
# Enter value for key 39: @maha
# Enter value for key 69: 1
# Enter value for key 24: 1q2w
# Average of numeric values: 8.0
# Concatenated string: madhu$@@maha1q2w
# Enter a value to search for: 1
# Keys with value '1': [69]
# Values with only special characters:
# $@
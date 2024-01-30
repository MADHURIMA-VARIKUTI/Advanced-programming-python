def outer_function(x):
    def inner_function(y):
        return y**3
    result = inner_function(x)
    return result

input_value = int(input("Enter a number: "))
output = outer_function(input_value)
print("Result:", output)

# Enter a number: 4
# Result: 64
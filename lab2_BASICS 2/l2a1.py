cache = {}
def expensive_calculation(n):

    if n in cache:
        print(f"Using cached result for {n}")
        return cache[n]
    result = n * n
    cache[n] = result
    print(f"Calculated result for {n}")
    return result

N = int(input("Input the number of digits to be taken: "))
number = input("Input the digits: ")

for num in number:
    num_as_int = int(num)
    result = expensive_calculation(num_as_int)
    print(f"Result for {num_as_int}: {result}")
    
#     Input the number of digits to be taken: 4
# Input the digits: 1234
# Calculated result for 1
# Result for 1: 1
# Calculated result for 2
# Result for 2: 4
# Calculated result for 3
# Result for 3: 9
# Calculated result for 4
# Result for 4: 16
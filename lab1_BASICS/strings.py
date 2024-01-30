n = int(input("Enter no.of strings: "))
str_list = [input() for _ in range(n)]
count = 0
for string in str_list:
    if string.endswith(string[0]) and len(string) > 1:
        count += 1
print("number of strings with same first and last char: ", count)
print("odd length strings: ")
[print(string) for string in str_list if len(string)%2 != 0]

# Enter no.of strings: 4
# aa
# abca
# cgc
# f
# number of strings with same first and last char:  3
# odd length strings:
# cgc
# f
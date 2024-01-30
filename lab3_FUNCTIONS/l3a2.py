n = int(input("Enter the number of rows: "))
for i in range(n):
    coef = 1
    for j in range(1, n - i + 1):
        print(" ", end="")
    
    for j in range(0, i + 1):
        if j > 0:
            coef = coef * (i - j + 1) // j
        print(coef, end=" ")
    print()
#C(n, k) = n! / (k! * (n - k)!)
# nCr formula i.e. n!/(n-r)!r!

# Enter the number of rows: 5
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1

#            0C0
#        1C0   1C1
#     2C0   2C1   2C2
#  3C0   3C1   3C2    3C3
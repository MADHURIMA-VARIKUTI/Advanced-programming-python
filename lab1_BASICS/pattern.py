n = int(input("Enter no.of rows: "))
start = 1
for i in range(n):
    for j in range(i+1):
        print(start, end = '\t')
        start+=1
    print('\n')
    # nested loops [pattern ex]
    
#     Enter no.of rows: 5
# 1

# 2       3

# 4       5       6

# 7       8       9       10

# 11      12      13      14      15
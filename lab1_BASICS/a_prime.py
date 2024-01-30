n,m=map(int,input("enter n and m:").split())
prime_nums=[]
for i in range(n,m+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
         prime_nums.append(i)
print(prime_nums)    

# enter n and m:1 11
# [1, 2, 3, 5, 7, 11]
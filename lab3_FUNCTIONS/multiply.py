def multiply(items):
   tot_product=1
   for num in items:
       tot_product*=num
   return tot_product
li=list(map(int,input("enter elements in the list: \n").split()))
print("product of all numbers",multiply(li))   

# enter elements in the list: 
# 2 -1 5 -9
# product of all numbers 90

  

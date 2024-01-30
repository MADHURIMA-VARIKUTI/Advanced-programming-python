def multiply(items):
   tot_product=1
   for num in items:
       tot_product*=num
   return tot_product
li=list(map(int,input("enter elements in the list: \n").split()))
print("product of all numbers",multiply(li)) 

# enter elements in the list: 
# -1 -2 3 4
# product of all numbers 24

# def multiply_list_numbers(numbers_list):
#     result = 1  
#     for num in numbers_list:
#         result *= num
#     return result

# list = []
# n = int(input("enter the number of elements:"))
# for i in range(0,n):
#     element = int(input())
#     list.append(element)

# result = multiply_list_numbers(list)
# print("result:", result)


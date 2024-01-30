list_inp = list(map(int, input("Enter elements in the list: ").split()))
res_list = []
for item in list_inp: 
    if item not in res_list: 
        res_list.append(item) 
print("Unique elements of the list using append():\n")    
for item in res_list: 
    print(item)
    
#     Enter elements in the list: 44 55 33 44 33 77
# Unique elements of the list using append():

# 44
# 55
# 33
# 77


# using set->eliminates duplicates
# def uniqueElements(nums):
# return list(set(nums))  
# l = list(map(int, input("Enter elements in the list: ").split()))
# print("All Unique Elements: ", uniqueElements(l))


list_inp = list(map(int, input("Enter elements in the list: ").split()))
res_list = []
for item in list_inp: 
    if item not in res_list: 
        res_list.append(item) 
print("Unique elements of the list using append():\n")    
for item in res_list: 
    print(item)
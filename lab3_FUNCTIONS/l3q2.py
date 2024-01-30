def unique(lst):
    print(set(lst))

input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [item for item in input_str.split()]
unique(input_list)

# Enter a list of numbers separated by spaces: 11 22 33 11 22 
# {'22', '33', '11'}


# list_inp = list(map(int, input("Enter elements in the list: ").split()))
# res_list = []
# for item in list_inp:
#     if item not in res_list:
#         res_list.append(item)
# print("Unique elements of the list using append():\n")    
# for item in res_list:
#     print(item)
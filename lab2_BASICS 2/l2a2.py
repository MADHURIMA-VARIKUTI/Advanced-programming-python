def find_union(list1, list2):
    union = []
    for item in list1:
        if item not in union:
            union.append(item)
    for item in list2:
        if item not in union:
            union.append(item)
    return union

def find_intersection(list1, list2):
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection

def find_difference(list1, list2):
    difference = []
    for item in list1:
        if item not in list2 and item not in difference:
            difference.append(item)
    return difference

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 9]

union_result = find_union(list1, list2)
intersection_result = find_intersection(list1, list2)
difference_result = find_difference(list1, list2)

print("Union:", union_result)
print("Intersection:", intersection_result)
print("Difference:", difference_result)

# Union: [1, 2, 3, 4, 5, 6, 7, 9]
# Intersection: [4, 5]
# Difference: [1, 2, 3]
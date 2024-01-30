list1=list(map(int,input("enter the elements in LIST 1:").split()))
list2=list(map(int,input("enter the elements in LIST 2:").split()))
# map() function 
# applies int to each string element in the input
# to wrap each element present in the string and convert them to the desired data type (say int).#
list3=[]
for num in list1:
  if num%2 == 1:
      list3.append(num)
      
for num in list2:
    if num%2 ==0:
        list3.append(num)
        
print("List 3 with odd num from l1 and even num from l2 is",list3)                


# enter the elements in LIST 1:1 5 3 8
# enter the elements in LIST 2:1 9 0 2
# List 3 with odd num from l1 and even num from l2 is [1, 5, 3, 0, 2]
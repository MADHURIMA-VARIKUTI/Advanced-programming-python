import re

text=dir(re)

res=[]
for function in text:
    if function.__contains__('find'):
        res.append(function)
res=sorted(res)
print(res)

# ['findall', 'finditer']

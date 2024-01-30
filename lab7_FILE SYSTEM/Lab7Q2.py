fileObj = open("madhu_input.txt","r")
myDict = {}
Lines = fileObj.readlines()
for line in Lines:
    words= line.split()
    for word in words:
        if word not in myDict:
            myDict[word] = 1
        else:
            myDict[word] = myDict[word]+1


print(myDict)

# {'This': 1, 'is': 1, 'madhurima': 1, 'from': 2, 'cce': 1, 'branch': 1, 'andhra': 1, 'pradesh': 1}

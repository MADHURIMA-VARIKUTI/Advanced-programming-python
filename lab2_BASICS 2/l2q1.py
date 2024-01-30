count = {}
sentence = input("Enter a Line : ")
list_of_words = sentence.split()
for word in list_of_words:
    count[word] = count.get(word, 0) + 1
print('Frequency')
for key in count.keys():
    print(key, count[key])
    
#     Enter a Line : Hi I'm madhu and I'm studying in MIT and sec CCEB 
# Frequency
# Hi 1
# I'm 2
# madhu 1
# and 2
# studying 1
# in 1
# MIT 1
# sec 1
# CCEB 1


# string = input("Please enter any String : ")
# words = []
# words = string.split()
# frequency = [words.count(i) for i in words]
# myDict = dict(zip(words, frequency))
# print("Dictionary Items  :  ",  myDict)



# Using the zip operation, we are able to match the first word of the word list
# with the first number in the frequency list, the second word and second frequency n so on
import re

reg = r'^[a-z]$|^([a-z]).*\1$'

string = input("Enter String: ")
if(re.search(reg, string)): 
    print("Valid") 
else: 
    print("Invalid")


    # Enter String: amadhua
    # Valid

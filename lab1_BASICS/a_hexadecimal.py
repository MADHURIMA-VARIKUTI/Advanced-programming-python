h=input("enter the hexadecimal number:")
for char in h:
    if(char>='0' and char<='9') or (char>='A' and char<='F'):
        continue
    else:
        print("not hexadecimal number")
        #12G4F5
        break
else:
    print("hexadecimal number")
     # ABCD1234
     
#enter the hexadecimal number:12G4F5
# not hexadecimal number
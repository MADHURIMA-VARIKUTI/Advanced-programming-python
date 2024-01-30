from datetime import datetime

name=input("Enter your name:")
time= datetime.now()
print("Time now !!:",time)

if(time.hour>=12 and time.hour<16):
    print("Good afternoon!",name)
elif(time.hour>=16 and time.hour<20):
    print("Good evening!",name)
elif(time.hour>=20 and time.hour<5):
    print("Good night!",name)
elif(time.hour>=5 and time.hour<12):
    print("Good morning!",name)

# Enter your name:VARIKUTI MADHURIMA
# Time now !!: 2023-09-13 11:29:27.843459
# Good morning! VARIKUTI MADHURIMA
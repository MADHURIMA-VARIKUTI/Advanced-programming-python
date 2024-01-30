import math

def funcmod(a):
    rad= (math.pi/180)*a
    sinval=math.sin(rad)
    sqrtval= math.sqrt(a)
    logval=math.log(a,10)
    print("The sin value of the number is:",sinval,", The square root of the number is:",sqrtval,", The log of the number is:",logval)



a=int(input("Enter the number:"))
funcmod(a)

# Enter the number:144
# The sin value of the number is: 0.5877852522924732 , The square root of the number is: 12.0 , The log of the number is: 2.1583624920952493
    
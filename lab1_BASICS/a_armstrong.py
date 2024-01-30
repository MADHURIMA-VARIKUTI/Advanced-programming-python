num=153
# 153 = 1*1*1 + 5*5*5 + 3*3*3 =153
order=len(str(num))
sum=0
temp=num
while temp!=0:
    digit=temp%10
    sum+=digit**order
    temp//=10

if(num==sum):
    print(num,"is an armstrong number!")  
else:
     print(num,"Not an armstrong number!")      
     
    #  153 is an armstrong number!
x=int(input("enter number to check it is armstrong or not"))
temp=x
digit=0
sum=0
while(temp>0):
    digit+=1
    temp//=10
print(digit)
temp=x
for i in range(1,digit+1):
    rem=temp%10
    temp=temp//10
    sum=sum+(rem**digit)
print(sum)    
if(sum==x):
    print(x,"is armstong number")
else:
    print(x,"is not armstrong number")

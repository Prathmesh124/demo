evena=[]
for i in range(45,68):
    if(i%2==0):
        evena.append(i)
print(evena)
print(evena[::-1])

#prime
a=[9,5,8,9,7,11,8,13,10,24]
check=True
k=[]
num=0
for i in a:
    num= i 
    for j in range(2,num//2): #9
        if(num%j==0):
            check = False
            break
    if(check==True):
        k.append(i)
    check=True    
print(k)


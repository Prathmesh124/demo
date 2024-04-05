llimit = int(input("Enter the 1st num : ")) #10
ulimit = int(input("Enter the 2nd num : ")) #30
count = 0
for j in range(llimit,ulimit+1): #10
    num = j #10
    check = True
    for i in range(2,num): #9
        if(num%i==0):
            check = False
            break
       
    if(check==True):
        print(j,end=" ")
        count+=1
   
print("These are the numbers between prime numbers b/w",llimit ,"and",ulimit,"is",count)


 
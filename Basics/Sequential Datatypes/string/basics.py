#ordinal ord() it will give you ascii value
#without function
#swapcase
name="India Is Great Country"
for i in name:
    if ord(i)>96 and ord(i)<123:
        print(chr(ord(i)-32),end="")
    elif ord(i)>64 and ord(i)<91:
        print(chr(ord(i)+32),end="")
    else:
        print(i,end="") 

print("")
#upper case
for i in name:
    if ord(i)>96 and ord(i)<123:
        print(chr(ord(i)-32),end="")
    else:
        print(i,end="")
print("")
#lower case
for i in name:
    if ord(i)>64 and ord(i)<91:
        print(chr(ord(i)+32),end="")
    else:
        print(i,end="")  

#chr is a function which converts ordinal value to string
#ord() it gives ascii value of all string
        # it is used like ord(i)
        #here i is character

#pre, suffix

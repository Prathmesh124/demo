#area of rectangle and perimeter
x= int(input("enter length number"))
y=int(input("enter breath number"))
print("area of rectangle is",x*y)
print("perimeter of rectangle is",2*(x+y))

#area of circle and circumference
r= int(input("enter radius of circle"))
print("area of circle is",(22*r*r)/7)
print("area of circle is",(2*22*r)/7)

#area,volume ,perimeter of rectangle and perimeter
l= int(input("enter length number"))
b=int(input("enter breath number"))
h=int(input("enter height number"))

print("volume of rectangle is",l**3)
print("perimeter of rectangle is",12*l)
print("area of rectangle is",6*(l*l))

#Generate two random integers within a specified range (e.g., 1-10).
#Ask the user to perform a basic mathematical operation on those numbers (e.g., add, subtract, multiply, divide) by displaying the operation symbol (+, -, *, /).
#Get the user's answer as an integer.
#Calculate the correct answer using the generated numbers and chosen operation.
#Check if the user's answer matches the correct answer.
#Display feedback as "Correct!" or "Incorrect."

x=int(input("Give some integer one"))
y=int(input("Give second integer"))
print("Now perform all addition subtraction division multiplication")
a=int(input("enter its output for addition"))
s=int(input("enter its output for subtraction"))
m=int(input("enter its output for multiplication"))
d=int(input("enter its output for division"))
j=x+y
l=x-y
k=x*y
i=x/y

if j==a:
    print("its correct")
else:
    print("its incorrect")
if s==l:
    print("its correct")
else:
    print("its incorrect")
if k==m:
    print("its correct")
else:
    print("its incorrect")
if i==d:
    print("its correct")
else:
    print("its incorrect")
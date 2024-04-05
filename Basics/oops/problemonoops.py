# class Person:
#     name=""
#     age=0

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def greet(self):
#         print("Hello,My name is ",self.name,"and my age is",self.age)

# class Test:
#     c1=Person("Akash",19) 
#     c1.greet()
#     akash=Person("Shivam",19) 
#     akash.greet()        

# class Rectangle:
#     length=0
#     breadth=0
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         a=self.length*self.breadth
#         print("the area is",a)
#     def perimeter(self):
#         p=2*(self.length+self.breadth)
#         print("the perimeter is",p)


# class Test:
#     c1=Rectangle(5,5)
#     c1.area()
#     c1.perimeter()

# class Numberchecker:
#     a=[]
#     def __init__(self,b):
#         self.a=b
#     def even_number(self):
#         for i in self.a:
#             if i%2==0:
#                 print(i,"this is even number")
#             else:
#                 print(i,"False")
        
# class Test:
#     b=[23,44,55,77,88,11]
#     a1=Numberchecker(b)
#     print(a1.even_number())
class Test:
    def armstrong(y):
        temp=str(y)
        l=len(temp)
        temp=int(y)
        sum=0
        for i in range(0,l):
            rem=temp%10
            temp=temp//10
            sum=sum+rem**l
        if sum==y:
            print("number is armstrong")
        else:
            print("number is not armstrong")
    def primenumber(y):
        temp=y
        check=False
        for i in range(2,temp//2):
            if temp%i==0 and temp!=i:
                check=True
                break
            
        if (check):
            print(temp,"is not prime number")
        else:
            print(temp,"is a prime number")

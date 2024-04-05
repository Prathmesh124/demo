# x= int(input("enter  totalcount of ids of foot ball team"))
# a=set()
# for i in range(0,x):
#     b=int(input("enter id of foot ball team"))
#     a.add(b)
# x= int(input("enter  totalcount of ids of cricket team"))
# c=set()
# for i in range(0,x):
#     b=int(input("enter id of cricket team"))
#     c.add(b)

# d=a.intersection(c)
# e=list(d)
# print(d)
# a="thr jshfskjf sjfhdkjfh hhsijch kjhsdkjh kjhsdkjh"
# a=a.replace(" ","")
# b=a.upper()
# print(b)


# def palindrome(n):
#     b=str(n)
#     a=b[::-1]
#     if a==b:
#         print("number is palindrome")
#     else:
#         print("number is not palindrome")

# a=int(input("enter number to check its palindrome or not"))
# palindrome(a)

# a=[1,5,7,8,9,2]
# sum=0
# for i in a:
#     if i%2==0:
#         sum=sum+i
# print(sum)
# class Employee:
#     name=""
#     age=0
#     salary=0
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def printname(self):
#         print(self.name)
#     def printage(self):
#             print(self.age)
#     def printsalary(self):
#         print(self.salary)
# class Test:
#      arun=Employee("Arun",20,180000)
#      arun.printname()
# a=int(input("enter number to find its factorial"))
# sum=1
# for i in range(1,a+1):
#    sum=sum*i
# print(sum)
# a=[2,2,4,6,7,7,8,9,1,1]
# for i in a:
#     r=a.index(i)
#     for b in a:
#         k=a.index(b)
#         if i==b and r!=k:
#             a.remove(b)   
# print(a)
# a = [2, 2, 4, 6, 7, 7, 8, 9, 1, 1]
# unique_list = []
# for i in a:
#     if i not in unique_list:
#         unique_list.append(i)

# print(unique_list)

# a=["apple","bannana","orange","bannana","apple","bannana"]
# unique_list = []
# for i in a:
#     if i not in unique_list:
#         unique_list.append(i)
# for j in unique_list:
#     print(j,a.count(j))
# a=[1,2,5,8,7,11,25]
# a.sort()
# print(a[-2])
# a=0
# n= int(input("enter"))
# print(a)
# b=1
# k=0
# for i in range(0,n):
#     k=a+b
#     a=b
#     b=k
#     print(b)
# my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 20}
# max_value = max(my_dict.values())
# max_key=[]
# for key, value in my_dict.items():
#     if value == max_value:
#         max_key.append(key)
# print(max_value, max_key)      

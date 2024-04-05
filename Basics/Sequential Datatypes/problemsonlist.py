#Find the largest and smallest element in a list of numbers:
# Write code that finds the largest and smallest numerical values in a given list.
# Example: Input [8, 2, 15, 3, 9] should output Largest: 15, Smallest: 2.
# x=[8,2,15,3,9]
# min=x[0]
# max=x[0]
# for i in x:
#     if min>i:
#         min=i
#     if max<i:
#         max=i
# print(max,min)

#Check if a specific element exists in a list and return its index if found:
# Write code that searches for a given element in a list and returns its index if it exists, otherwise returns -1.
# Example: Input my_list = [5, 7, 3, 9] and search_value = 3 should output Index of 3: 2.
# my_list=[]
# a=int(input("Enter total number in list"))
# for i in range(0,a):
#     x=int(input("enter number to add in list"))
#     my_list.append(x)
# b=int(input("Enter number to search"))
# print("index of",b,":",my_list.index(b))



# Remove all duplicate elements from a list and print the unique elements:


# Write code that removes all duplicates from a list, preserving only the unique elements.
# Example: Input [2, 5, 2, 8, 5, 1] should output [2, 5, 8, 1].

#Remove all duplicate elements from a list and print the unique elements:
# Write code that removes all duplicates from a list, preserving only the unique elements.
# Example: Input [2, 5, 2, 8, 5, 1] should output [2, 5, 8, 1]

# input_list = [2, 5, 2, 8, 5, 1]
# unique_elements = []
# for item in input_list:
#     if item not in unique_elements:
#         unique_elements.append(item)
# print(unique_elements)



#Merge two lists and sort the combined list in ascending order:


# Write code that takes two lists as input, merges them into a single list, and sorts the resulting list in ascending order.
# Example: Input list1 = [3, 1, 5] and list2 = [2, 4, 6] should output [1, 2, 3, 4, 5, 6].
# a=[3,1,5]
# b=[2,4,6]
# output=[]
# output=a+b
# print(output)
# for i in range(0,len(output)):
#     for j in range(i+1,len(output)):
#         if output[i]>output[j]:
#             a=output[j]
#             output[j]=output[i]
#             output[i]=a
# print(output)


# Write code that counts how many times each unique element appears in a list.
# Example: Input ["apple", "banana", "apple", "cherry", "banana"] should output apple: 2, banana: 2, cherry: 1.
# a=["apple", "banana", "apple", "cherry", "banana"]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# for i in b:
#     print(i,a.count(i))


# Find the sum of all elements in a list:


# Write code that calculates the sum of all numerical values in a list.
# Example: Input [5, 10, 2, 8, 1] should output Sum: 26.
# a= [5, 10, 2, 8, 1]
# sum=0
# for i in a:
#     sum+=i
# print(sum)

# Rotate the elements of a list by a specified number of positions:


# Write code that shifts the elements of a list to the right by a given number of positions.
# Example: Input my_list = [1, 2, 3, 4, 5] and rotate_by = 2 should output [4, 5, 1, 2, 3].
# my_list = [1, 2, 3, 4, 5]
# rotate_by = 2
# i=0
# while i<=rotate_by:
#     a=my_list[0]
#     my_list.remove(a)
#     my_list.append(a)
#     i+=1
# print(my_list)  

# 1. Create a list with the names of your favorite fruits. Print the list.

# 2. Given a list of numbers, double each element and print the modified list.

# a=[1,2,8,3,4,5,6,7,8]
# for i in range(0,len(a)):
#     a[i]=a[i]*2

# print(a)

# Split a list into sub-lists of equal size:


# Write code that divides a list into smaller sub-lists of a given size.
# Example: Input my_list = [1, 2, 3, 4, 5, 6, 7, 8] and sub_list_size = 3 should output [[1, 2, 3], [4, 5, 6], [7, 8]].
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# sub_list_size = 3
# sub_list=[]
# for i in range(0,len(my_list),sub_list_size):
#     sub_list.append(my_list[i:i+sub_list_size])
# print(sub_list)

# 5. Take a list of words and sort them in alphabetical order. Print the sorted list.

# anim=["jake","alhg","avghfhd","hfhf","eaegfhh"]
# n = len(anim)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if anim[j] > anim[j+1]:
#             anim[j], anim[j+1] = anim[j+1], anim[j]
# print(anim)

# Given a tuple of fruits, find the ones with more than 5 characters.

# a=("banana","apple","mango","papaya","blueberry")
# for i in range(0,len(a)):
#     if len(a[i])>5:
#         print(a[i])


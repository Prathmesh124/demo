#(a) 1, 4, 9, 16,
for i in range(1,11):
    print(i*i,end=" ")

#(b)1, 2, 4, 7, 11
ft=1
for i in range(0,11):
    k=ft+i
    print(k)
    ft=k    

#(c) 3, 6, 9, 12
i=3
for j in range(1,11):
    print(3*j)

#4, 8, 16, 32
j=2
i=4
print(i,end=" ")
for k in range(1,11):
    print(4*j,end=" ")
    j*=2  

# 1.5, 3.0, 4.5, 6.0
i=1.5
for j in range(1,11):
    print(1.5*j,end=" ")

#(f) 0, 7, 26
for i in range(1,11):
    k=(i**3)-1
    print(k)



#(g) 1, 9, 25, 49
for i in range(1,20,2):
    print(i*i)

#(h) 4, 16, 36, 64
for i in range(2,20,2):
    print(i*i)

#(i) 0, 3, 8, 15
k=0
print(k)
for i in range(3,20,2):
    print(k+i)
    k=k+i

#(j) 24, 99, 224, 399
for i in range(5,50,5):
    k=(i**2)-1
    print(k)



#(k) 2, 5, 10, 17
j=1
for i in range(1,11,2):
    print(i+j)
    j=j+i


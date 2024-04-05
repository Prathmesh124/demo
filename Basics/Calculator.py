x=int(input("enter number one"))
y=int(input("enter number two"))
z=input("operation you need to perform +,/,-,*")
match(z):
    case "+":
        k=x+y
        print("sum of", x ,"and", y , "is",k)
    case "-":
        k=x-y
        print("differance of",x ,"and", y , "is",k)
    case "/":
        k=x/y
        print("division",x ,"and", y , "is",k)
    case "*":
        k=x*y
        print("product", x ,"and", y ,"is",k)
    case _:
        print("invalid operation")    
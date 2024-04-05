num1=0
num2=0

class myerror(Exception):
    pass
try:
    result = num1 / num2 # Potential ZeroDivisionError
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Division by zero is not allowed!")
else:
    print(f"The result is: {result}")

raise myerror("happy birthday")

# try:
#     file = open("myfile.txt", "r")
# except FileNotFoundError:
#     print("The specified file does not exist.")
# finally:
#     if file:
#         file.close()  # Ensure file closure even if an exception occurs

# try:
#     my_dict = {"a": 1, "b": 2}
#     value = my_dict["c"]  # Potential KeyError
# except KeyError:
#     print("The key 'c' does not exist in the dictionary.")

# raise ValueError("This is a custom exception that I raised.")  # Manually raising an exception


# score=int(input("enter your score"))
# if score>90:
#     print("Execellent")
# elif score>80 and score<=90:
#     print("Good job")
# elif score>70 and score<=80:
#     print("need improvement")
# elif score<=70:
#     print("study harder")
# else:
#     print("invalid input")


# j=7
# for i in range(1,4):
#     guess=int(input("enter a random number btw 1 to 10"))
#     if guess>j:
#         print("too high")
#     elif guess<j:
#         print("too low")
#     else:
#         print("you guessed it")
#         break
#     if i==3:
#         print("game over")    

# x=int(input("enter your time "))
# y=False
# if x<=12 and x>1:
#     print("breakfast")
# elif x>12 and x<17:
#     print("lunch")
# else:
#     print("dinner")
#     y=int(input("want reservation press 0 for no and 1 for yes "))
#     if(y):
#         print("you are eligible for 10 percent discount")
#     else:
#         print("sorry no discount")

# x=input("apples,bananas,icecream,cookies any of them")
# if(x=="apples" or x=="bananas"):
#     print("healthy choice")
# elif(x=="icecream" or x=="cookies"):
#     print("treat time!")
# else:
#     print("invalid input")

# age=int(input("enter your age"))
# if age>=18:
#     print("old enough to vote ,drive and watch 18+ movies ")
# else:
#     print("18 ka ho ja pehle")

# bill=int(input("tell me your total bill"))
# age=int(input("tell me your age for discount"))
# if bill>50 and age<60:
#     print("you are eligible for 10 percent discount")
# elif bill<50 and age>=60:
#     print("you are eligible for 5 percent discount")
# elif bill>50 and age>=60:
#     print("you are eligible for 15 percent discount")
temp=int(input("enter temp"))
if temp>=90:
    print("too hot ")
elif temp<90 and temp>=30:
    print("moderate")
else:
    print("brrr!")

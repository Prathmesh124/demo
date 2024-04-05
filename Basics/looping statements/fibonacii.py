firstterm=0
secondterm=1
nextterm=0
for i in range(0,11):
    print(nextterm)
    nextterm=firstterm+secondterm
    firstterm=secondterm
    secondterm=nextterm
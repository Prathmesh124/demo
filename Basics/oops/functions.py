def run(x):
    if (x<=100):
        print(x,end=" ")
        run(x+1)
run(0)
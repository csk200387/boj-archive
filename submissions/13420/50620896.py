num = int(input())
for i in range(num) :
    a = input().replace(" ","").split("=")
    if eval(a[0]) == int(a[1]) :
        print("correct")
    else :
        print("wrong answer")
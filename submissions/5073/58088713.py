import sys
input = lambda:sys.stdin.readline().rstrip()

while True :
    a, b, c = map(int, input().split())
    if a == b == c == 0 :
        break
    elif (a+b+c) - max(a,b,c) <= max(a,b,c) :
        print("Invalid")
    else :
        if a == b == c :
            print("Equilateral")
        elif a == b or b == c or c == a :
            print("Isosceles")
        else :
            print("Scalene")
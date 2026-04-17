import sys
input = lambda:sys.stdin.readline().rstrip()

while True:
    a, b, c = input().split()
    a, c = int(a), int(c)
    result = 0
    if a == c == 0 and b == "W":
        break
    if b == "W":
        resut = a-c
    else:
        resut = a+c

    if resut < 0:
        print("Not allowed")
    else:
        print(resut)
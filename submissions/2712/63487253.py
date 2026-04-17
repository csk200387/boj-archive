import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
for i in range(n) :
    t, d = input().split()
    t = float(t)
    if d == "kg":
        print(f"{t*2.2046:.4f} lb")
    elif d == "l":
        print(f"{t*0.2642:.4f} g")
    elif d == "lb":
        print(f"{t*0.4536:.4f} kg")
    elif d == "g":
        print(f"{t*3.7854:.4f} l")
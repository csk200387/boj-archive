import sys
input = lambda:sys.stdin.readline().rstrip()

for i in range(int(input())):
    h, c = map(int, input().split())
    h = bin(h)[2:]
    if h.count('1') % 2 == 0 and c == 0:
        print("Valid")
    elif h.count('1') % 2 == 1 and c == 1:
        print("Valid")
    else:
        print("Corrupt")
import sys
input = lambda:sys.stdin.readline().rstrip()

c = 1
stack = []

for i in range(int(input())) :
    s = int(input())
    while c <= s :
        stack += [c]
        c += 1
        print("+")
    if stack.pop() == s :
        print("-")
    else:
        print("NO")
        exit(0)
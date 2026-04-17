import sys
input = lambda:sys.stdin.readline().rstrip()

c = 1
stack = []
re = []
for i in range(int(input())) :
    s = int(input())
    while c <= s :
        stack += [c]
        c += 1
        re.append("+")
    if stack.pop() == s :
        re.append("-")
    else:
        print("NO")
        exit(0)
print(*re, sep="\n")
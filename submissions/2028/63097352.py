import sys
input = lambda:sys.stdin.readline().rstrip()
for i in range(int(input())):
    n = int(input())
    result = n**2
    if str(result).find(str(n), -len(str(n))) != -1:
        print("YES")
    else:
        print("NO")
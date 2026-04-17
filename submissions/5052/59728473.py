import sys
input = lambda:sys.stdin.readline().rstrip()

t = int(input())
for i in range(t):
    n = int(input())
    s = [input() for j in range(n)]
    s.sort()
    for j in range(1, n):
        if s[j-1] == s[j][:len(s[j-1])]:
            print("NO")
            break
    else:
        print("YES")
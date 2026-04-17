import sys
input = lambda:sys.stdin.readline().rstrip()
def power(n, m):
    if m == 0:
        return 1
    elif m % 2 == 0:
        half = power(n, m // 2)
        return half * half
    else:
        half = power(n, (m - 1) // 2)
        return half * half * n

for i in range(int(input())) :
    n = int(input())
    result = power(n, 2)
    if str(result).find(str(n), -len(str(n))) != -1:
        print("YES")
    else:
        print("NO")
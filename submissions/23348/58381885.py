import sys
input = lambda:sys.stdin.readline().rstrip()
a, b, c = map(int, input().split())
N = int(input())
arr = [0]*N
for i in range(N) :
    s = 0
    for l in range(3) :
        x, y, z = map(int, input().split())
        s += x*a + y*b + z*c
    arr[i] = s
print(max(arr))
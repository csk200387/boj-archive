import sys
input = lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())):
    n = int(input())
    arr = sorted(map(int, input().split()))
    t = [arr[i]for i in range(n)if i%2==0]+[arr[i]for i in range(n)if i%2==1][::-1]
    nm = 0
    for i in range(1,n):
        p = abs(t[i-1]-t[i])
        if nm < p:nm=p
    print(nm)
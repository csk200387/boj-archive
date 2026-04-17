n = int(input())
arr = sorted(map(int, input().split()))
res = 0
for i in range(n):
    res += sum(arr[0:i+1])
print(res)
x, n = map(int, input().split())
arr = list(map(int, input().split()))
sums = [sum(arr[:n])]
for i in range(n, x):
    sums.append(sums[-1]-arr[i-n]+arr[i])
mx = max(sums)
if mx == 0:
    print("SAD")
else:
    print(mx)
    print(sums.count(mx))
arr = []
for i in range(int(input())) :
    arr.append(tuple(map(int, input().split())))
n = len(arr)
S = 0.0
for i in range(n):
    j = (i + 1) % n
    S += arr[i][0] * arr[j][1]
    S -= arr[j][0] * arr[i][1]
S = abs(S) / 2.0
print(round(S, 2))
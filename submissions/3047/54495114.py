arr = list(map(int, input().split()))
t = []
for i in sorted(input()) :
    t.append(arr[65-ord(i)])
print(*t, sep=" ")
input()
arr = map(int, input().split())
t = 1
count = 0
for i in arr:
    if t < i:
        count += 1
    t = i
print(count)
d=input()
l=len(d)//3
arr = [d[i:i+l] for i in range(0, len(d), l)]
max = ""
c = 0
for i in arr:
    if arr.count(i) > c:
        c = arr.count(i)
        max = i
print(max)
arr = [1,1,1]
n = int(input())
while len(arr) != n:
    arr.append(arr[-1] + arr[-3])
print(arr[-1])
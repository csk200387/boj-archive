n = int(input())
arr = [*map(int, input().split())]

a, b = 0, 0
for i in range(n) :
    a += ((arr[i]//30) + 1) * 10
    b += ((arr[i]//60) + 1) * 15
r = "Y"
if a == b :
    r = "Y M"
elif a > b :
    r = "M"

print(r, min(a,b))
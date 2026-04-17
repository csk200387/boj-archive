n,*arr=open(0)
A,B = 0, 0
for i in range(int(n)):
    a, b = map(int, arr[i].split())
    if a == b:
        continue
    elif a > b:
        A += 1
    elif b > a:
        B += 1
print(A,B)
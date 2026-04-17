a = list(map(int,input().split()))
b = list(map(int,input().split()))
at, bt = 0, 0
for i in range(9):
    at += a[i]
    bt += b[i]
    if at > bt:
        print("Yes")
        exit()
print("No")
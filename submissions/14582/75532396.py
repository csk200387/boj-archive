a = list(map(int,input().split()))
b = list(map(int,input().split()))
at, bt = 0, 0
for i in range(18):
    if i%2==0:
        at += a[i//2]
    else:
        bt += b[i//2]
    if at > bt:
        print("Yes")
        exit()
print("No")
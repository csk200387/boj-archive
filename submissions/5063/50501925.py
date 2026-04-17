num = int(input())
for i in range(num):
    a = list(map(int,input().split()))
    m = a[1] - a[2]
    if a[0] < m :
        print("advertise")
    elif a[0] > m :
        print("do not advertise")
    else :
        print("does not matter")
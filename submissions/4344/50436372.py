num = int(input(""))
for i in range(0,num):
    arr = list(map(int,input().split()))
    maxr = arr[0]
    del arr[0]
    avg = sum(arr)/maxr
    avgup = 0
    for a in arr:
        if a > avg :
            avgup += 1
    res = avgup/maxr * 100
    print(f'{res:.3f}%')
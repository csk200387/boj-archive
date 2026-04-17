num = int(input(""))
for i in range(0,num):
    arr = list(map(int,input().split()))
    avg = sum(arr[1:])/arr[0]
    avgup = 0
    for a in arr:
        if a > avg :
            avgup += 1
    res = avgup/arr[0] * 100
    print(f'{res:.3f}%')
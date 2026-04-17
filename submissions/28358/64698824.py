import sys
input = lambda:sys.stdin.readline().rstrip()
dateDict = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

# 등장하면 1, 등장하지 않으면 0
n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    months = {*range(1,13)}
    discarded = set()
    result = 0

    for i in range(10):
        if arr[i] == 1:
            for tmp_m in range(1, 13):
                if str(i) in str(tmp_m):
                        months.discard(tmp_m)
                        discarded.add(str(i))

    if len(months) == 0:
        print(0)
        continue
    for m in months:
        for d in range(1, dateDict[m]+1):
            if set(str(d)) & discarded == set():
                result += 1
    print(result)
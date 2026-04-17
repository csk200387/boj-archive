n,*arr=map(int, open(0))
cnt = 0
while (mx:=max(enumerate(arr), key=lambda x: x[1])[0]) != 0:
    arr[mx] -= 1
    arr[0] += 1
    cnt += 1
arr.sort()
if len(arr) > 1 and arr[-1] == arr[-2]:
    print(cnt+1)
else:
    print(cnt)
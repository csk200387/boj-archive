def findLayer(n:int) -> int :
    i = 0
    while 1 :
        i += 1
        if int(i*(i+1)/2) >= n :
            return i
n = int(input())
f = findLayer(n)
arr = [f"{i+1}/{f-i}" for i in range(f)]
index = n-int(f*(f-1)/2)-1
if n == 1 :
    print("1/1")
elif n == 2 :
    print("1/2")
elif n%2 != 0 :
    print(arr[index])
else :
    print(arr[::-1][index])
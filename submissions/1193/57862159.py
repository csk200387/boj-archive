def findLayer(n:int) -> int :
    i = 0
    sum = 0
    while 1 :
        i += 1
        t = int(i*(i+1)/2)
        if t >= n :
            return i, t
def findFrac(n:int) :
    f, s = findLayer(n)
    arr = [f"{i+1}/{f-i}" for i in range(f)]
    if n == 1 :
        print("1/1")
    elif f%2 != 0 :
        print(arr[s-n])
    else :
        print(arr[f-s+n-1])

findFrac(int(input()))
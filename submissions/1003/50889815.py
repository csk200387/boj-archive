import sys
input = sys.stdin.readline
def fibo(n) :
    global a, b
    if n == 0 :
        a += 1
        return 0
    elif n == 1 :
        b += 1
        return 1
    else :
        return fibo(n-1) + fibo(n-2)
n = int(input().rstrip())
for i in range(n) :
    a, b = 0, 0
    fibo(int(input().rstrip()))
    print(a,b)
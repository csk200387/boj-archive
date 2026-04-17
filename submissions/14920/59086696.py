def cfun(n, i=1) :
    if n == 1 :
        return i
    elif n%2 == 0 :
        return cfun(n//2, i+1)
    else :
        return cfun(3*n+1, i+1)
num = int(input())
print(cfun(num))
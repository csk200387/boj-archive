i = 1
def cfun(n) :
    global i
    if n == 1 :
        return i
    elif n%2 == 0 :
        i += 1
        return cfun(n//2)
    else :
        i += 1
        return cfun(3*n+1)
num = int(input())
print(cfun(num))
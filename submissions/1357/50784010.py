def Rev(n) :
    n = str(n)
    n = int(n[::-1])
    return n
a = input().split()
print(Rev(Rev(a[0])+Rev(a[1])))
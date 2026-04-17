def convert(n, base):
    T = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    q, r = divmod(n, base)

    return convert(q, base) + T[r] if q else T[r]

a, b = map(int,input().split())
print(convert(a,b))
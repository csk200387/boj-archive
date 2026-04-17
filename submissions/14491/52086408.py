def conv(n, base):
    T = "0123456789" # A-Z
    q, r = divmod(n, base)
    return conv(q, base) + T[r] if q else T[r]

print(conv(int(input()), 9))
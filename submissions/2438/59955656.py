def star(n):
    if n == 0:
        return
    star(n-1)
    print("*"*n)
star(int(input()))
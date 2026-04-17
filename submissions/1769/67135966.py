def main():
    n = input
    p = print
    t = n()
    stack = 0
    while len(t) > 1 :
        stack += 1
        t = str(sum(map(int, t)))
    p(stack)
    p("NO" if int(t)%3>0 else "YES")

main()
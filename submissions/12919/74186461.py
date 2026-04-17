d=input()
g=input()
def sol(t):
    if t == d:
        print(1)
        exit()
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        sol(t[:-1])
    if t[0] == 'B':
        sol(t[1:][::-1])

sol(g)
print(0)
def d(n):
    global ar
    global count
    if n%2 == 1 :
        ar.append(count)
    if n//2 == 0:
        return str(n%2)
    count += 1
    return d(n//2)+str(n%2)
for _ in range(int(input())) :
    count = 0
    ar = []
    N = int(input())
    d(N)
    print(" ".join(map(str,ar)))
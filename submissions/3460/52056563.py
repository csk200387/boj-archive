count = 0
def d(n):
    global count
    if n%2 == 1 :
        print(count, end=" ")
    if n//2 == 0:
        return str(n%2)
    count += 1
    return d(n//2)+str(n%2)
for _ in range(int(input())) :
    N = int(input())
    d(N)
import sys
input = lambda:sys.stdin.readline().rstrip()
def prime(n):
    status = True
    if n < 3:
        return 2
    while 1:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                status = False
                break
        if status:
            return n
        n += 1
        status = True
n = int(input())
for _ in range(n):
    print(prime(int(input())))
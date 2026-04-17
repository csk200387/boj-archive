import sys
input = lambda:sys.stdin.readline().rstrip()

def count_factors_zero2(n):
    count = 0
    for i in range(1, 13):
        count += n // (5 ** i)
    return count


n = int(input())

for i in range(n) :
    t = int(input())
    print(count_factors_zero2(t))
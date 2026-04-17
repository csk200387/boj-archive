import sys
sys.setrecursionlimit(7000)
def prob(n) :
    if n == 1 :
        return 2%10
    if n % 2 == 0 :
        a = prob(n//2)
        return a * a % 10
    else :
        a = prob(n//2)
        return a * a * 2 % 10
print(prob(int(input())))
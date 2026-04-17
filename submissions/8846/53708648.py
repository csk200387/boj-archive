n = int(input())
def prob(n) :
    if n == 1 :
        return 4
    if n % 2 == 0 :
        a = prob(n//2)
        return a * a
    else :
        a = prob(n//2)
        return a * a * 4
print(((prob(n))//3)%500000009)
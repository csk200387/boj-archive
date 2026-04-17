A, B, C = map(int,input().split())
def prob(n) :
    if n == 1 :
        return A%C
    if n % 2 == 0 :
        a = prob(n//2)
        return a * a % C
    else :
        a = prob(n//2)
        return a * a * A % C
print(prob(B))
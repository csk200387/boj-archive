def prob_1(n:int) -> int :
    return sum(map(int, str(n)))

def prob_2(n:int) -> int :
    n = sum(map(int, str(n)))
    if n < 10 :
        if n % 3 == 0 :
            return True
        return False
    else :
        return False

t = int(input())
stack = 0
while t > 9 :
    stack += 1
    t = prob_1(t)

print(stack)
print("YES" if prob_2(t) else "NO")
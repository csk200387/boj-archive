b = eval(input().replace(" ","+"))
p = int(input())
print(b - p*2 if b >= p*2 else b)
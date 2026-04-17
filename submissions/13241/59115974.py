a, b = map(int, input().split())
r = a*b
while b > 0 :
    a, b = b, a % b
print(int(r/a))
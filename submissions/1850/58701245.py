a, b = map(int, input().split())
while a > 0 :
    a, b = b, a % b
print("1"*a)